from . import db

class SpotsCategory(db.Model):
    __tablename__ = 'SpotsCategories'

    CategoryId = db.Column(db.Integer, primary_key=True)
    CategoryName = db.Column(db.Text)
