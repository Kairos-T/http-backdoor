import http.server
import socketserver
import os
from datetime import datetime

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        upload_dir = "uploads"
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)

        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"uploaded_file_{timestamp}.tar.gz"

        with open(os.path.join(upload_dir, filename), 'wb') as f:
            f.write(post_data)

        self.send_response(200)
        self.end_headers()

PORT = 8123
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
