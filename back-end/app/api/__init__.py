# -*- coding: utf-8 -*-
# @Time    : 2019/5/8 16:05
# @Author  : Gumgui
# @File    : __init__.py

from flask import Blueprint
bp = Blueprint('api',__name__)

from app.api import ping

