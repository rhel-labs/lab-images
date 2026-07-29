from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>rhhi-demo v1</h1><p>Flask on Red Hat Hardened Python 3.12</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
