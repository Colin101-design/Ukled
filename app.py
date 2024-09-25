import os
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from models import db, Product

app = Flask(__name__)

# Set up file upload configurations
UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'supersecretkey'

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
        try:
            # Get form data, some fields can be left empty (handled as optional)
            name = request.form.get('name')
            category = request.form.get('category', None)
            led_type = request.form.get('led_type', None)
            warranty = request.form.get('warranty', None)
            part_l_compliant = request.form.get('part_l_compliant') == 'on'
            dimensions = request.form.get('dimensions', None)
            weight = request.form.get('weight', None)
            windage = request.form.get('windage', None)
            equivalent_to = request.form.get('equivalent_to', None)
            power_consumption = request.form.get('power_consumption', None)
            input_voltage = request.form.get('input_voltage', None)
            power_factor = request.form.get('power_factor', None)
            operating_temperature = request.form.get('operating_temperature', None)
            l70_rated_lifetime = request.form.get('l70_rated_lifetime', None)
            ingress_protection = request.form.get('ingress_protection', None)
            luminous_efficiency = request.form.get('luminous_efficiency', None)
            beam_angle = request.form.get('beam_angle', None)
            cri = request.form.get('cri', None)
            lumen_output = request.form.get('lumen_output', None)
            colour_temperature = request.form.get('colour_temperature', None)
            emergency_version = request.form.get('emergency_version') == 'on'
            occupancy_detector = request.form.get('occupancy_detector') == 'on'
            dimmable_1_10v = request.form.get('dimmable_1_10v') == 'on'
            dimmable_dali = request.form.get('dimmable_dali') == 'on'

            # Handle the file upload for the picture
            file = request.files.get('picture', None)
            if file and file.filename != '':
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            else:
                filename = None  # No file was uploaded

            # Create a new product instance with optional fields
            new_product = Product(
                name=name,
                picture=filename,
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

            flash('Product added successfully!', 'success')
            return redirect(url_for('products'))
        
        except Exception as e:
            # Log the error and flash an error message
            print(f"Error adding product: {e}")
            flash('There was an error adding the product. Please try again.', 'danger')

    return render_template('add_products.html')

# Route to display products
@app.route('/products')
def products():
    products = Product.query.all()
    return render_template('products.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
