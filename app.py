from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """Render the home page."""
    return render_template('index.html')

@app.route('/about')
def about():
    """Render the about us page."""
    return render_template('about.html')

@app.route('/products')
def products():
    """Render the products page."""
    return render_template('products.html')

@app.route('/contact')
def contact():
    """Render the contact page."""
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
