#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/5/22 14:40
# @Author :春衫
# @File :learn_sql.py

import pymysql
from tools.project_path import db_config_path
from tools.read_config import ReadConfig


class DoMysql:

    def __init__(self, cursors_type="dict"):
        # db_config = eval(ReadConfig().read_config(case_config_path,'DB','db_config'))
        db_config = ReadConfig().read_config(db_config_path)
        # 创建一个数据库连接  **关键字参数
        self.cnn = pymysql.connect(**db_config)
        # 游标cursor
        if cursors_type == "dict":
            self.cursor = self.cnn.cursor(cursor=pymysql.cursors.DictCursor)
        else:
            self.cursor = self.cnn.cursor(cursor=pymysql.cursors.Cursor)

    # 增删改
    def insert_delete_updata(self, sql):
        """

        Parameters
        ----------
        sql：SQL语句

        Returns
        -------

        """
        try:
            # 拼接并执行sql语句
            self.cursor.execute(sql)
            # 涉及写操作要注意提交
            self.cnn.commit()
            print("数据库操作执行成功")
        except Exception as e:
            print("数据库操作异常，异常原因是：", e)
            # 有异常，回滚事务
            self.cnn.rollback()
        finally:
            # 关闭游标
            self.cursor.close()
            # 关闭连接
            self.cnn.close()

    def query_all(self, sql):
        """

        Parameters：查询所有的结果集
        ----------
        sql：SQL语句

        Returns：所有的查询结果 list[dict,dict]
        -------

        """
        try:
            # 执行语句
            self.cursor.execute(sql)
            # 获取结果
            res = self.cursor.fetchall()
            return res
        except Exception as e:
            print("数据库查询异常，异常原因是：", e)
            raise e
        finally:
            # 关闭游标
            self.cursor.close()
            # 关闭连接
            self.cnn.close()

    def query_one(self, sql):
        """

        Parameters：查询结果集中的第一条数据
        ----------
        sql：要执行的sql语句

        Returns：查询结果集中的第一条数据 dict
        -------

        """

        try:
            # 执行语句
            self.cursor.execute(sql)
            # 获取结果
            res = self.cursor.fetchone()
            return res
        except Exception as e:
            print("数据库查询异常，异常原因是：", e)
            raise e
        finally:
            # 关闭游标
            self.cursor.close()
            # 关闭连接
            self.cnn.close()

    def query_one_value(self, sql):
        """

        Parameters：查询结果集中的第一条数据
        ----------
        sql：要执行的sql语句

        Returns：查询结果集中的第一条数据 dict
        -------

        """

        try:
            # 执行语句
            self.cursor.execute(sql)
            # 获取结果
            res = self.cursor.fetchone()
            return res[0]
        except Exception as e:
            print("数据库查询异常，异常原因是：", e)
            raise e
        finally:
            # 关闭游标
            self.cursor.close()
            # 关闭连接
            self.cnn.close()


if __name__ == '__main__':
    SQL = 'select count(*) from member where mobile_phone=13133172226;'
    res = DoMysql("tuple").query_one_value(SQL)
    print(res)
