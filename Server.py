import json
from Log import log
from http.server import BaseHTTPRequestHandler, HTTPServer
from Settings import HOST, PORT


class RequestHandler(BaseHTTPRequestHandler):
    '''处理请求并返回页面'''

    # 页面模板
    Page = '''\
        <html>
        <body>
        <p>{}</p>
        </body>
        </html>
    '''

    # 处理一个GET请求
    def do_GET(self):
        
        # log.update("(Server): HTTP GET /")
        
        content = str(log.get_data())
        content = self.Page.format(content)
        
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content.encode())

#----------------------------------------------------------------------

def server():
    host = HOST
    port = PORT
    serverAddress = (host, port)
    log.update("(Server): http://{}:{}/".format(host, port))
    server = HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()
