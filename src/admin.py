import os
from flask_admin import Admin
from models import db, User, Planet, Character, Vehicle, FavoritePlanet, FavoriteCharacter, FavoriteVehicle
from flask_admin.contrib.sqla import ModelView

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')

    class FavoriteCharacterView(ModelView):
        column_list=('character_id', 'user_id')
        form_columns=('character_id', 'user_id')
    class FavoritePlanetView(ModelView):
        column_list=('planet_id', 'user_id')
        form_columns=('planet_id', 'user_id')
    class FavoriteVehicleView(ModelView):
        column_list=('vehicle_id', 'user_id')
        form_columns=('vehicle_id', 'user_id')

    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Character, db.session))
    admin.add_view(ModelView(Planet, db.session))
    admin.add_view(ModelView(Vehicle, db.session))
    admin.add_view(FavoriteCharacterView(FavoriteCharacter, db.session))
    admin.add_view(FavoritePlanetView(FavoritePlanet, db.session))
    admin.add_view(FavoriteVehicleView(FavoriteVehicle, db.session))