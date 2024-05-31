from flask import Blueprint, render_template, request, redirect

bp = Blueprint('main', __name__, template_folder='templates', url_prefix='/')

@bp.route('/', methods=['GET'])
@bp.route('/main', methods=['GET'])
def index():

    return render_template('./main/index.html')