from flask import Blueprint, jsonify
from methods.file_operation import list_files, move_file

file_blueprint = Blueprint('file_blueprint', __name__)

@file_blueprint.route('/list_files', methods=['GET'])
def route_list_files():
    files = list_files('source_data')
    return jsonify(files)

@file_blueprint.route('/move_file/<filename>', methods=['GET'])
def route_move_file(filename):
    result = move_file('source_data', 'processed_data', filename)
    return jsonify(result)

@file_blueprint.route('/', methods=['GET'])
def home():
    # HTML content to be displayed
    html_content = """
    <html>
        <head>
            <title>Welcome to File Manager</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    text-align: center;
                    margin-top: 50px;
                }
                h1 {
                    color: #333;
                }
                p {
                    color: #666;
                }
            </style>
        </head>
        <body>
            <h1>Welcome to File Manager</h1>
            <p>Use our API to manage files efficiently!</p>
        </body>
    </html>
    """
    return html_content

