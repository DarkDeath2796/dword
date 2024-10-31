import http.server

# Run website at localhost:6896

print("starting")
http.server.HTTPServer(("localhost", 3000), http.server.SimpleHTTPRequestHandler).serve_forever()