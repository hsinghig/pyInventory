from flask import Flask, render_template
from app.blueprints.dashboard.views import dashboard_blueprint
from app.blueprints.home.views import home_blueprint
from app.blueprints.extruder.views import extruder_blueprint
from app.dataLoader import get_table_DUMMY_DATA
from .extensions import db
from .constants import get_formatted_conn
from sqlalchemy.ext.automap import automap_base
import dateutil, datetime

def create_app():
    app = Flask(__name__)
    conn = get_formatted_conn() # 'mssql+pyodbc://'+username+':' + pwd + '@'+ server + '/' + database + '?driver=ODBC+Driver+17+for+SQL+Server'
    print(conn)
    app.config['SECRET_KEY'] = 'SECRET_KEY'
    app.config['SQLALCHEMY_DATABASE_URI'] = conn
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    @app.errorhandler(404)  
    def page_not_found(e):
        return render_template("404.html"), 404
    
    @app.template_filter('strftime')
    def _jinja2_filter_datetime(strDate, fmt=None):
        date = dateutil.parser.parse(strDate)
        native = date.replace(tzinfo=None)
        format='%b %d, %Y %H:%M:%S'
        format2 = '%Y-%m-%d %H:%M:%S'
        return native.strftime(format) 

    @app.route("/table")
    def displayTable():       
        heading, data = get_table_DUMMY_DATA()
        return render_template('table.html', heading=heading, data=data)
    
    @app.route("/")
    def home():
        return render_template('home.html')
    
    app.register_blueprint(dashboard_blueprint, url_prefix='/dashboard')
    app.register_blueprint(home_blueprint, url_prefix='/home' )
    app.register_blueprint(extruder_blueprint, url_prefix='/extruder')
   
    return app


