from django.shortcuts import render

from apps.main.models import Shop, ShopImage

"""
?
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
                imgs = ShopImage.objects.filter(shop_id=shop.get('shop_id')).values('shop_img_id', 'type')
                shop.update(imgs=imgs)
                return render(request, 'detail.html', {'shop': shop})
        except Exception as e:
            print(e)
    else:
        pass
        # return render(request, 'detail.html')
