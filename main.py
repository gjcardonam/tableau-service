from flask import Flask, request
from controllers.controllers import controllers

app = Flask(__name__)


@app.route('/tableau/<route>', methods=['POST'])
def router(route):
    # Content management
    content = {
        "json": request.get_json(silent=True),
        "file": request.files
    }

    return controllers(route, content)


if __name__ == '__main__':
    app.run(debug=True)
