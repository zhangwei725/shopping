from django.db.models import Q
from django.shortcuts import render

from apps.main.models import Shop, Image

"""
like
全文检索
"""


def search(request):
    if request.method == 'GET':
        kw = request.GET.get('keyword')
        # 或者 [{},{}]
        shops = Shop.objects \
            .filter(Q(name__contains=kw) | Q(sub_title__contains=kw)) \
            .values('shop_id', 'promote_price', 'name', 'sub_title')
        for shop in shops:
            #  [{},{}]
            img = Image.objects.filter(shop_id=shop.get('shop_id')).values('shop_img_id', 'type').first()
            shop.update(img=img)
        return render(request, 'page_search.html', {'shops': shops})
