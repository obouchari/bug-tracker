from flask import Flask

app = Flask(__name__)


@app.get('/')
def home():
    return 'Welcome to full-stack flask!'


if __name__ == "__main__":
    app.run()
