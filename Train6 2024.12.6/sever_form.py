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
        # 設定HTTP 回應的狀態碼和標頭
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        # 看有幾次考試生成幾個選項
        exam_times_html = ""
        for i in range(1, student_list.max_exam_times + 1):
            exam_times_html += f'<option value="{i}">Exam {i}</option>'

        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Student Management System</title>
            <script>
                function updateAction() {{
                    const form = document.getElementById("mainForm");
                    const functionSelect = document.getElementById("functionSelect");
                    const selectedValue = functionSelect.value;
                    form.action = "/" + selectedValue; // 動態改變 action
                }}
            </script>
        </head>
        <body>
            <h1>Choose function and Exam time</h1>
            <form id="mainForm" action="1" method="post"> 
                <label>Function choose:</label>
                <select name="function" id="functionSelect" onchange="updateAction()">  
                <!-- 值被改變的時候 觸發前面寫的函數改路徑 -->
                    <option value="1">1. Print students' grade</option>
                    <option value="2">2. Print subjects' grade</option>
                    <option value="3">3. Print students' rank</option>
                </select>
                <br><br>  <!-- 插兩個換行 -->
                <label>Exam time:</label>
                <select name="exam_time">
                    {exam_times_html} 
                </select>
                <br><br>
                <input type="submit" value="submit">
                <!-- 所有資訊會提交到action指定的根路徑。 -->
            </form>
        </body>
        </html>
        """
        # 要回應的html
        self.wfile.write(html.encode())
        # 將http body 傳回去

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()

        content_length = int(self.headers["Content-Length"])  # 知道整個數據有多大
        post_data = self.rfile.read(content_length).decode()
        # 根據 Content-Length 的大小，讀取指定字節數的數據 再去把讀ㄉ奧內容解碼成字串
        params = parse_qs(post_data)  # 把剛剛解碼的內容轉換成字典
        # {'function': ['1'], 'exam_time': ['2']}

        func = int(params.get("function")[0])
        exam_time = int(params.get("exam_time")[0])
        result_html = self.handle_function(func, exam_time)
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
        server = HTTPServer(("localhost", PORT_NUMBER), MyHandler)  # 實例化
        print("Started httpserver on port ", PORT_NUMBER)
        # Wait forever for incoming http requests
        server.serve_forever()

    except KeyboardInterrupt:
        print("^C received, shutting down the web server")
        server.socket.close()
