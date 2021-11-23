from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
<head>
<title>My webserver</title>
</head>
<body>
<h1>TOP FIVE PROGRAMMING LANGUAGES</h1>
<h2>1. Python</h2>
Python is an easy to learn, object-oriented, high level language, interpreted, dynamic and multipurpose programming language. Python is commonly used for developing websites and software, task automation, data analysis, and data visualization.Python applications include Developing websites and software, Aritifical Intelligence, Data Science, Machine Learning.
<h2>2.C#</h2>
C# is a general-purpose, multi-paradigm programming language. C# encompasses static typing, strong typing, lexically scoped, imperative, declarative, functional, generic, object-oriented, and component-oriented programming disciplines.Uses of C# are Developing desktop applications, Web-based Applications, Web services, Game development in Unity.
<h2>3. Java</h2>
Java is a high-level, class-based, object-oriented programming language that is designed to have as few implementation dependencies as possible. Java applications are typically compiled to bytecode that can run on any Java virtual machine (JVM) regardless of the underlying computer architecture.Uses of Java include Mobile App Development, Web-based Applications, Gaming Applications, IoT Applications.
<h2>4.C</h2>
C is a general-purpose, procedural computer programming language supporting structured programming, lexical variable scope, and recursion, with a static type system. C is an imperative procedural language. It was designed to be compiled to provide low-level access to memory and language constructs that map efficiently to machine instructions, all with minimal runtime support. Despite its low-level capabilities, the language was designed to encourage cross-platform programming. Uses of C are Operating system development, Word processors & Spread sheets, Web services, Interpreters.
<h2>5. JavaScript</h2>
JavaScript often abbreviated as JS, is a programming language that conforms to the ECMAScript specification. JavaScript is high-level, often just-in-time compiled and multi-paradigm. It has dynamic typing, prototype-based object-orientation and first-class functions. Applications of JavaScript include Validating User’s Input, Simple Client-side Calculations, Generating HTML Content, Detecting the User’s Browser and OSDetecting the User’s Browser and OS.
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
