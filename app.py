from flask import Flask, render_template
from models import db, Product  # Import db and Product from models.py

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Create database tables
with app.app_context():
    db.create_all()

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/add_products')
def add_products():
    product1 = Product(
        name='Product 1',
        picture='url_to_picture_1',  # Replace with the actual URL or path to your image
        category='Category 1',
        led_type='SMD3030',
        warranty='5 Year',
        part_l_compliant=True,
        dimensions='Ø458 x 659mm',
        weight=6.7,
        windage=0.15,
        equivalent_to='70 SON / MHL',
        power_consumption=30,
        input_voltage='100-280V AC',
        power_factor=0.95,
        operating_temperature='-20°C to 65°C',
        l70_rated_lifetime='+55,000hrs',
        ingress_protection='IP65',
        luminous_efficiency=125,
        beam_angle='150° x 150°',
        cri=80,
        lumen_output=3750,
        colour_temperature='3000K',
        emergency_version=False,
        occupancy_detector=False,
        dimmable_1_10v=False,
        dimmable_dali=False
    )
    
    db.session.add(product1)
    db.session.commit()
    return 'Product added!'

@app.route('/products')
def products():
    products = Product.query.all()
    return render_template('products.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
