from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask, redirect, url_for
#from flask_login import LoginManager
#from flask_bcrypt import Bcrypt


# For database
db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')  # Start app with Flask
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./blueprints.sqlite'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./test.db'
    app.secret_key = 'busrabusrabusra'  # Keep the information

    #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./sqlite.db'  # Veritabanı URI'sini ayarlayın
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    from blueprintapp.blueprints.core.routes import core
    from blueprintapp.blueprints.people.routes import people
    from blueprintapp.blueprints.todos.routes import todos



    app.register_blueprint(core, url_prefix='/')
    app.register_blueprint(todos, url_prefix='/todos')
    app.register_blueprint(people, url_prefix='/people')

    migrate = Migrate(app, db)

    #login_manager = LoginManager()
    #login_manager.init_app(app)

    #@login_manager.unauthorized_handler
    #def unauthorized_callback():
    #    return redirect(url_for('index'))

    #bcrypt = Bcrypt(app)


    return app

