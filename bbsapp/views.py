from django.shortcuts import render
from django.core.paginator import Paginator
from bbsapp.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q

# Create your views here.


def mainpage(request):
    postings=Posting.objects.all()
    page_num=request.GET.get('page',1)  # 第二个参数为第一参数没有时的默认值

    paginator=Paginator(postings,30)
    c_page=paginator.page(int(page_num))

    return render(request, 'bbsapp/mainpage.html', locals())



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




