#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/4/10 22:24
# @Author :春衫
# @File :read_config.py

import yaml


class ReadConfig:

    def read_config(self, caps_dir):
        fs = open(caps_dir, encoding="utf-8")
        datas = yaml.load(fs, Loader=yaml.FullLoader)
        return datas


if __name__ == '__main__':
    from tools.project_path import *

    res = ReadConfig().read_config(case_config_path)
    print(type(res))
    print(res)
