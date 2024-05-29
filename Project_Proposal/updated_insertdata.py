# insert_data.py

from app import app
from models import db, River, Region

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

    regions = [
        Region(ward_name='Mukuru Kwa Njenga Ward', constituency='Embakasi South Constituency', estates='Mukuru Kwa Njenga slums, Sinai, Viwandani'),
        Region(ward_name='Laini Saba', constituency='Kibra Constituency', estates='Kibera slums (especially Gatwekera, Kianda, and Laini Saba villages), Lindi, Mashimoni'),
        Region(ward_name='Lindi', constituency='Kibra Constituency', estates='Kibera slums (especially Gatwekera, Kianda, and Laini Saba villages), Lindi, Mashimoni'),
        Region(ward_name='Makina', constituency='Kibra Constituency', estates='Kibera slums (especially Gatwekera, Kianda, and Laini Saba villages), Lindi, Mashimoni'),
        Region(ward_name='Mutu-ini', constituency='Dagoretti South Constituency', estates='Kawangware, Riruta Satelite'),
        Region(ward_name='Riruta', constituency='Dagoretti South Constituency', estates='Kawangware, Riruta Satelite'),
        Region(ward_name='Kariobangi North', constituency='Embakasi North Constituency', estates='Kariobangi North, Kariobangi South, Korogocho slums'),
        Region(ward_name='Kariobangi South', constituency='Embakasi North Constituency', estates='Kariobangi North, Kariobangi South, Korogocho slums'),
        Region(ward_name='Mabatini', constituency='Mathare Constituency', estates='Mathare slums (especially Mathare North and Mathare 4A)'),
        Region(ward_name='Hospital', constituency='Mathare Constituency', estates='Mathare slums (especially Mathare North and Mathare 4A)'),
        Region(ward_name='Parklands/Highridge', constituency='Westlands Constituency', estates='Parts of Westlands, Parklands'),
        Region(ward_name='Eastleigh North', constituency='Kamukunji Constituency', estates='Parts of Eastleigh'),
        Region(ward_name='Eastleigh South', constituency='Kamukunji Constituency', estates='Parts of Eastleigh'),
        Region(ward_name='Nairobi West', constituency='Langata Constituency', estates='Parts of South C and Nyayo Highrise')
    ]

    db.session.add_all(rivers)
    db.session.add_all(regions)
    db.session.commit()

