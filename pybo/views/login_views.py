from flask import Blueprint, render_template, redirect,  url_for, request

bp = Blueprint('login', __name__, url_prefix='/login')

# @bp.route('/', methods=['GET', 'POST'])
# def login():


#     return render_template('./login/login.html')


# @bp.route('/sign_up', methods=['POST'])
# def signup():

#     return render_template('./login/sign_up.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Perform login logic
        return redirect(url_for('main.index'))  # 엔드포인트 이름을 정확하게 지정
    return render_template('login/login.html')


@bp.route('/sign_up', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Perform sign up logic
        return redirect(url_for('login.login'))  # 엔드포인트 이름을 정확하게 지정
    return render_template('login/sign_up.html')