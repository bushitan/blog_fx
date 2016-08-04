# -*- coding: utf-8 -*-
import httplib, urllib,urllib2
import json
if __name__ == '__main__':

    #http://127.0.0.1:8000/art/wx_img_str
    httpClient = None
    try:
        # url = 'http://127.0.0.1:8000/blog/artwork/'
        url = 'http://120.27.97.33:82/blog/artwork/'


        data  = {
            "open_id":13,
            "img_url":"http://h.hiphotos.baidu.com/zhidao/wh%3D600%2C800/sign=546fe1ddb1119313c716f7b6550820ef/0b7b02087bf40ad165f5e8fc542c11dfa9ecce9f.jpg",
            "char_img_url": 'http://zhidao.baidu.com/daily/view?id=18711'
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