#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/12/22 17:31
# @Author :春衫
# @File :GlobalEnvironment.py


class GlobalEnvironment:

    def _init(self):
        global _global_dict
        _global_dict = {}

    def put(self, name, value):
        _global_dict[name] = value

    def get(self, name, defValue=None):
        try:
            return _global_dict[name]
        except KeyError:
            return defValue
