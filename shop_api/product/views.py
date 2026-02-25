from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Product, Review
from .serializers import CategoryListSerializers, CategoryDetailSerializers, ProductListSerializers, ProductDetailSerializers
from .serializers import ReviewListSerializers, ReviewDetailSerializers
@api_view(['GET'])
def shop_list_category_view(request):
    # Вытаскиваем все объекты
    category = Category.objects.all()
    # Формотируем все объекты
    data = CategoryListSerializers(category, many=True).data
    # Отправляем все в json формате 
    return Response(data=data)

@api_view(['GET'])
def shop_detail_category_view(request, id):
    try:
        category_one = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(data={'error': 'not exsist this table'},
                        status=status.HTTP_404_NOT_FOUND)
    data = CategoryDetailSerializers(category_one).data
    return Response(data=data)

@api_view(['GET'])
def shop_list_product_view(request):
    product = Product.objects.all()
    data = ProductListSerializers(product, many=True).data
    return Response(data=data)

@api_view(['GET'])
def shop_detatil_product_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(data={'error': 'Не найден айди'})
    data = ProductDetailSerializers(product).data
    return Response(data=data)

@api_view(['GET'])
def shop_list_review_view(request):
    review = Review.objects.all()
    data = ReviewListSerializers(review, many=True).data
    return Response(data=data)

@api_view(['GET'])
def shop_detatil_review_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'Не найден айди'})
    data = ReviewDetailSerializers(review).data
    return Response(data=data)