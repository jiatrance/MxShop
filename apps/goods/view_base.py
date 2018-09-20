from django.views.generic import View
from goods.models import Goods
import json
from django.core import serializers
from django.http import HttpResponse

class GoodsListView(View):
    def get(self,request):
        #通过django的view实现商品列表页
        json_list = []
        #获取所有商品
        goods = Goods.objects.all()
        # for good in goods:
        #     json_dict = {}
        #     #获取商品的每个字段，键值对形式
        #     json_dict['name'] = good.name
        #     json_dict['category'] = good.category.name
        #     json_dict['market_price'] = good.market_price
        #     json_list.append(json_dict)

        json_data = serializers.serialize('json',goods)
        json_data = json.loads(json_data)
        #返回json，一定要指定类型content_type='application/json'
        return HttpResponse(json.dumps(json_data,ensure_ascii=False),content_type='application/json;charset=utf-8')