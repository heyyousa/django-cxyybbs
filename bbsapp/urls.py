from django.urls import path
from bbsapp import views

urlpatterns = [
    path('mainpage/',views.mainpage),  # 主页函数带分页功能
    path('posting/',views.posting),  # 帖子页面
    path('search/',views.search),  # 搜索功能
    path('wposting/',views.wposting),  # 发帖页面
    path('create_pst/',views.create_pst),  # 发帖功能
    path('create_cmt/',views.create_cmt),  # 评论功能
    path('backmain/',views.backmain),  # 返回主页
    path('test/',views.test),  # 测试页
    path('wdata/',views.wdata),  # 写入帖子数据
    path('wcomments/',views.wcomments),  # 写评论数据
]