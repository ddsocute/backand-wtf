from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
from student import Student, StudentList, StudentManagement, HEADER, TXT_PATH

PORT_NUMBER = 8080

# 先載入學生資料
students = Student.load_txt(TXT_PATH)
student_list = StudentList()
student_list.students = students  # 將已載入的 students 指派給 student_list


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 看有幾次考試生成幾個選項
        exam_times_html = ""
        for i in range(1, student_list.max_exam_times + 1):
            exam_times_html += f'<option value="{i}">Exam {i}</option>'

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()

        html = f"""
        <!DOCTYPE html>
        <head>
            <title>Student Management System</title>
        </head>
        <body>
            <h1>Choose function and Exam time</h1>
            <form action="/post_result" method="post">
                <label>Function choose:</label>
                <select name="function">
                    <option value="1">1. print students' grade</option>
                    <option value="2">2. print subjects' grade</option>
                    <option value="3">3. print students' rank</option>
                </select>
                <br><br>
                <label>Exam time:</label>
                <select name="exam_time">
                    {exam_times_html}
                </select>
                <br><br>
                <input type="submit" value="submit">
            </form>
        </body>
        </html>
        """  # 要回應的html
        self.wfile.write(html.encode())

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length).decode()
        params = parse_qs(post_data)

        func = params.get("function", [None])[0]
        exam_time_str = params.get("exam_time", [None])[0]
        func = int(func)
        exam_time = int(exam_time_str)
        result_html = self.handle_function(func, exam_time)

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(result_html.encode())

    def handle_function(self, func, exam_time):
        # 根據選擇的功能呼叫 student.py 中的方法
        if func == 1:
            displayed_student_list = StudentManagement.get_student_in_exam(
                students, exam_time
            )
            display_attribute_list = list(vars(students[0]).keys())
            # 總共有 name, phone, exam_history, total, average
            table = StudentManagement.display_student(
                exam_time, HEADER, displayed_student_list, display_attribute_list
            )
            return table.get_html_string()
        elif func == 2:
            displayed_subject_list = StudentManagement.get_subject(
                StudentManagement.get_student_in_exam(students, exam_time),
                exam_time,
            )
            header = ["subject", "total", "average"]
            table = StudentManagement.display_subject(header, displayed_subject_list)
            return table.get_html_string()

        elif func == 3:
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
        server = HTTPServer(("localhost", PORT_NUMBER), MyHandler)
        print("Started httpserver on port ", PORT_NUMBER)
        # Wait forever for incoming http requests
        server.serve_forever()

    except KeyboardInterrupt:
        print("^C received, shutting down the web server")
        server.socket.close()
