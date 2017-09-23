from clarifai import rest
from clarifai.rest import ClarifaiApp
app=ClarifaiApp("pgTSm-cRKH1MaPxO4Q_UBAXbk1nnOIoAaEiFniII", "xVwObZXwITHHX34Dwp8n3sLBq9eklHisK1zDle93")
model = app.models.get("general-v1.3")
model.predict_by_url(url='https://samples.clarifai.com/metro-north.jpg')