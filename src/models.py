from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True) 
    email = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    favorites_characters = db.relationship('FavoriteCharacter', backref='user', lazy=True)
    favorites_planets = db.relationship('FavoritePlanet', backref='user', lazy=True)
    favorites_vehicles = db.relationship('FavoriteVehicle', backref='user', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email
        }

class Character(db.Model):
    __tablename__ = 'character'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    favorites_characters = db.relationship('FavoriteCharacter', backref='character', lazy=True)

    def __repr__(self):
        return '<Character %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }

class FavoriteCharacter(db.Model):
    __tablename__ = 'favorite_character'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'))

    def __repr__(self):
        return '<FavoriteCharacter %r>' % self.id

    def serialize(self):
        result = Character.query.filter_by(id=self.character_id).first()
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": result.serialize()["name"]
        }

class Planet(db.Model):
    __tablename__ = 'planet'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    favorites_planets = db.relationship('FavoritePlanet', backref='planet', lazy=True)

    def __repr__(self):
        return '<Planet %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }

class FavoritePlanet(db.Model):
    __tablename__ = 'favorite_planet'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))

    def __repr__(self):
        return '<FavoritePlanet %r>' % self.id

    def serialize(self):
        result = Planet.query.filter_by(id=self.planet_id).first()
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": result.serialize()["name"]
        }

class Vehicle(db.Model):
    __tablename__ = 'vehicle'
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    favorites_vehicles = db.relationship('FavoriteVehicle', backref='vehicle', lazy=True)

    def __repr__(self):
        return '<Vehicle %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }

class FavoriteVehicle(db.Model):
    __tablename__ = 'favorite_vehicle'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'))

    def __repr__(self):
        return '<FavoriteVehicle %r>' % self.id

    def serialize(self):
        result = Vehicle.query.filter_by(id=self.vehicle_id).first()
        return {
            "id": self.id,
            "user_id": self.user_id,
            "vehicle_id": result.serialize()["name"]
        }

