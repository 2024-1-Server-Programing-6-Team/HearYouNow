from flask import Blueprint, render_template, redirect

bp = Blueprint('login', __name__, url_prefix='/login')

@bp.route('/', methods=['GET', 'POST'])
def login():


    return render_template('login/login.html')


@bp.route('/sign_up', methods=['POST'])
def signup():

    return render_template('login/sign_up.html')
