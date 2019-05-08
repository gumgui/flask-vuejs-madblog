# -*- coding: utf-8 -*-
# @Time    : 2019/5/8 16:06
# @Author  : Gumgui
# @File    : ping.py


from flask import jsonify
from app.api import bp
@bp.route('/ping',methods=['GET'])
def ping():
	return jsonify("Pong!")