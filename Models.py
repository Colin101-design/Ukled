from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    picture = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    led_type = db.Column(db.String(50), nullable=False)
    warranty = db.Column(db.String(50), nullable=False)
    part_l_compliant = db.Column(db.Boolean, nullable=False)
    dimensions = db.Column(db.String(50), nullable=False)
    weight = db.Column(db.Float, nullable=False)
    windage = db.Column(db.Float, nullable=False)
    equivalent_to = db.Column(db.String(100), nullable=False)
    power_consumption = db.Column(db.Float, nullable=False)
    input_voltage = db.Column(db.String(50), nullable=False)
    power_factor = db.Column(db.Float, nullable=False)
    operating_temperature = db.Column(db.String(50), nullable=False)
    l70_rated_lifetime = db.Column(db.String(50), nullable=False)
    ingress_protection = db.Column(db.String(50), nullable=False)
    luminous_efficiency = db.Column(db.Float, nullable=False)
    beam_angle = db.Column(db.String(50), nullable=False)
    cri = db.Column(db.Float, nullable=False)
    lumen_output = db.Column(db.Float, nullable=False)
    colour_temperature = db.Column(db.String(50), nullable=False)
    emergency_version = db.Column(db.Boolean, nullable=False)
    occupancy_detector = db.Column(db.Boolean, nullable=False)
    dimmable_1_10v = db.Column(db.Boolean, nullable=False)
    dimmable_dali = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f'<Product {self.name}>'
