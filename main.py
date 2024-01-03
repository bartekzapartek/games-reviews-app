from flask import Flask

from database.init import init
from base.views import base
from userAuthentication.views import authentication

app = Flask(__name__)

app.secret_key = "secretkey"

app.register_blueprint(base, template_folder = 'templates')
app.register_blueprint(authentication, template_folder = 'templates')


if __name__ == '__main__':
    init()

    app.run(debug = True)