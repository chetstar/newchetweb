import os
from flask import Flask, render_template, send_from_directory
from flask_bootstrap import Bootstrap
# from flask.ext.sqlalchemy import SQLAlchemy

# initialization
app = Flask(__name__)
app.config.update(
    DEBUG = True,
)
Bootstrap(app)


from views import *

# launch
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)