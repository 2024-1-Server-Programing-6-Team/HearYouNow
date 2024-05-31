from flask import Blueprint, render_template, request

bp = Blueprint('posting', __name__, url_prefix='/posting')

@bp.route('/new', methods=['GET, POST'])
def new_posting():

    return render_template('./posting/write-post.html')


@bp.route('/post', methods=['POST'])
def get_posting():

    return render_template('./posting/view-post.html')
