from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

"""
表
cart
主键
商品图片表里 商品的图片  商品表 商品的名称  商品的价格   
关联商品
商品的数量
"""

"""
cart_id
外键  shop_id
number 数量
外键 user_id
status
"""

"""
验证登录
验证登录跳转的连接
1>在装饰器使用
2> 全局验证登录调转连接
"""


# 添加商品到购物车
@login_required
def add_car(request):
    return HttpResponse('1111')


# 查看购物车功能
def list(reqeust):
    pass


# 修改购物车商品的数量
def update(reqeust):
    pass


def delete(request):
    pass
