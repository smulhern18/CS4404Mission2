from flask import Flask, render_template, request

global app
app = Flask(__name__)

def index():
    return render_template('bombast.html')


def create_app():
    app.config["DEBUG"] = True
    app.add_url_rule("/", view_func=index)


if __name__ == "__main__":
    create_app()
    app.run(host="0.0.0.0", port=80, debug=True)


