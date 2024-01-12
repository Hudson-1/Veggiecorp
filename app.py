from flask import Flask, render_template

app = Flask(__name__)

#
# @app.route('/')
# def hello_world():
#     return """
#     <h1>Hello World!</h1>
#     <br />
#     Try these links: <br />
#     - <a href='/pets'>pets</a><br />
#      - <a href='/home'>home</a><br />
#      - <a href='/bootstrap'>bootstrap</a><br />
#     """


# Rendering a html template
@app.route('/')
def home():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/products')
def products():
    return render_template("products.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)