import requests
import re
import json 



def download(url , data=None):
    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
    }
    try:
        return requests.get(url , params=data , headers=header)
    except Exception as e:
        print(e)

def getMusicId(name):
    api = 'http://music.baidu.com/search'
    data = {
        'key' : name
    }
    response = download(api , data = data)
    response.encoding = 'utf-8'
    html = response.text
    ul = re.findall(r'<ul.*</ul>' , html , re.S)[0]
    sids = re.findall(r'sid&quot;:(\d+),' , ul , re.S)
    return sids

def getSong(songid):
    url = 'http://tingapi.ting.baidu.com/v1/restserver/ting?method=baidu.ting.song.play&format=jsonp&callback=jQuery17205500581185420972_1513324047403&songid=%s&_=1513324048127' %songid
    data = download(url).text
    data = re.findall(r'\((.*)\)' , data)[0]
    data = json.loads(data)
    return data

def getMusicInfo(name):
    sids = getMusicId(name)
    music_info = []
    for sid in sids:
        temp = getSong(sid)
        music_info.append(temp)
    return music_info

if __name__ == '__main__':
    music_info = getMusicInfo('刘德华')
    print(music_info)