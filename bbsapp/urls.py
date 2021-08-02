from django.urls import path
from bbsapp import views

urlpatterns = [
    path('mainpage/',views.mainpage),  # 主页函数带分页功能
    path('wdata/',views.wdata),  # 写入帖子数据
    path('posting/',views.posting),  # 帖子页面
    path('wposting/',views.wposting),  # 发帖页面
    path('create_pst/',views.create_pst),  # 发帖功能
    path('wcomment/',views.wcomment),  # 评论页面
    path('create_cmt/',views.create_cmt),  # 评论功能
    path('backmain/',views.backmain),  # 返回主页
    path('backtop/',views.backtop),  # 返回顶部
    path('test/',views.test),  # 测试页
    path('wcomments/',views.wcomments),  # 写评论数据
]