from . import db

class Spot(db.Model):
    __tablename__ = 'Spots'

    SpotId = db.Column(db.Integer, primary_key=True)
    CategoryId = db.Column(db.Integer)
    SpotTitle = db.Column(db.Text)
    SpotDescription = db.Column(db.Text)
    Address = db.Column(db.Text)
    TrafficInfo = db.Column(db.Text)
    Longitude = db.Column(db.Text)
    Latitude = db.Column(db.Text)
    OpenTime = db.Column(db.Text)
    ContactPhone = db.Column(db.Text)
    DateCreated = db.Column(db.DateTime)
    SpotImage = db.Column(db.Text)
