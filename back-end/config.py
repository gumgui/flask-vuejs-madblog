# -*- coding: utf-8 -*-
# @Time    : 2019/5/8 16:08
# @Author  : Gumgui
# @File    : config.py
import os
from dotenv import load_dotenv
base_dir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(base_dir,'.env'))

class Config(object):
	pass