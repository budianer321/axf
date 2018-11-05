from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^home/$', views.home, name='home'),  # 首页
    url(r'^cart/$', views.cart, name='cart'),   # 购物车
    url(r'^market/(\d+)/(\d+)/(\d+)/$', views.market, name='market'),  #闪购超市
    url(r'^mine/$', views.mine, name='mine'),   # 我的
    url(r'^base/$', views.base, name='base'),   # 我的
]
