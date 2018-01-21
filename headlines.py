#!/usr/bin/python
#-*-coding:utf-8 -*-
from __future__ import unicode_literals
import datetime
import requests
import feedparser
from flask import Flask, render_template, request, make_response
from song import getMusicInfo
from linkdb import *
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
            "b1" : "http://news.baidu.com/n?cmd=1&class=civilnews&tn=rss" ,
            "b2" : "http://news.baidu.com/n?cmd=1&class=internews&tn=rss" ,
            "b3" : "http://news.baidu.com/n?cmd=1&class=mil&tn=rss" ,
            "souhu1" : "http://rss.news.sohu.com/rss/guonei.xml" ,
            "souhu2" : "http://rss.news.sohu.com/rss/guoji.xml"
            }

DEFAULTS = {'city': '北京',
            'publication': 'souhu2'}

WEATHERS = {"北京": 101010100,
            "上海": 101020100,
            "广州": 101280101,
            "深圳": 101280601}


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
    city = get_value_with_fallback('city')

    weather = get_weather(city) #获得天气
    articles = get_news(publication) #获得头条数据

    response = make_response(render_template('top.html', articles=articles,
                                             weather=weather))

    expires = datetime.datetime.now() + datetime.timedelta(days=365)
    response.set_cookie('publication',  publication, expires=expires)
    response.set_cookie('city',  city, expires=expires)

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
    print(music_info[0])
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
    msgAdd(title , shortmsg , msg)
    return "添加成功"

@app.route('/msgSelect' , methods=['GET', 'POST'])
def msgSelectFn():
    msg = msgSelect()
    
    print(msg)
    msg = json.dumps(msg)
    return msg

def get_news(publication):
    feed = feedparser.parse(RSS_FEED[publication])
    return feed['entries']


def get_weather(city):
    code = WEATHERS.get(city, 101010100)
    url = "http://www.weather.com.cn/data/sk/{0}.html".format(code)

    r = requests.get(url)
    r.encoding = 'utf-8'

    data = r.json()['weatherinfo']
    return dict(city=data['city'], temperature=data['temp'],
                description=data['WD'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5678, debug=True)
    # app.run(host='192.168.1.33', port=5678, debug=True)
