# app.py
from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
port = int(os.getenv("PORT", 8080))
print(f"serving on {port}")
HTTPServer(("", port), SimpleHTTPRequestHandler).serve_forever()
