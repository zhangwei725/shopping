from django.shortcuts import render

from apps.main.models import Shop, Image, PropertyValue, Review

"""
动态路由
"""


# http://127.0.0.1:8000/shop/detail/?sid=899
def detail(request):
    shop_id = request.GET.get('sid')
    if shop_id:
        try:
            # 返回列表套字典对象
            shops = Shop.objects.filter(shop_id=shop_id).values('shop_id',
                                                                'promote_price',
                                                                'original_price',
                                                                'stock', 'sub_title',
                                                                'name')

            if shops.exists():
                shop = shops.first()
                imgs = Image.objects.filter(shop_id=shop.get('shop_id')).values('shop_img_id', 'type')
                shop.update(imgs=imgs)
                values = PropertyValue.objects.filter(shop_id=shop_id)
                reviews = Review.objects.filter(shop_id=shop_id)
                return render(request, 'detail.html', {'shop': shop, 'values': values, 'reviews': reviews})
            # 一对一查询
            # 正向查询反向查询 都能查询出相关的子表数据
            #  user.userprofile.phone
            # userprofile.user.username
            # 一对多 查询
            #  正向查询 能查询出主表的相关数据
            #  反向查询
        except Exception as e:
            print(e)
            return render(request, 'error.html')

    return render(request, 'error.html')
