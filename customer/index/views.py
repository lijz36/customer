from django.shortcuts import render
from django.http import *
from django.db.models import F, Q
from .models import *
from utils.commons import *


# 全局变量
USERID = 'id'

# 获取网站标题
def get_title():
    titles = Title.objects.all()
    if titles:
        title = titles[0].name
    else:
        title = '客户管理系统'
    return title


# 登录页面处理视图
def login_views(request):
    title = get_title()
    if request.method == 'POST':
        uphone = request.POST.get('uphone', '')
        upass = request.POST.get('upass', '')
        usave = request.POST.get('usave', False)
        if uphone and upass:
            users = Users.objects.filter(user_phone=uphone)
            if users:
                u = users[0]
                if u.user_active:
                    cur_upass = md5_hash(upass)
                    if cur_upass == u.user_passwd:
                        resp = HttpResponseRedirect('/main/')
                        if usave:
                            resp.set_cookie(USERID, u.id, expires=60*30)
                        return resp
                    else:
                        err_msg = "密码输入错误"
                        return render(request, 'index.html', locals())
                else:
                    err_msg = "此手机号被锁定"
                    return render(request, 'index.html', locals())
            else:
                err_msg = "手机号不存在"
                return render(request, 'index.html', locals())
        else:
            if not uphone:
                err_msg = "手机号不能为空"
            elif not upass:
                err_msg = "密码不能为空"
            return render(request, 'index.html', locals())
    else:
        if USERID in request.session:
            return HttpResponseRedirect('/main/')
        else:
            return render(request, 'index.html', locals())


# 主页面视图处理函数
def main_views(request):
    if request.method == "GET":
        title = get_title()

        if USERID in request.session:
            cur_id = request.session.get(USERID)
            user = Users.objects.get(id=cur_id)

            types = Types.objects.all()
            sectypes = dict()
            for t in types:
                sectypes[t.id] = t.sectypes_set.all()
            return render(request, 'main.html', locals())
        else:
            if USERID in request.COOKIES:
                dic = request.COOKIES
                request.session[USERID] = dic[USERID]
                request.session.set_expiry(0)
                user = Users.objects.get(id=dic[USERID])

                types = Types.objects.all()
                sectypes = dict()
                for t in types:
                    sectypes[t.id] = t.sectypes_set.all()
                return render(request, 'main.html', locals())
            else:
                return HttpResponseRedirect('/')


# 进入后台登录页面处理视图
def admin_views(request):
    if request.method == "GET":
        return HttpResponseRedirect('/admin/')


# 退出登录处理视图
def logout_views(request):
    if request.method == 'GET':
        if USERID in request.session:
            del request.session[USERID]
    return HttpResponseRedirect('/')


# 修改用户密码处理视图
def changepwd_view(request):
    if request.method == 'GET':
        if USERID in request.session:
            user_id = request.session.get(USERID)
            return render(request, 'changepwd.html', locals())
        elif USERID in request.COOKIES:
            user_id = request.COOKIES[USERID]
            return render(request, 'changepwd.html', locals())
        else:
            return HttpResponseRedirect('/')