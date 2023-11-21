from flask import Flask

from database.init import init

from base.home import home 

app = Flask(__name__)
database = init()


if __name__ == '__main__':
    
    app.run()