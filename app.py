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

# Ensure the upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Initialize the database
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        # Handle file upload
        picture = None
        if 'picture' in request.files:
            file = request.files['picture']
            if file.filename != '':
                filename = secure_filename(file.filename)
                picture = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(picture)
        
        # Handle form fields, using default values (None or empty strings) for optional fields
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
        
        # Create a new product
        new_product = Product(
            name=name,
            picture=picture,
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
        
        try:
            db.session.add(new_product)
            db.session.commit()
            flash('Product added successfully!', 'success')
            return redirect(url_for('add_product'))
        except Exception as e:
            db.session.rollback()
            flash(f"Error adding product: {e}", 'danger')
    
    return render_template('add_product.html')

@app.route('/products')
def products():
    products = Product.query.all()
    return render_template('products.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
