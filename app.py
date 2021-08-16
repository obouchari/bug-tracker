from flask import Flask, render_template
from flask_assets import Environment, Bundle

app = Flask(__name__)

assets = Environment(app)
css = Bundle('src/css/*.css', filters='postcss', output='dist/css/app.css')
assets.register('app_css', css)
css.build()


@app.get('/')
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
