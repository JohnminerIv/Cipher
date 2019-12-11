from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/decode')
def decode():
    return render_template('decode.html')

@app.route('/encode')
def encode():
    return render_template('encode.html')

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
