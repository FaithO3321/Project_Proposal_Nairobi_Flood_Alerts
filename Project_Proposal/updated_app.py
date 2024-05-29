# app.py

from flask import Flask, render_template, request, redirect, url_for
from config import Config
from models import db, River, Region

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    rivers = River.query.all()
    return render_template('index.html', rivers=rivers)

@app.route('/regions')
def regions():
    regions = Region.query.all()
    return render_template('regions.html', regions=regions)

@app.route('/update', methods=['POST'])
def update():
    if request.method == 'POST':
        river_id = request.form['id']
        water_level = request.form['water_level']
        river = River.query.get(river_id)
        river.water_level = water_level
        db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

