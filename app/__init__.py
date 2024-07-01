from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase

from app.order.models import db
from config import Config



def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    # Initialize Flask extensions here
    with app.app_context():
        db.create_all()

        # new_user = User(username="aaaa")
        # print(new_user)
        # db.session.add(new_user)
        # db.session.commit()

    # Register blueprints here
    from app.order import bp as main_bp
    app.register_blueprint(main_bp)

    @app.route('/health')
    def health():
        return {
            "status": "ok"}

    return app