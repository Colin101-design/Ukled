from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    picture = db.Column(db.String(200), nullable=True)  # Picture is optional
    category = db.Column(db.String(50), nullable=True)  # Optional
    led_type = db.Column(db.String(50), nullable=True)  # Optional
    warranty = db.Column(db.String(50), nullable=True)  # Optional
    part_l_compliant = db.Column(db.Boolean, nullable=True)  # Optional
    dimensions = db.Column(db.String(100), nullable=True)  # Optional
    weight = db.Column(db.Float, nullable=True)  # Optional
    windage = db.Column(db.Float, nullable=True)  # Optional
    equivalent_to = db.Column(db.String(50), nullable=True)  # Optional
    power_consumption = db.Column(db.Integer, nullable=True)  # Optional
    input_voltage = db.Column(db.String(50), nullable=True)  # Optional
    power_factor = db.Column(db.Float, nullable=True)  # Optional
    operating_temperature = db.Column(db.String(50), nullable=True)  # Optional
    l70_rated_lifetime = db.Column(db.String(50), nullable=True)  # Optional
    ingress_protection = db.Column(db.String(50), nullable=True)  # Optional
    luminous_efficiency = db.Column(db.Float, nullable=True)  # Optional
    beam_angle = db.Column(db.String(50), nullable=True)  # Optional
    cri = db.Column(db.Integer, nullable=True)  # Optional
    lumen_output = db.Column(db.Integer, nullable=True)  # Optional
    colour_temperature = db.Column(db.String(50), nullable=True)  # Optional
    emergency_version = db.Column(db.Boolean, nullable=True)  # Optional
    occupancy_detector = db.Column(db.Boolean, nullable=True)  # Optional
    dimmable_1_10v = db.Column(db.Boolean, nullable=True)  # Optional
    dimmable_dali = db.Column(db.Boolean, nullable=True)  # Optional
