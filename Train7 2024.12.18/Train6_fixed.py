from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
from student import Student, StudentList, StudentManagement, HEADER, TXT_PATH

PORT_NUMBER = 8080

# 先載入學生資料
students = Student.load_txt(TXT_PATH)
student_list = StudentList()
student_list.students = students


class MyHandler(BaseHTTPRequestHandler):
    # 繼承BaseHTTPRequestHandler，並覆寫其中的method
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            home = """
            <!DOCTYPE html>
            <html>
            <head>
                <title>Student Management System</title>
            </head>
            <body>
                <a href="http://localhost:8080/1" target="_blank">Function1</a>
                <br><br>
                <a href="http://localhost:8080/2" target="_blank">Function2</a>
                <br><br>
                <a href="http://localhost:8080/3" target="_blank">Function3</a>
                <br><br>
            </body>
            </html>
            """
            self.wfile.write(home.encode())
        elif self.path == "/1":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            result_html = ""
            for exam_time in range(1, student_list.max_exam_times + 1):
                result_html += self.handle_function(1, exam_time)
            func1 = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Function2</title>
            </head>
            <body>
                {result_html}
            </body>
            </html>
            """
            self.wfile.write(func1.encode())
        elif self.path == "/2":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            result_html = ""
            for exam_time in range(1, student_list.max_exam_times + 1):
                result_html += self.handle_function(2, exam_time)
            func2 = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Function2</title>
            </head>
            <body>
                {result_html}
            </body>
            </html>
            """
            self.wfile.write(func2.encode())
        elif self.path == "/3":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            result_html = ""
            for exam_time in range(1, student_list.max_exam_times + 1):
                result_html += self.handle_function(3, exam_time)
            func3 = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Function2</title>
            </head>
            <body>
                {result_html}
            </body>
            </html>
            """
            self.wfile.write(func3.encode())
        return

    def handle_function(self, function, exam_time):
        # 根據選擇的功能呼叫 student.py 中的方法
        if function == 1:
            displayed_student_list = StudentManagement.get_student_in_exam(
                students, exam_time
            )
            display_attribute_list = list(vars(students[0]).keys())
            # 總共有 name, phone, exam_history, total, average
            table = StudentManagement.display_student(
                exam_time, HEADER, displayed_student_list, display_attribute_list
            )
            return table.get_html_string()
        elif function == 2:
            displayed_subject_list = StudentManagement.get_subject(
                StudentManagement.get_student_in_exam(students, exam_time),
                exam_time,
            )
            header = ["subject", "total", "average"]
            table = StudentManagement.display_subject(header, displayed_subject_list)
            return table.get_html_string()

        elif function == 3:
            displayed_student_list = StudentManagement.get_student_rank(
                StudentManagement.get_student_in_exam(students, exam_time),
                exam_time,
            )
            header = ["rank", "name", "average"]
            display_attribute_list = ["name", "average"]
            table = StudentManagement.display_student(
                exam_time,
                header,
                displayed_student_list,
                display_attribute_list,
                rank=True,
            )
            return table.get_html_string()


if __name__ == "__main__":
    try:
        # Create a web server and define the handler to manage the incoming request
        server = HTTPServer(("localhost", PORT_NUMBER), MyHandler)  # 實例化
        print("Started httpserver on port ", PORT_NUMBER)
        # Wait forever for incoming http requests
        server.serve_forever()

    except KeyboardInterrupt:
        print("^C received, shutting down the web server")
        server.socket.close()
