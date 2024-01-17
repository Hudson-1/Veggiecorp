from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)


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


@app.route('/confirmation')
def confirmation():
    name = request.args.get('name')
    address = request.args.get('adr')
    email = request.args.get('email')
    phone = request.args.get('phone')

    # Create a DataFrame
    data = {
        'Name': [name],
        'Address': [address],
        'Email': [email],
        'Phone': [phone]
    }

    df = pd.DataFrame(data)

    df.to_csv('user_data.csv', index=False)

    props = {
        "name": name,
        "email": email,
        "address": address,
        "phone": phone
    }

    return render_template("confirmation.html", data=props)

if __name__ == '__main__':
    app.run(debug=True)