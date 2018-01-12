from flask import Flask, render_template, json, request
from werkzeug import generate_password_hash, check_password_hash

app = Flask(__name__)

# MySQL configurations


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5002)
