#!/usr/bin/env python3
import http.server
import socketserver
import sys

PORT = 8081

Handler = http.server.SimpleHTTPRequestHandler

try:
    with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
        print(f"Server running at http://0.0.0.0:{PORT}/")
        sys.stdout.flush()
        httpd.serve_forever()
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
