# coding=utf-8

"""
@author: shenke
@project: c3d
@file: __init__.py.py
@date: 2021/4/20
@description: 
"""

import os

print(r'Log directory: %s' % os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'log'))
