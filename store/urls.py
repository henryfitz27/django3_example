from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /store/product/5/
    path('product/<int:product_id>/', views.detail, name='product'),
]