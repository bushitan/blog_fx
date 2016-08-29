# -*- coding: utf-8 -*-
import httplib, urllib,urllib2
import json
if __name__ == '__main__':

    httpClient = None
    try:
        #此处微信使用
        #1、先跟image服务获取数据
        #2、跟新blog的数据库

        url = 'http://127.0.0.1:8000/grid/api/game/'
        # url = 'http://120.27.97.33:91/grid/api/game/'
        data  = {  "img_url":"http://127.0.0.1:8000/static/art/img/20160706154153.png"}
        # data  = {  "img_url":"http://127.0.0.1:8000/static/art/img/1370454329.jpg"}

        data  = {  "img_url":"http://avatar.csdn.net/3/5/5/1_n289950578.jpg"}
        req = urllib2.Request(url)
        data = urllib.urlencode(data)
        #enable cookie
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
        response = opener.open(req,data)

        # stage_json = json.loads( response.read() ) #字符串变json
        stage_data =  response.read() #所有数据全部存储
        print stage_data
        # print obj
        # print  len(stage_data)


        url = 'http://127.0.0.1:8001/blog/game/add/'
        data  = {'stage_data':stage_data}
        req = urllib2.Request(url)
        data = urllib.urlencode(data)
        #enable cookie
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
        response = opener.open(req,data)
        res = response.read()
        print res

        # return HttpResponse(
        #     json.dumps(res),
        #     content_type="application/json"
        # )
    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()


    # str1 = "{u'1': [{u'y': 87, u'x': 68, u'r': 13}, {u'y': 71, u'x': 93, u'r': 14}], u'0': [{u'y': 72, u'x': 0, u'r': 12}], u'3': [{u'y': 15, u'x': 105, u'r': 13}], u'2': [{u'y': 2, u'x': 74, u'r': 15}, {u'y': 85, u'x': 98, u'r': 9}], u'5': [{u'y': 23, u'x': 12, u'r': 15}], u'4': [{u'y': 10, u'x': 90, u'r': 11}]}"
    # print str1.decode('utf-8"')