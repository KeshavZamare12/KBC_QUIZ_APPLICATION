# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 08:58:55 2023

@author: Admin
"""
import cx_Oracle
class db:
    def conn_db(self,name,email,college,mobile_no):
        self.money=0
        self.name,self.email,self.college,self.mobile_no=name,email,college,mobile_no
        self.con=cx_Oracle.connect("system/manager@192.168.43.212/xepdb1")
        self.cur=self.con.cursor()
        self.qry="insert into student values('%s','%s','%s',%d,%d)"
        self.cur.execute(self.qry %(self.name,self.email,self.college,self.mobile_no,self.money))
        self.con.commit()
    def update_money(self,money):
        self.qry="update student set money=%d where name='%s'"%(money,self.name)
        self.cur.execute(self.qry)
        self.con.commit()
