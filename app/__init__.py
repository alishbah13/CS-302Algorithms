from flask import Flask

app = Flask(__name__)
# login = LoginManager(app)
# login.login_view = 'login'

from app import routes