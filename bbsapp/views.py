from django.shortcuts import render
from django.core.paginator import Paginator
from bbsapp.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q

# Create your views here.

#bbs主页
def mainpage(request):
    postings=Posting.objects.all()
    page_num=request.GET.get('page',1)  # 第二个参数为第一参数没有时的默认值

    paginator=Paginator(postings,30)
    c_page=paginator.page(int(page_num))

    return render(request, 'bbsapp/mainpage.html', locals())


#帖子页面
def postingpage(request):
    postingid=request.GET.get('ptindex')
    posting=Posting.objects.filter(Q(index=postingid),Q(is_active=True))

    comments = Comments.objects.filter(Q(posting_id=postingid), Q(is_active=True))
    page_num=request.GET.get('page',1)

    paginator=Paginator(comments,30)
    c_page=paginator.page(int(page_num))

    return render(request,'bbsapp/posting.html',locals())

#发帖页面
def wposting(request):
    return render(request,'bbsapp/wposting.html',locals())

#发帖功能
def create_pst(request):
    ptitle=request.POST.get('ptitle')
    pcontent=request.POST.get('pcontent')
    poster=request.GET.get('poster')

    if ptitle=='' or pcontent=='':
        return HttpResponse('请输入标题和内容')

    a = Posting.objects.last()
    if not bool(a):
        lindex = "0000000001"
        pstindex = lindex
    else:
        lindex = int(a.index)
        lindex += 1
        pstindex = str(lindex).zfill(10)

    posting=Posting.objects.create(index=pstindex,title=ptitle,content=pcontent,poster=poster)

    return render(request,'bbsapp/posting.html',locals())

#回到主页功能
def backmain(request):
    return HttpResponseRedirect('/bbsapp/mainpage')

#回到顶部功能
def backtop(request):
    chtml=request.GET.get('chtml')
    if chtml=='main':
        return HttpResponseRedirect('/bbsapp/mainpage')
    elif chtml=='comment':
        return HttpResponseRedirect('/bbsapp/posting.html')

#写帖子测试数据函数
def wdata(request):
    for i in range(0,30):
        a = Posting.objects.last()

        if not bool(a):
            lindex = "0000000001"
            pstindex = lindex
        else:
            lindex = int(a.index)
            lindex += 1
            pstindex = str(lindex).zfill(10)

        Posting.objects.create(index=pstindex,title='test'+str(int(pstindex)),content='xxxx'+str(i),comment_num=i,like_num=i+2,poster='wang')

    return HttpResponse('添加成功')


#写评论测试数据
def wcomments(request):
    for i in range(0,30):
        a = Comments.objects.last()

        if not bool(a):
            lindex = "0000000001"
            pstindex = lindex
        else:
            lindex = int(a.index)
            lindex += 1
            pstindex = str(lindex).zfill(10)

        Comments.objects.create(index=pstindex,content='test'+str(int(pstindex)),poster='wwwww',posting_id='0000000001')

    return HttpResponse('添加成功')


def test(request):
    return render(request,'bbsapp/test.html')


