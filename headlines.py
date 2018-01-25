#!/usr/bin/python
#-*-coding:utf-8 -*-
from __future__ import unicode_literals
import datetime
import requests
import feedparser
from flask import Flask, render_template, request, make_response
from song import getMusicInfo
import linkdb
import json

app = Flask(__name__)

RSS_FEED = {"zhihu": "https://www.zhihu.com/rss",
            "netease": "http://news.163.com/special/00011K6L/rss_newsattitude.xml",
            "songshuhui": "http://songshuhui.net/feed",
            "t1": "http://news.qq.com/newsgn/rss_newsgn.xml" ,
            "t2": "http://news.qq.com/newsgj/rss_newswj.xml",
            "s1":"http://rss.sina.com.cn/news/china/focus15.xml" ,
            "s2":"http://rss.sina.com.cn/news/world/focus15.xml" ,
            "fankexue" : "http://pansci.asia/feed" ,
            "r1" : "http://www.people.com.cn/rss/politics.xml" ,
            "r2" : "http://www.people.com.cn/rss/world.xml" ,
            "w1" : "http://news.163.com/special/00011K6L/rss_newstop.xml" ,
            "k1" : "http://www.sciencenet.cn/xml/news-0.aspx?news=0",
            "k2" : "http://www.sciencenet.cn/xml/news-0.aspx?di=0" ,
            "k3" : "http://www.sciencenet.cn/xml/news-0.aspx?di=1" ,
            "k4" : "http://www.sciencenet.cn/xml/news-0.aspx?di=7" ,
            "souhu1" : "http://rss.news.sohu.com/rss/guonei.xml" ,
            "souhu2" : "http://rss.news.sohu.com/rss/guoji.xml"
            }

DEFAULTS = {'publication': 'souhu2'}



def get_value_with_fallback(key):
    if request.args.get(key):
        return request.args.get(key)
    if request.cookies.get(key):
        return request.cookies.get(key)
    return DEFAULTS[key]

@app.route('/')
def index():
    return render_template("index3.html")

@app.errorhandler(404)
def lostPage(err):
    # return render_template("lostPage.html")
    # return redirect(url_for("indexFn"))
    return "我是404界面"

@app.route('/about')
def aboutFn():
    return render_template("about.html")

@app.route('/top')
def home():
    publication = get_value_with_fallback('publication')
    articles = get_news(publication) #获得头条数据
    response = make_response(render_template('top.html', articles=articles,))
    response.set_cookie('publication',  publication)
    return response

@app.route('/delSpace')
def delSpaceFn():
    return render_template("delSpace.html")

@app.route('/delChar')
def delCharFn():
    return render_template("delChar.html")

@app.route('/music')
def musicFn():
    name = get_value_with_fallback('publication')
    info  = getMusicInfo(name)
    response = make_response(render_template('music.html' , info=info))
    return response

@app.route('/musicImp')
def musicImpFn():
    music_info  = getMusicInfo('周星驰')
    response = make_response(render_template('music.html'))
    return response

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
    msg = linkdb.msgSelect()
    msg = json.dumps(msg)
    return msg

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
    return "删除成功"
    
@app.route('/content' , methods=['GET', 'POST'])
def contentFn():
    id = request.args.get('id')
    return render_template("content.html")

def get_news(publication):
    feed = feedparser.parse(RSS_FEED[publication])
    return feed['entries']




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5678, debug=True)
    # app.run(host='192.168.1.33', port=5678, debug=True)
