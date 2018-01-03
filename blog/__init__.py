import os

from flask import Flask

app = Flask(__name__)
config_path = os.environ.get('CONFIG_PATH', 'blog.config.DevelopmentConfig')
#above foldername.filename.objectname
app.config.from_object(config_path)
#configure the app from the object specified

from . import views
from . import filters