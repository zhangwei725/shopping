from functools import wraps

from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django_ajax.decorators import ajax

from apps.main.models import ShopCar
from shopping import settings

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


# def axjx_login_required(func):
#     def inner(request, *args, **kwargs):
#         if request.user.is_authenticated():
#             return func(request, *args, **kwargs)
#         else:
#             return redirect(settings.LOGIN_URL.join('?next=').join(request.path))
#     return inner


# 添加商品到购物车
# 浏览器的一种机制
@ajax
@login_required
def add_car(request):
    result = {'status': 200, 'msg': 'ok'}
    if request.method == 'GET':
        try:
            number = request.GET.get("number")
            shop_id = request.GET.get('shop_id')
            # 如果商品存在用户的购物车更新的操作
            # string list  hash set
            car = ShopCar.objects.filter(shop_id=shop_id, user_id=request.user.id, status=1)
            update_number = 0
            if car.exists():
                # 如果存在应该是做更新的操作
                car.update(number=F('number') + number)
            else:
                update_number = 1
                car = ShopCar(number=number, shop_id=shop_id, user_id=request.user.id)
                car.save()
            result.update(data=update_number)
            return JsonResponse(result)
        except Exception as e:
            result = {'status': 400, 'msg': '添加失败'}
            return JsonResponse(result)
    else:
        result = {'status': 2, 'msg': '不支持的请求方式'}
        return JsonResponse(result)


@login_required
def list(reqeust):
    car_list = ShopCar.objects.filter(user_id=reqeust.user.id)
    return  render(reqeust,'cars.html')

# 修改购物车商品的数量
def update(reqeust):
    pass


def delete(request):
    pass
