#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/4/19 19:03
# @Author :春衫
# @File :UserLog.py

import datetime
import logging
import os

from tools.project_path import log_path
from tools.project_path import logs_config_path
from tools.read_yaml import read_yaml


class UserLog:

    def user_log(self, msg, level, interface, case_id):

        config = read_yaml(logs_config_path)
        # 收集
        logger_collect_level = config['logger_collect_level']
        # 打印
        logger_print_level = config['logger_print_level']
        # 输出
        logger_output_level = config['logger_output_level']

        # 定义一个日志收集器my_logger
        my_logger = logging.getLogger('春衫')

        # 设置级别 全收集
        my_logger.setLevel(logger_collect_level)

        # 设置输出格式
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(name)s - 日志信息:%(message)s')

        # 创建一个输出渠道 打印级别
        ch = logging.StreamHandler()
        ch.setLevel(logger_print_level)
        ch.setFormatter(formatter)

        # 日志文件名格式
        folder_path = log_path + "\\" + interface
        # 创建文件夹
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        log_file_name = interface + "_" + str(case_id) + ".log"
        file_path = folder_path + "\\" + log_file_name

        #创建文件
        if not os.path.exists(file_path):
            os.system(file_path)

        # 创建日志文件 写入级别
        fh = logging.FileHandler(file_path, encoding='utf-8')
        fh.setLevel(logger_output_level)
        fh.setFormatter(formatter)

        # 收集输出对接
        my_logger.addHandler(ch)
        my_logger.addHandler(fh)

        # 收集日志
        if level == 'DEBUG':
            my_logger.debug(msg)

        elif level == 'INFO':
            my_logger.info(msg)

        elif level == 'WARNING':
            my_logger.warning(msg)

        elif level == 'ERROR':
            my_logger.error(msg)

        elif level == 'CRITICAL':
            my_logger.critical(msg)

        # 关闭日志收集器(渠道)
        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)

    def debug(self, msg, interface, case_id):
        self.user_log(msg, 'DEBUG', interface, case_id)

    def info(self, msg, interface, case_id):
        self.user_log(msg, 'INFO', interface, case_id)

    def warning(self, msg, interface, case_id):
        self.user_log(msg, 'WARNING', interface, case_id)

    def error(self, msg, interface, case_id):
        self.user_log(msg, 'ERROR', interface, case_id)

    def critical(self, msg, interface, case_id):
        self.user_log(msg, 'CRITICAL', interface, case_id)


if __name__ == '__main__':
    my_logger = UserLog()
    my_logger.debug("测试", 'login', 1)
    # my_logger.info('测试')
    # UserLog().user_log('测试一下1', 'ERROR')
    # UserLog().user_log('测试一下2', 'ERROR')
