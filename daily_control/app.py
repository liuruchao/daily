#coding=utf-8

from flask import Flask,request,Response,jsonify
from flask_cors import CORS
from flask_compress import Compress
import mysql.connector
from Module import sql 
from Module import user
import hashlib
import time, uuid
import os

app = Flask(__name__)
Compress(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})   # 解决跨域




def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)

#连接数据库
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="daily"
)

#初始化前台首页数据
@app.route('/init',methods=['POST','GET'])
def home():
    if request.method == 'POST':
        v1 = sql.select(mydb,'article',"where classes='长院要闻'","count(1)")
        v2 = sql.select(mydb,'article',"where classes='综合新闻'","count(1)")
        v3 = sql.select(mydb,'article',"where isReport='true'","count(1)")
        v4 = sql.select(mydb,'article',"where classes='公告通知'","count(1)")
        artHot = sql.select(mydb,'article',"ORDER BY likes desc limit 6","id,title,likes")
        artNew = sql.select(mydb,'article',"where isReport='false' ORDER By time desc limit 6","id,title,subhead,imgUrl,time")
        #传到前端数据
        datas = (v1[0],v2[0],v3[0],v4[0],artHot,artNew)     
        return jsonify(datas)


# 分类响应，前台展示三类文章
@app.route('/article',methods=['POST'])
def article():
    if request.method == 'POST':
        # 文章类别
        classes = request.form['classes']      
        where = "where classes='" + classes + "'"
        count = sql.select(mydb,'article',where,'count(1)')
        artNew = sql.select(mydb,'article',where + ' ORDER By time desc limit 6')
        datas = (count[0],artNew)
        return jsonify(datas)     
    else:
        return 'false'

# 前台文章页分页系统
@app.route('/select',methods=['POST','GET'])
def select():
    classes = request.form['classes']
    pages = request.form['pages']
    pages = (int(pages) - 1)*6
    where = "where classes='" + classes + "'"
    artNew = sql.select(mydb,'article',where + ' ORDER By time desc limit ' + str(pages) + ',6')
    return jsonify(artNew)
    
# 前台期刊导读
@app.route('/period/<status>',methods=['POST'])
def perios(status):
    if request.method == 'POST':
        if status == 'init':
            return jsonify(sql.select(mydb,'journal','where 1','id,qikan,qikanshu'))
        elif status == 'selectAll':
            qikan = request.form['qikan']
            qikanshu = request.form['qikanshu']
            where = "where qikan='" +qikan + "' and " + "qikanshu='" + qikanshu +"'"
            return jsonify(sql.select(mydb,'journal',where,'id,title'))
        elif status == 'selectPost':
            id = request.form['id']
            where = 'where id=' + id
            return jsonify(sql.select(mydb,'journal',where,'title,author,keyword,digest'))

# 注册
@app.route('/login',methods=['POST'])
def login(us=user):
    if request.method == 'POST':
        if not request.form['sno']:
            raise Exception('sno', 'Invalid sno')
        if not request.form['pwd']:
            raise Exception('pwd', 'Invalid pwd') 
        # return jsonify(request.form['sno'],request.form['pwd'])   
        uid = next_id()
        pwd = request.form['pwd']
        sno = request.form['sno']
        # 查找是否已注册
        where = "where sno=" + sno
        res = sql.select(mydb,'user',where)
        if len(res) > 0 :
            return 'hasLogin'  #已注册    
        sha1_pwd = '%s:%s' % (uid,pwd)
        # 摘要算法防篡改
        sha1 = hashlib.sha1()
        sha1.update(sha1_pwd.encode('utf-8'))
        sha1_pwd = sha1.hexdigest()
        user = us.User(uid,sno,sha1_pwd)
        if user.save(mydb,sql) == 1:
            return 'loginSuccess'   #注册成功
        else:
            return 'loginFails'

# 登陆
@app.route('/landing',methods=['POST'])
def landing():
    if request.method == 'POST':
        sno = request.form['sno']
        pwd = request.form['pwd']
        #是否注册
        where = "where sno=" + sno  
        res = sql.select(mydb,'user',where)
        if len(res) <= 0 :
            return 'noLogin'  #未注册
        uid = res[0]['uid']
        user_pwd = res[0]['pwd'] #数据库中的sha摘要
        sha1 = hashlib.sha1()
        sha1.update(uid.encode('utf-8'))
        sha1.update(b':')
        sha1.update(pwd.encode('utf-8'))
        sha1_pwd = sha1.hexdigest()
        # sha1_pwd   根据登录时传过来的账号、密码，重新计算的sha摘要
        if sha1_pwd != user_pwd:
            return 'landingFails'
        else:
            return jsonify(('landingSuccess',uid))
    
# 后台发布文章
@app.route('/issue',methods=['POST'])
def issue():
    if request.method == 'POST':
        form = request.get_json()    #前端传过来的json数据 
        classes = form['classes'][0].strip()
        title = form['title'].strip()
        subhead = form['subhead'].strip()
        content = form['content']
        imgUrl = form['croImgBase64']
        res = sql.insert(mydb,'article',classes=classes,title=title,subhead=subhead,content=content,imgUrl=imgUrl)
        if res[0] == 1:
            return 'issueSuccess'
        else:
            return 'issueFails'

