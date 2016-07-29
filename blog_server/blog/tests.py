# -*- coding: utf-8 -*-
import httplib, urllib,urllib2
import json
if __name__ == '__main__':

    #http://127.0.0.1:8000/art/wx_img_str
    httpClient = None
    try:
        url = 'http://127.0.0.1:8000/blog/artwork/'

        data  = {
            "open_id":12,
            "img_url":"http://mmbiz.qpic.cn/mmbiz/EmT9585IibD0V5dic327aVTjBFr1PgAcdzb7SDPK0Ndo3qqm26wHn6s4Qpf5TddjtpNFRrmL8CBb8Q64XuN13v4Q/0",
            "char_img_url": 'https://ss0.baidu.com/73t1bjeh1BF3odCf/it/u=2050787984,3198270160&fm=85&s=4EC0DC10B4FAE429207A30D9030070B3'
        }

        req = urllib2.Request(url)
        data = urllib.urlencode(data)
        #enable cookie
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
        response = opener.open(req,data)
        res = response.read()
        print res
    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()