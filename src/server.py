from flask import Flask, render_template, request

global app
app = Flask(__name__)

def index():
    return render_template('index.html')


def bombast():
    return render_template('bombast.html')


def good_provider():
    return render_template('goodProvider.html')


def create_app():
    app.config["DEBUG"] = True
    app.add_url_rule("/", view_func=index)
    app.add_url_rule("/bombast", view_func=bombast)
    app.add_url_rule("/goodProvider", view_func=good_provider)


if __name__ == "__main__":
    create_app()
    app.run(host="0.0.0.0", port=80, debug=True)


