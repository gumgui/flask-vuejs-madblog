# -*- coding: utf-8 -*-
# @Time    : 2019/5/8 16:01
# @Author  : Gumgui
# @File    : __init__.py

from flask import Flask
from config import Config

def create_app(config_class=Config):
	app = Flask(__name__)
	app.config.from_object(config_class)

	#register blueprint

	from app.api import bp as api_bp
	app.register_blueprint(api_bp,url_prefix='/api')
	return app

