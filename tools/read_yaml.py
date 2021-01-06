#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/9/10 13:55
# @Author :春衫
# @File :read_yaml.py

import yaml

def read_yaml(file_path):
    fs = open(file_path, encoding="utf-8")
    data = yaml.load(fs,Loader=yaml.FullLoader)
    return  data

if __name__ == '__main__':
    pass