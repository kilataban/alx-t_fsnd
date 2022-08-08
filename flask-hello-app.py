from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://kilataban@localhost:5432/kilataban'
db =SQLAlchemy(app)

@app.route('/')
def index():
    return 'Hello World!'

