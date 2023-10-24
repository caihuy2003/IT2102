from flask import Flask, render_template
import data

app = Flask(__name__)


@app.route('/')
def hello():
    products = data.products()
    return render_template('index.html', data=products)


if __name__ == ("__main__"):
    app.run(debug=True)
