from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = '89876eade3c65e5087860989a134d9bd'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app) #Cria um banco de dados usando a classe sqlalchemy, usando as config do flask
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Faça o Login para continuar'
login_manager.login_message_category = 'alert-warning'

#Executando o arquivo routes
from comunidadeimpressionadora import routes
