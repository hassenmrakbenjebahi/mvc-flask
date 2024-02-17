
from flask import Blueprint
from controllers.user import add_user


user_bp = Blueprint('user_bp', __name__)
user_bp.route('/add', methods=['POST'])(add_user)
