from ast import keyword
from multiprocessing import connection
from unittest import result
from django.shortcuts import render
from django.http import HttpResponse
from django.db import connections
from myapp.models import students
from django.forms.models import model_to_dict

def serach_list(request):
    ########################################
    # 可檢查sql寫法
    if 'cName' in request.GET:
        # print("ok")
        cName = request.GET['cName']
        print(cName) 
        # ORM:
        #resultList = students.objects.filter(cName=cName)
        resultList = students.objects.filter(cName__contains=cName)
    else:
        # print("false")
        # resultList= students.objects.all().order_by("-cID")  #讀取資料表, 依 id 遞減排序
        # ORM:
        resultList= students.objects.all().order_by("id")  #讀取資料表, 依 id 遞增排序
        for d in resultList:
            print(model_to_dict(d))
    
    errormessage=""
    if not resultList: #判斷有無資料
        errormessage="無此資料"
    # print(errormessage)
    # print(resultList)
    # return HttpResponse("test...")
    return render(request,"serach_list.html",locals())

def search_name(request):
    # return HttpResponse("test...")
    return render(request,"search_name.html",locals())

from django.db.models import Q
def index(request):
    if 'site_search' in request.GET:
        site_search = request.GET["site_search"]
        site_search= site_search.strip() #去除空白        
        
        #####################
        # #multiple key words
        keywords = site_search.split() #切割字元，但空格不會切
        print(keywords)
        
        # orm:
        q_objects = Q()
        for keyword in keywords:
            q_objects.add(Q(cName__contains=keyword), Q.OR) 
            q_objects.add(Q(cSex__contains=keyword), Q.OR)
            q_objects.add(Q(cBirthday__contains=keyword), Q.OR)
            q_objects.add(Q(cEmail__contains=keyword), Q.OR)
            q_objects.add(Q(cPhone__contains=keyword), Q.OR)
            q_objects.add(Q(cAddr__contains=keyword), Q.OR)
        print(q_objects)
        # reference
        # https://stackoverflow.com/questions/852414/how-to-dynamically-compose-an-or-query-filter-in-django
        # print(sql)
        # resultList=[] # check
        # resultList = students.objects.filter(cName__contains=keyword)
        # resultList = students.objects.filter(
        #     Q(cName__contains=keyword)|
        #     Q(cEmail__contains=keyword)|
        #     Q(cPhone__contains=keyword)|
        #     Q(cAddr__contains=keyword)
        # )

        resultList = students.objects.filter(q_objects)
    else:
        # ORM:
        resultList= students.objects.all().order_by("id")  #讀取資料表, 依 id 遞增排序

    status=True
    # resultList=[] #check empty
    if not resultList: #判斷有無資料
        errormessage="無此資料"
        status=False
    # print(errormessage)
    data_count=len(resultList)
    # print(data_count)
    # return HttpResponse("test...")
    
    return render(request,"index.html",locals())

from django.shortcuts import redirect
def post1(request):
    if request.method == "POST":
        cName = request.POST["cName"]
        cSex = request.POST["cSex"]
        cBirthday = request.POST["cBirthday"]
        cEmail = request.POST["cEmail"]
        cPhone = request.POST["cPhone"]
        cAddr = request.POST["cAddr"]
        print("{}:{}:{}:{}:{}:{}".format(cName, cSex, cBirthday, cEmail, cPhone, cAddr))
        # print(cName+" "+cSex+" "+cBirthday+" "+cEmail+" "+cPhone+" "+cAddr+" ")

         # orm:
        add = students(cName=cName, cSex=cSex, cBirthday=cBirthday, cEmail=cEmail, cPhone=cPhone, cAddr=cAddr)
        add.save()

        # return HttpResponse("已送出...")
        return redirect('/index/') #自動轉址
    else:
        # return HttpResponse("test...")
        return render(request,"post1.html",locals())

def edit1(request, id=None, mode=None):
    # print(id)
    # print(mode)
    if mode == "edit":
        cName = request.GET["cName"]
        cSex = request.GET["cSex"]
        cBirthday = request.GET["cBirthday"]
        cEmail = request.GET["cEmail"]
        cPhone = request.GET["cPhone"]
        cAddr = request.GET["cAddr"]
        # print(cName)
        # print(cSex)
        # print(cBirthday)
        # print(cEmail)
        # print(cPhone)
        # print(cAddr)
        
        # orm:
        update = students.objects.get(id=id)
        update.cName = cName
        update.cSex = cSex
        update.cBirthday = cBirthday
        update.cEmail = cEmail
        update.cPhone = cPhone
        update.cAddr = cAddr
        update.save()

        # return HttpResponse("修改.......")
        return redirect('/index/')
    elif mode == "load":
        # orm:
        dict_data = students.objects.get(id=id)
        # return HttpResponse("test.......")
        return render(request,"edit1.html", locals())

def edit2(request, id=None):
    # print(id)
    if request.method == "POST":
        cName = request.POST["cName"]
        cSex = request.POST["cSex"]
        cBirthday = request.POST["cBirthday"]
        cEmail = request.POST["cEmail"]
        cPhone = request.POST["cPhone"]
        cAddr = request.POST["cAddr"]
        # print(cName)
        # print(cSex)
        # print(cBirthday)
        # print(cEmail)
        # print(cPhone)
        # print(cAddr)
        
        # orm:
        update = students.objects.get(id=id)
        update.cName = cName
        update.cSex = cSex
        update.cBirthday = cBirthday
        update.cEmail = cEmail
        update.cPhone = cPhone
        update.cAddr = cAddr
        update.save()

        # return HttpResponse("修改.......")
        return redirect('/index/')
    else:
       # orm:
        dict_data = students.objects.get(id=id)
        print(dict_data)
        # return HttpResponse("test.......")
        return render(request,"edit2.html", locals())

def delete(request, id=None):
    if request.method == "POST":
        # orm:
        delete_data = students.objects.get(id=id)
        delete_data.delete()
        # return HttpResponse("按刪除")
        return redirect('/index/')
    else:
        # orm:
        dict_data = students.objects.get(id=id)
        # return HttpResponse("test.......")
        return render(request,"delete.html", locals())