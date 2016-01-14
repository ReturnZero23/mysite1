from django.http import HttpResponse,Http404
from django.template import Template,Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
import datetime
import pymysql
from django.db import connection


def hello(request):

#   return HttpResponse("Hello world")
#获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库

    try:
        #conn=pymysql.connect(host='localhost',user='root',passwd='930623',db='test',port=3306,charset='utf8')
        #cur=conn.cursor()#获取一个游标
        cur=connection.cursor()
        cur.execute('select * from test.diannengbiao')
        data=cur.fetchall()
        for d in data :
            #注意int类型需要使用str函数转义
            print("ID: "+str(d[0])+'  名字： '+d[1]+"  性别： "+d[2]+"  名字： "+d[3])

        cur.close()#关闭游标
        conn.close()#释放数据库资源
    except Exception :print('abc')
    return HttpResponse("Hello world")


def current_time(request):
    now = datetime.datetime.now()
    #t = get_template('mytemplate.html')
    #html = t.render(Context({'current_time':now}))
    #return HttpResponse(html)
    return render_to_response('mytemplate.html',{'current_time':now})

def hours_ahead(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><title>LYF</title><body>In %s hours , it will be %s.</body></html>"%(offset,dt)
    return HttpResponse(html)
