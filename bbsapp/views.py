from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from bbsapp.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q


# Create your views here.

# bbs主页
def mainpage(request):
    postings = Posting.objects.all()

    paginator = Paginator(postings, 30)
    page_num = request.GET.get('page', 1)  # 第二个参数为第一参数没有时的默认值
    c_page = paginator.page(int(page_num))

    return render(request, 'bbsapp/mainpage.html', locals())


# 帖子页面
def posting(request):
    postingid = request.GET.get('ptindex')

    posting = Posting.objects.filter(Q(index=postingid), Q(is_active=True))
    comments = Comments.objects.filter(Q(posting_id=postingid), Q(is_active=True))

    paginator = Paginator(comments, 30) # 分页对象
    page_num = request.GET.get('page', 1) # 获取当前页数字
    c_page = paginator.page(int(page_num)) # 当前页

    return render(request, 'bbsapp/posting.html', locals())


# 发帖页面
def wposting(request):
    return render(request, 'bbsapp/wposting.html', locals())

# 发帖功能
def create_pst(request):
    # 从request中获取有用信息
    ptitle = request.POST.get('ptitle')
    pcontent = request.POST.get('pcontent')
    poster = request.GET.get('poster')

    # 获取用户IP
    userip=request.META['REMOTE_ADDR']

    if ptitle == '' or pcontent == '':
        return HttpResponse('请输入标题和内容')
    if not poster:
        poster='游客'+userip

    a = Posting.objects.last()
    if not bool(a):
        lindex = "0000000001"
        pstindex = lindex
    else:
        lindex = int(a.index)
        lindex += 1
        pstindex = str(lindex).zfill(10)

    Posting.objects.create(index=pstindex,title=ptitle,content=pcontent,poster=poster,comment_num=0)
    posting=Posting.objects.filter(index=pstindex,is_active=True)

    return render(request, 'bbsapp/posting.html', locals())


# 添加评论功能
def create_cmt(request):
    ptindex = request.POST.get('ptindex')
    ccontent = request.POST.get('ccontent')
    poster = request.GET.get('poster')
    page = request.GET.get('page')

    # 获取用户IP
    userip=request.META['REMOTE_ADDR']
    ipmask=userip[0:7]+'***'+userip[:-1]

    posting = Posting.objects.filter(Q(index=ptindex), Q(is_active=True))

    if ccontent == '':
        return HttpResponse('请输入内容')

    if not poster:
        poster = '游客'+userip

    a = Comments.objects.last()
    if not bool(a):
        lindex = "0000000001"
        cmtindex = lindex
    else:
        lindex = int(a.index)
        lindex += 1
        cmtindex = str(lindex).zfill(10)

    comment_num=posting[0].comment_num
    comment_num+=1

    Comments.objects.create(index=cmtindex, content=ccontent, poster=poster, posting_id=ptindex)

    posting.update(comment_num=comment_num)

    comments = Comments.objects.filter(Q(posting_id=ptindex), Q(is_active=True)).order_by('created_time')
    page_num = request.GET.get('page', 1)
    paginator = Paginator(comments, 30)
    c_page = paginator.page(int(page_num))

    return render(request, 'bbsapp/posting.html', locals())


# 回到主页功能
def backmain(request):
    return HttpResponseRedirect('/bbsapp/mainpage')


# 回到顶部功能
def backtop(request):
    chtml = request.GET.get('chtml')

    if chtml == 'main':
        return HttpResponseRedirect('/bbsapp/mainpage')
    else:
        return HttpResponseRedirect('/bbsapp/posting')


# 写帖子测试数据函数
def wdata(request):
    for i in range(0, 30):
        a = Posting.objects.last()

        if not bool(a):
            lindex = "0000000001"
            pstindex = lindex
        else:
            lindex = int(a.index)
            lindex += 1
            pstindex = str(lindex).zfill(10)

        Posting.objects.create(index=pstindex, title='test' + str(int(pstindex)), content='xxxx' + str(i),
                               comment_num=i, like_num=i + 2, poster='wang')

    return HttpResponse('添加成功')


# 写评论测试数据
def wcomments(request):
    for i in range(0, 30):
        a = Comments.objects.last()

        if not bool(a):
            lindex = "0000000001"
            pstindex = lindex
        else:
            lindex = int(a.index)
            lindex += 1
            pstindex = str(lindex).zfill(10)

        Comments.objects.create(index=pstindex, content='test' + str(int(pstindex)), poster='wwwww',
                                posting_id='0000000001')

    return HttpResponse('添加成功')


def test(request):
    return render(request, 'bbsapp/test.html')
