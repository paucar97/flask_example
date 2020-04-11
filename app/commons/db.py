from app.api import app
from flask_sqlalchemy import SQLAlchemy
from io import StringIO


def getSessionServer():
    #"""
    user='root'
    ssh_user = 'inf245'
    passwssh = "6CmINL2eRPo%baH"
    passw= 'GiME4OI9'
    dbName = 'sec2'
    localhost = '127.0.0.1'
    port = 3307
    host = "200.16.7.185"
    #tunnel = sshtunnel.SSHTunnelForwarder(
    #        (host,22),
    #        ssh_password = passwssh,
    #        ssh_username=ssh_user,
    #        remote_bind_address=(localhost, 3306)
    #)
    #tunnel.start()
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(user,passw,localhost,tunnel.local_bind_port,dbName)
    #"""
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/test'
    app.config['SQLALCHEMY_POOL_SIZE'] = 5
    app.config['SQLALCHEMY_POOL_TIMEOUT'] = 30
    app.config['SQLALCHEMY_POOL_RECYCLE'] = 31
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db = SQLAlchemy(app)
    
    return db