# 后台文章列表展示
@app.route('/articleShow/<status>',methods=['POST'])
def articleShow(status):
    if request.method == 'POST':
        data = request.get_json()
        if status == 'init':
            return jsonify(sql.select(mydb,'article','where 1'))
        elif status == 'delete':
            where = 'id=' + str(data['id'])
            res = sql.delete(mydb,'article',where)
            if res == 1:
                return 'deletSuccess'

# 后台热门文章
@app.route('/topAritcle',methods=['POST'])
def topAritcle():
    if request.method == 'POST':
        return jsonify(sql.select(mydb,'article',"ORDER BY likes desc limit 6","id,title,likes"))

# 文章详情页
@app.route('/page/<status>',methods=['POST'])
def page(status):
    if request.method == 'POST':
        id = request.form['id']
        uid = request.form['uid']
        title = request.form['title']
        # 获取文章详细内容
        if status == 'init':
            where = 'where id=' + str(id)
            return jsonify(sql.select(mydb,'article',where))
        # 点赞
        elif status == 'likes':
            where = 'where postId=' + str(id) + " and uid='" + str(uid) +"'"
            res = sql.select(mydb,'user_likes',where)
            if len(res) == 0:
                res = sql.insert(mydb,'user_likes',uid=uid,postId=id,likes=1,title=title)
                # 插入成功
                if res[0] == 1:
                    mycursor = mydb.cursor(dictionary=True)
                    sqls = "update article set likes=likes+1 where id=" + str(id)
                    mycursor.execute(sqls)
                    mycursor.close()
                    mydb.commit()
                    return 'success'
                else:
                    return 'fails'
            elif len(res) == 1:
                mycursor = mydb.cursor(dictionary=True)
                sqls = "update user_likes set likes=1 where postId=" + str(id)
                mycursor.execute(sqls)
                mycursor.close()
                mydb.commit()
                if mycursor.rowcount == 1:
                    mycursor = mydb.cursor(dictionary=True)
                    sqls = "update article set likes=likes+1 where id=" + str(id)
                    mycursor.execute(sqls)
                    mycursor.close()
                    mydb.commit()
                    return 'success'
                else:
                    return 'fails'
        # 收藏
        elif status == 'collect':
            where = 'where postId=' + str(id) + " and uid='" + str(uid) +"'"
            res = sql.select(mydb,'user_likes',where)
            if len(res) == 0:
                res = sql.insert(mydb,'user_likes',uid=uid,postId=id,collect=1,title=title)
                # 插入成功
                if res[0] == 1:
                    return 'success'
                else:
                    return 'fails'
            elif len(res) == 1:
                mycursor = mydb.cursor(dictionary=True)
                sqls = "update user_likes set collect=1 where postId=" + str(id)
                mycursor.execute(sqls)
                mycursor.close()
                mydb.commit()
                if mycursor.rowcount == 1:
                    return 'success'
                else:
                    return 'fails'

#在线投稿
@app.route('/delivery',methods=['POST'])
def delivery():
    if request.method == 'POST':
        file = request.files['file']
        name = request.form['name']
        tel = request.form['tel']
        adr = request.form['adr']
        email = request.form['email']
        other = request.form['other']        
        pwd = os.path.abspath('.') + '/upload'
        fileName = str(int(time.time())) + '.pdf'
        filePath = os.path.join(pwd,fileName)
        file.save(filePath)
        res = sql.insert(mydb,'delivery',name=name,tel=tel,adr=adr,email=email,other=other,filePath=fileName)
        if res[0] == 1:
            return 'success'
        else:
            return 'fails'

# 初始化未审核投稿 
@app.route('/noaudit',methods=['POST'])
def noaudit():
    if request.method == 'POST':
        where = "where hasAudit=false"
        res = sql.select(mydb,'delivery',where)
        return jsonify(res)

# 初始化已审核投稿 
@app.route('/hasaudit',methods=['POST'])
def hasaudit():
    if request.method == 'POST':
        where = "where hasAudit=true"
        res = sql.select(mydb,'delivery',where)
        return jsonify(res)

@app.route('/audit',methods=['POST'])
def audit():
    if request.method == 'POST':
        id = request.get_json()['id']
        text = request.get_json()['text']
        mycursor = mydb.cursor(dictionary=True)
        sql = "update delivery set hasAudit=true,evaluate='" +text+"'" +" where id=" + str(id)
        mycursor.execute(sql)
        mycursor.close()
        mydb.commit()
        if mycursor.rowcount == 1:
            return 'success'
        
# 用户中心
@app.route('/userCenter',methods=['POST'])
def userCenter():
    if request.method == 'POST':
        uid = request.form['uid']
        where = "where uid='" + uid + "' and collect=1"
        return jsonify(sql.select(mydb,'user_likes',where,'postId,title'))

@app.route('/cms',methods=['POST'])
def cms():
    if request.method == 'POST':
        zhanghao = request.get_json()['zhanghao']
        pwd = request.get_json()['pwd']
        where = "where zhanghao='" + zhanghao + "' and pwd='" +pwd+ "'"
        res = sql.select(mydb,'cms',where)
        if len(res) == 1:
            return 'success'
        else:
            return 'fails'


if __name__ == '__main__':
    app.run()



