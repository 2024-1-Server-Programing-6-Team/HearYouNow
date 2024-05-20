from flask import Flask


def create_app():

    app = Flask(__name__)

    from views import main_views, login_views, mypage_views, post_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(login_views.bp)
    app.register_blueprint(mypage_views.bp)
    app.register_blueprint(post_views.bp)

    return app



