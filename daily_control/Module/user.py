#coding=utf-8
class User(object):
    def __init__(self,uid,sno,pwd):
        self.sno = sno
        self.uid = uid
        self.pwd = pwd
    
    def save(self,mydb,sql):
        res = sql.insert(mydb,'user',uid=self.uid,sno=self.sno,pwd=self.pwd)
        return res[0]
        