import os
from flask import Flask, request, send_from_directory, render_template_string

app = Flask(__name__)

# Define the root directory for static files
STATIC_DIR = os.path.join(os.path.dirname(__file__), 'static')

@app.route('/')
def serve_html():
    # Serve the main HTML file
    with open('index.html', 'r', encoding='utf-8') as file:
        content = file.read()
    return render_template_string(content)

@app.route('/static/<path:path>')
def serve_static(path):
    # Serve static files (CSS, images, etc.)
    return send_from_directory(STATIC_DIR, path)

def hello_world(request):
    with app.test_request_context(request.path, method=request.method, data=request.data, headers=request.headers):
        return app.full_dispatch_request()
