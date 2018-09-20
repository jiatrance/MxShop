from goods.serializers import GoodsSerializer
from .filters import GoodsFilter
from .models import Goods
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins,viewsets,generics,filters
from rest_framework.pagination import PageNumberPagination

class GoodsPagination(PageNumberPagination):
    '''
    商品列表自定义分页
    '''
    #默认每页显示的个数
    page_size = 10
    #可以动态改变每页显示的个数
    page_size_query_param = 'page_size'
    #页码参数
    page_query_param = 'page'
    #最多能显示多少页
    max_page_size = 100


class GoodsListView(generics.ListAPIView):
    '''
    商品列表
    '''
    pagination_class = GoodsPagination
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer


class GoodsListViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    '商品列表页'

    # 分页
    pagination_class = GoodsPagination
    #这里必须要定义一个默认的排序,否则会报错
    queryset = Goods.objects.all().order_by('id')
    serializer_class = GoodsSerializer

    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)

# 设置filter的类为我们自定义的类
    filter_class = GoodsFilter

    search_fields = ('=name','goods_brief')
#排序
    ordering_fields = ('sold_num', 'add_time')