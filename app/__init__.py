import os
from flask import Flask, render_template, send_from_directory
from flask_bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.mail import Mail

# initialization
app = Flask(__name__)

app.config.update(
    DEBUG = True,
)
app.config.from_object('config')
#now i can access config vars via app.config['VAR_Name']
Bootstrap(app)
db = SQLAlchemy(app)
mail = Mail(app)


from views import *
from models import *

# launch
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
