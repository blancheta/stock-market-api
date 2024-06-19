from app.order import bp


@bp.route('/')
def index():
    return 'This is The Main Blueprint'
