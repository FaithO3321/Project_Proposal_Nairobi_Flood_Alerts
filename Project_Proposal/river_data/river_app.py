# app.py

from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM rivers")
    river_data = cur.fetchall()
    cur.close()
    return render_template('index.html', rivers=river_data)

@app.route('/update', methods=['POST'])
def update():
    if request.method == 'POST':
        river_id = request.form['id']
        water_level = request.form['water_level']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE rivers
            SET water_level = %s
            WHERE id = %s
        """, (water_level, river_id))
        mysql.connection.commit()
        cur.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

