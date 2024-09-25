from flask import Flask, render_template, request, redirect, url_for
from models import db, Product

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

# Homepage Route
@app.route('/')
def homepage():
    return render_template('index.html')

# About Us Route
@app.route('/about')
def about():
    return render_template('about.html')

# Route to display form for adding new products
@app.route('/add_products', methods=['GET', 'POST'])
def add_products():
    if request.method == 'POST':
        # Extract form data
        name = request.form['name']
        picture = request.form['picture']
        category = request.form['category']
        led_type = request.form['led_type']
        warranty = request.form['warranty']
        # Add other fields similarly...

        # Create new product object
        new_product = Product(name=name, picture=picture, category=category, led_type=led_type, warranty=warranty)
        # Add the product to the database
        db.session.add(new_product)
        db.session.commit()

        return redirect(url_for('products'))

    return render_template('add_products.html')

# Route to display products
@app.route('/products')
def products():
    all_products = Product.query.all()
    return render_template('products.html', products=all_products)

if __name__ == '__main__':
    app.run(debug=True)
