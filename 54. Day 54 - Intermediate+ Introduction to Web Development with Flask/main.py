from flask import Flask

app = Flask(__name__)
# app.app_context().push()    # for fast updates


@app.route("/")
def index():
    return "hello World dima"


if __name__ == "__main__":
    app.run(debug=True)     # automatic starting app