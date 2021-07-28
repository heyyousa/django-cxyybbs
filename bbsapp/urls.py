from django.urls import path
from bbsapp import views

urlpatterns = [
    path('mainpage/',views.mainpage),  # 主页函数带分页功能
    path('wdata/',views.wdata),  # 写入测试数据
]