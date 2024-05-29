# models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class River(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    length_km = db.Column(db.Float, nullable=False)
    regions = db.Column(db.Text, nullable=False)
    estates = db.Column(db.Text, nullable=False)
    water_level = db.Column(db.String(255), nullable=False)
    pollution_content = db.Column(db.Text, nullable=False)
    flooding_potential = db.Column(db.Text, nullable=False)
    last_updated = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

