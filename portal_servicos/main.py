import os
from flask import Flask, request, send_from_directory, render_template_string

app = Flask(__name__)

# Define the root directory for static files
STATIC_DIR = os.path.join(os.path.dirname(__file__), 'static')

@app.route('/')
def serve_html():
    try:
        # Serve the main HTML file
        with open('index.html', 'r', encoding='utf-8') as file:
            content = file.read()
        return render_template_string(content)
    except Exception as e:
        print(f"Error serving HTML: {e}")
        return "Internal Server Error", 500

@app.route('/static/<path:path>')
def serve_static(path):
    try:
        # Serve static files (CSS, images, etc.)
        return send_from_directory(STATIC_DIR, path)
    except Exception as e:
        print(f"Error serving static file: {e}")
        return "Internal Server Error", 500

def hello_world(request):
    try:
        with app.test_request_context(request.path, method=request.method, data=request.data, headers=request.headers):
            return app.full_dispatch_request()
    except Exception as e:
        print(f"Error in hello_world function: {e}")
        return "Internal Server Error", 500
