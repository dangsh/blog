#!/usr/bin/python
#-*-coding:utf-8 -*-
from __future__ import unicode_literals
import datetime
import requests
import feedparser
from flask import Flask, render_template, request, make_response
import linkdb
import json

app = Flask(__name__)



@app.route('/')
def index():
    return render_template("index.html")

@app.errorhandler(404)
def lostPage(err):
    return render_template("404.html")


@app.route('/delSpace')
def delSpaceFn():
    return render_template("delSpace.html")

@app.route('/delChar')
def delCharFn():
    return render_template("delChar.html")

@app.route('/color')
def colorFn():
    return render_template("color.html")

@app.route('/base')
def baseFn():
    return render_template("base.html")  

@app.route('/login')
def loginFn():
    return render_template("login.html")

@app.route('/loginCheck' , methods=['GET', 'POST'])
def loginCheckFn():
    username = request.form.get('username','111')
    password = request.form.get('password','222')
    print(username , password)
    if username == "zxg" and password == "123456":
        return render_template("manage.html")
    else:
        return render_template("login.html")

@app.route('/forgot')
def forgotFn():
    return render_template("forgot.html")

@app.route('/sign')
def signFn():
    return render_template("sign.html")

@app.route('/messageboard')
def messageboardFn():
    return render_template("messageBoard.html")

@app.route('/proxy')
def proxyFn():
    return render_template("proxy.html")

@app.route('/getProxy' , methods=['GET' , 'POST'])
def getProxyFn():
    if request.method == "POST":
        msg = linkdb.selectProxy()
        msg = json.dumps(msg)
        return msg
    if request.method == "GET":
        score = request.args.get('score')
        if score == '10':
            msg = linkdb.selectGoodProxy()
            msg = json.dumps(msg)
        elif score == 'other':
            msg = linkdb.selectAllProxy()
            msg = json.dumps(msg)
        else:
            pass
        return msg

@app.route('/addmsg' , methods=['GET' , 'POST'])
def addmsgFn():
    return render_template("addmsg.html")

@app.route('/msgAdd' , methods=['GET', 'POST'])
def msgAddFn():
    title = request.form.get('title','111')
    shortmsg = request.form.get('shortmsg','222')
    msg = request.form.get('msg','111')
    linkdb.msgAdd(title , shortmsg , msg)
    return render_template("manage.html")

@app.route('/msgSelect' , methods=['GET', 'POST'])
def msgSelectFn():
    if request.method == "GET":
        page = request.args.get('page')
        print(page)
        msg = linkdb.msgSelect(page)
        msg = json.dumps(msg)
        return msg
    else:
        num = linkdb.msgPageSelect()
        num = json.dumps(num)
        return num

@app.route('/oneSelect' , methods=['GET', 'POST'])
def oneSelectFn():
    id = request.args.get('id')
    msg = linkdb.oneSelect(id)
    msg = json.dumps(msg)
    return msg

@app.route('/msgDel' , methods=['GET', 'POST'])
def msgDelFn():
    id = request.args.get('id') 
    linkdb.msgDel(id)
    return render_template("manage.html")
    
@app.route('/content' , methods=['GET', 'POST'])
def contentFn():
    id = request.args.get('id')
    return render_template("content.html")





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5678, debug=True)
    # app.run(host='192.168.1.33', port=5678, debug=True)
