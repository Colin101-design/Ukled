from flask import Flask, render_template

app = Flask(__name__)

# Homepage route
@app.route('/')
def homepage():
    return render_template('index.html')

# About page route
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
