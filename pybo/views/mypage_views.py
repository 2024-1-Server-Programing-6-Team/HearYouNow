from flask import Blueprint, render_template, request, redirect

bp = Blueprint('mypage_views', __name__, url_prefix='/mypage')

@bp.route('/mypage')
def mypage():

    return render_template('mypage/my-page.html')
