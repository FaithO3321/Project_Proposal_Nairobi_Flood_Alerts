# insert_data.py

from app import app
from models import db, River

with app.app_context():
    db.create_all()

    rivers = [
        River(name='Nairobi River', length_km=60, regions='Ngong Hills, Kibera, Industrial Area, Eastlands',
              estates='Kibera, Dandora, Mukuru kwa Njenga, South B, South C', 
              water_level='Highly variable, prone to flooding during rainy seasons', 
              pollution_content='High levels of industrial and domestic waste, raw sewage', 
              flooding_potential='High risk of flooding in informal settlements along the banks during heavy rains'),
        River(name='Ngong River', length_km=40, regions='Ngong Hills, Karen, Langata', 
              estates='Karen, Langata, Rongai', 
              water_level='Moderate to low, depends on rainfall', 
              pollution_content='Moderate levels of agricultural and domestic waste', 
              flooding_potential='Moderate risk in low-lying areas during heavy rains'),
        River(name='Motoine River', length_km=30, regions='Ngong Hills, Kibra, Dagoretti', 
              estates='Kibera, Dagoretti, Kawangware', 
              water_level='Highly variable, prone to flooding', 
              pollution_content='High levels of domestic and industrial waste', 
              flooding_potential='High risk in informal settlements along the banks'),
        River(name='Mathare River', length_km=25, regions='Mathare Valley, Eastlands', 
              estates='Mathare, Huruma, Kariobangi', 
              water_level='Highly variable, prone to flooding', 
              pollution_content='Very high levels of domestic and industrial waste', 
              flooding_potential='Extreme risk in informal settlements during heavy rains')
    ]

    db.session.add_all(rivers)
    db.session.commit()

