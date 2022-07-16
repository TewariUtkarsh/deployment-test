from flask import Flask, render_template, request
from flask_cors import cross_origin, CORS
import os


app = Flask(__name__)
CORS(app=app)

# PORT = os.getenv('$PORT', 80)


@app.route('/', methods=['GET', 'POST'])
@cross_origin()
def index() -> str:
    return f"Test Deployment Pipeline Running....."


if __name__ == '__main__':
    app.run(debug=True)