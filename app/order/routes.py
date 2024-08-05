from app.order import bp
from app.order.models import User


@bp.route('/')
def index():
    return 'This is The Main Blueprint'


@bp.route('/users')
def index():
    users = User.query.all()

    response_json = [
        {
            "name": user.name
        } for user in users
    ]
    return response_json

