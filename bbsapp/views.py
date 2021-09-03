from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from bbsapp.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q


# Create your views here.
#ip遮掩网段函数
def maskip(userip):
    a = []

    for i in range(len(userip)):
        a.append(userip[i])

    b = ''
    num = 0
    for j in range(len(userip)):
        if a[j] == '.':
            num += 1
        if num != 2:
            b += a[j]
        elif num == 2:
            if a[j] == '.':
                b += a[j]
                for n in range(3):
                    b += '*'
    return b


# bbs主页
def mainpage(request):
    postings = Posting.objects.all().order_by('-created_time')

    paginator = Paginator(postings, 30)
    page_num = request.GET.get('page', 1)  # 第二个参数为第一参数没有时的默认值
    c_page = paginator.page(int(page_num))

    return render(request, 'bbsapp/mainpage.html', locals())

# 搜索功能
def search(request):
    s_title=request.GET.get('s_title')

    postings=Posting.objects.filter(Q(title__icontains=s_title)&Q(is_active=True))

    paginator = Paginator(postings, 30)
    page_num = request.GET.get('page', 1)  # 第二个参数为第一参数没有时的默认值
    c_page = paginator.page(int(page_num))
    print(postings)

    return render(request,'bbsapp/searchpage.html',locals())


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

    # 获取游客IP并伪装
    userip=request.META['REMOTE_ADDR']
    mkip=maskip(userip)
    if not poster:
        poster='游客'+mkip

    # 防止空内容和空标题
    if ptitle == '' or pcontent == '':
        return HttpResponse('请输入标题和内容')

    # 生成帖子的主键index的代码块
    a = Posting.objects.last()
    if not bool(a):
        lindex = "0000000001"
        pstindex = lindex
    else:
        lindex = int(a.index)
        lindex += 1
        pstindex = str(lindex).zfill(10)

    # 帖子数据写入数据库
    Posting.objects.create(index=pstindex,title=ptitle,content=pcontent,poster=poster,comment_num=0)

    # 查出前端需要的数据
    posting=Posting.objects.filter(Q(index=pstindex)&Q(is_active=True))
    flag=1

    return render(request, 'bbsapp/posting.html', locals())


# 添加评论功能
def create_cmt(request):
    ptindex = request.POST.get('ptindex')
    ccontent = request.POST.get('ccontent')
    poster = request.GET.get('poster')
    page = request.GET.get('page')

    # 获取游客IP并伪装
    userip=request.META['REMOTE_ADDR']
    mskip=maskip(userip)
    if not poster:
        poster = '游客'+mskip

    # 获取关联帖子
    posting = Posting.objects.filter(Q(index=ptindex)&Q(is_active=True))

    # 防止空内容
    if ccontent == '':
        return HttpResponse('请输入内容')

    # 制作主键index的代码块
    a = Comments.objects.last()
    if not bool(a):
        lindex = "0000000001"
        cmtindex = lindex
    else:
        lindex = int(a.index)
        lindex += 1
        cmtindex = str(lindex).zfill(10)

    # 制作楼层的代码块
    b=Comments.objects.filter(Q(posting_id=ptindex))
    if not b:
        floor=1
    else:
        floor=len(b)+1

    # 写评论数据到表内
    Comments.objects.create(index=cmtindex, content=ccontent, poster=poster, posting_id=ptindex,floor=floor)

    # 写评论数到帖子表的comment_num列
    comment_num = posting[0].comment_num
    comment_num += 1

    # 修改帖子的评论数数据
    posting.update(comment_num=comment_num)

    # 查出前端需要的数据
    comments = Comments.objects.filter(Q(posting_id=ptindex)&Q(is_active=True)).order_by('created_time')
    page_num = request.GET.get('page', 1)
    paginator = Paginator(comments, 30)
    c_page = paginator.page(int(page_num))

    return render(request, 'bbsapp/posting.html', locals())


# 回到主页功能
def backmain(request):
    return HttpResponseRedirect('/bbsapp/mainpage')


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
