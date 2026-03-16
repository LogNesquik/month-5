from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product import views

router = DefaultRouter()
router.register(
    'categories', views.ShopListCategoryView
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/categories/', views.shop_list_category_view), # GET - list, POST - create
    path('api/v1/categories/<int:id>/', views.shop_detail_category_view),
    path('api/v1/products/', views.shop_list_product_view),
    path('api/v1/products/<int:id>/', views.shop_detatil_product_view),
    path('api/v1/reviews/', views.shop_list_review_view),
    path('api/v1/reviews/<int:id>/', views.shop_detatil_review_view),
    path('api/v1/products/reviews/', views.shop_products_with_reviews_view),
    path('api/v2/', include(router.urls)),    
]
