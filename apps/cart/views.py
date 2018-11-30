import datetime
import json
import random
from functools import wraps

from django.contrib.auth.decorators import login_required
from django.core import cache
from django.db.models import F
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django_ajax.decorators import ajax
from django_redis import get_redis_connection

from apps.main.models import ShopCar, Order

from django.db import transaction

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
    if request.method == 'POST':
        try:
            number = request.POST.get("number")
            shop_id = request.POST.get('shop_id')
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


# redis
def add_car1(request):
    number = request.GET.get("number")
    shop_id = request.GET.get('shop_id')
    if number > 0 and shop_id > 0:
        user_id = request.user.id
        rds = get_redis_connection()
        car_name = f'cart:{user_id}'
        value = rds.hget(car_name, shop_id)
        # 如果有值 做累加操作
        if value:
            value += number
            rds.hset(name=car_name, key=shop_id, value=value)
        else:
            rds.hset(name=car_name, key=shop_id, value=number)
    else:
        return HttpResponse('参数错误')
    # # string  list   hash  set  zset
    # rds.hset('h', key=111, value=222)
    # rds.hget(name='h', key=111)
    # # 列表操作
    # # li  [ 1, 2, 3, 4, 5, 5, 6,7]
    # rds.lpush('li', 1, 2, 3, 4, 5, 5, 6)
    # rds.rpush('li', 7)
    # # 获取列表的中元素
    # rds.lrange(name=, start=0, end=10)
    # # key [1,2]
    # rds.sadd('key', 1, 1, 2, 2)
    # # rds.zadd()
    return HttpResponse(11111)


@login_required
def list(reqeust):
    car_list = ShopCar.objects.filter(user_id=reqeust.user.id)
    for car in car_list:
        car.shop.img = car.shop.image_set \
            .filter(shop=car.shop) \
            .values_list('shop_img_id', flat=True) \
            .first()
    return render(reqeust, 'car.html', {'car_list': car_list})


# 修改购物车商品的数量
def update(reqeust):
    pass


def delete(request):
    pass


# 开始事务
@ajax
@login_required
def confirm(request):
    if request.method == 'POST':
        cars_str = request.POST.get('car')
        if cars_str:
            # [{carid:1,number:10}]
            cars = json.loads(cars_str)
            try:
                # 开启事务
                with transaction.atomic():
                    # 生成订单
                    oid = product_order(request, cars)
                    #      做事务相关的操作
                    for car in cars:
                        ShopCar.objects.filter(car_id=car.get('car_id')).update(number=car.get('num'), order_id=oid)
                #    生成订单的操作
                return {'oid': oid}
            except Exception as e:
                transaction.rollback()
        else:
            pass


# 生成订单信息
def product_order(request, cars):
    # 第一步生成订单号  全站必须唯一   尽量大于8位
    user_id = request.user.id
    order_code = f"{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}{random.randint(100000,999999)}"
    order = Order(order_code=order_code, user_id=user_id)
    order.save()
    return order.oid


@login_required
def confirm1(request):
    oid = request.GET.get('oid')
    shops = ShopCar.objects.filter(order_id=oid)
    return render(request, 'confirm.html', {'shops': shops})
