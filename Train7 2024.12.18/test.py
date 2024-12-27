import logging
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
from student import Student, StudentList, StudentManagement, HEADER, TXT_PATH

# 配置日誌
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 常數定義
HOST_NAME = "localhost"
PORT_NUMBER = 8080
HOME_PAGE = "/"
FUNCTION_PATHS = {
    "1": "Function1",
    "2": "Function2",
    "3": "Function3"
}

# 載入學生資料
students = Student.load_txt(TXT_PATH)
student_list = StudentList()
student_list.students = students

class StudentRequestHandler(BaseHTTPRequestHandler):
    """處理 HTTP GET 請求的處理器"""

    def do_GET(self):
        """處理 GET 請求"""
        parsed_path = urlparse(self.path)
        path = parsed_path.path

        logging.info(f"Received GET request for path: {path}")

        try:
            if path == HOME_PAGE:
                self.handle_home()
            elif path.strip("/") in FUNCTION_PATHS:
                func_id = path.strip("/")
                self.handle_function(func_id)
            else:
                self.handle_404()
        except Exception as e:
            logging.error(f"Error handling request: {e}")
            self.handle_500()

    def handle_home(self):
        """處理首頁請求"""
        logging.info("Handling home page request")
        content = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Student Management System</title>
        </head>
        <body>
            <h1>Welcome to the Student Management System</h1>
            <ul>
                <li><a href="/1">Function1</a></li>
                <li><a href="/2">Function2</a></li>
                <li><a href="/3">Function3</a></li>
            </ul>
        </body>
        </html>
        """
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(content.encode('utf-8'))

    def handle_function(self, func_id):
        """處理功能頁面請求"""
        logging.info(f"Handling function {func_id} request")
        function_title = FUNCTION_PATHS.get(func_id, "Unknown Function")
        result_html = ""

        try:
            func_number = int(func_id)
            for exam_time in range(1, student_list.max_exam_times + 1):
                result_html += self.generate_function_content(func_number, exam_time)
        except ValueError:
            logging.warning(f"Invalid function ID: {func_id}")
            self.handle_404()
            return

        content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>{function_title}</title>
        </head>
        <body>
            <h1>{function_title}</h1>
            {result_html}
            <br>
            <a href="/">Back to Home</a>
        </body>
        </html>
        """
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(content.encode('utf-8'))

    def generate_function_content(self, function, exam_time):
        """生成特定功能和考試時間的 HTML 內容"""
        if function == 1:
            student_list_exam = StudentManagement.get_student_in_exam(students, exam_time)
            display_attrs = ["name", "phone", "total", "average"]
            table = StudentManagement.display_student(
                exam_time, HEADER, student_list_exam, display_attrs
            )
            return table.get_html_string()
        elif function == 2:
            subject_list = StudentManagement.get_subject(
                StudentManagement.get_student_in_exam(students, exam_time),
                exam_time,
            )
            header = ["Subject", "Total", "Average"]
            table = StudentManagement.display_subject(header, subject_list)
            return table.get_html_string()
        elif function == 3:
            ranked_students = StudentManagement.get_student_rank(
                StudentManagement.get_student_in_exam(students, exam_time),
                exam_time,
            )
            header = ["Rank", "Name", "Average"]
            display_attrs = ["name", "average"]
            table = StudentManagement.display_student(
                exam_time,
                header,
                ranked_students,
                display_attrs,
                rank=True,
            )
            return table.get_html_string()
        else:
            return "<p>Unknown Function</p>"

    def handle_404(self):
        """處理 404 Not Found 錯誤"""
        logging.warning(f"Path not found: {self.path}")
        self.send_response(404)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        content = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>404 Not Found</title>
        </head>
        <body>
            <h1>404 Not Found</h1>
            <p>The requested URL was not found on this server.</p>
            <a href="/">Back to Home</a>
        </body>
        </html>
        """
        self.wfile.write(content.encode('utf-8'))

    def handle_500(self):
        """處理 500 Internal Server Error 錯誤"""
        self.send_response(500)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        content = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>500 Internal Server Error</title>
        </head>
        <body>
            <h1>500 Internal Server Error</h1>
            <p>There was an error processing your request.</p>
            <a href="/">Back to Home</a>
        </body>
        </html>
        """
        self.wfile.write(content.encode('utf-8'))

    def log_message(self, format, *args):
        """覆蓋 BaseHTTPRequestHandler 的 log_message 方法，使用 logging 代替"""
        logging.info("%s - - [%s] %s" %
                     (self.client_address[0],
                      self.log_date_time_string(),
                      format % args))


def run_server(host=HOST_NAME, port=PORT_NUMBER):
    """啟動 HTTP 服務器"""
    server_address = (host, port)
    httpd = HTTPServer(server_address, StudentRequestHandler)
    logging.info(f"Server started at http://{host}:{port}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()
        logging.info("Server stopped.")


if __name__ == "__main__":
    run_server()
