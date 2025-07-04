from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from pytz import timezone
import pytz
Kabelo

app = Flask(__name__)
login = LoginManager(app)
login.login_view = 'login'
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app,db)
@app.template_filter('localtime')
def localtime_filter(utc_dt):
    if utc_dt is None:
        return "Never"
    sa_tz = timezone('Africa/Johannesburg')
    if utc_dt.tzinfo is None:
        utc_dt = pytz.utc.localize(utc_dt)
    return utc_dt.astimezone(sa_tz).strftime('%Y-%m-%d %H:%M:%S')




from app import routes, models


