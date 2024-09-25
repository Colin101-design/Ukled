import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from models import db, Product

app = Flask(__name__)

# Set up file upload configurations
UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db.init_app(app)

with app.app_context():
    db.create_all()

# Home Page
@app.route('/')
def homepage():
    return render_template('index.html')

# About Us Page
@app.route('/about')
def about():
    return render_template('about.html')

# Route to add products
@app.route('/add_products', methods=['GET', 'POST'])
def add_products():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        category = request.form['category']
        led_type = request.form['led_type']
        warranty = request.form['warranty']
        part_l_compliant = 'part_l_compliant' in request.form
        dimensions = request.form['dimensions']
        weight = request.form['weight']
        windage = request.form['windage']
        equivalent_to = request.form['equivalent_to']
        power_consumption = request.form['power_consumption']
        input_voltage = request.form['input_voltage']
        power_factor = request.form['power_factor']
        operating_temperature = request.form['operating_temperature']
        l70_rated_lifetime = request.form['l70_rated_lifetime']
        ingress_protection = request.form['ingress_protection']
        luminous_efficiency = request.form['luminous_efficiency']
        beam_angle = request.form['beam_angle']
        cri = request.form['cri']
        lumen_output = request.form['lumen_output']
        colour_temperature = request.form['colour_temperature']
        emergency_version = 'emergency_version' in request.form
        occupancy_detector = 'occupancy_detector' in request.form
        dimmable_1_10v = 'dimmable_1_10v' in request.form
        dimmable_dali = 'dimmable_dali' in request.form
        
        # Handle the file upload
        if 'picture' not in request.files:
            return 'No file part'
        
        file = request.files['picture']
        
        if file.filename == '':
            return 'No selected file'
        
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        # Create a new product instance
        new_product = Product(
            name=name,
            picture=filename,  # Save the filename in the database
            category=category,
            led_type=led_type,
            warranty=warranty,
            part_l_compliant=part_l_compliant,
            dimensions=dimensions,
            weight=weight,
            windage=windage,
            equivalent_to=equivalent_to,
            power_consumption=power_consumption,
            input_voltage=input_voltage,
            power_factor=power_factor,
            operating_temperature=operating_temperature,
            l70_rated_lifetime=l70_rated_lifetime,
            ingress_protection=ingress_protection,
            luminous_efficiency=luminous_efficiency,
            beam_angle=beam_angle,
            cri=cri,
            lumen_output=lumen_output,
            colour_temperature=colour_temperature,
            emergency_version=emergency_version,
            occupancy_detector=occupancy_detector,
            dimmable_1_10v=dimmable_1_10v,
            dimmable_dali=dimmable_dali
        )

        # Add to the database
        db.session.add(new_product)
        db.session.commit()

        return redirect(url_for('products'))

    return render_template('add_products.html')

# Route to display products
@app.route('/products')
def products():
    products = Product.query.all()
    return render_template('products.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
