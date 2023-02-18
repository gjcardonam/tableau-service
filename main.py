from flask import Flask, request
from router.router import router

app = Flask(__name__)


@app.route('/tableau/<route>', methods=['POST'])
def controller(route):
    # Content management
    content = {
        "json": request.get_json(silent=True),
        "file": request.files
    }

    return router(route, content)


if __name__ == '__main__':
    app.run(debug=True)
