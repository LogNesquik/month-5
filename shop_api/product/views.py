from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Product, Review
from .serializers import CategoryListSerializers, CategoryDetailSerializers, ProductListSerializers, ProductDetailSerializers
from .serializers import ReviewListSerializers, ReviewDetailSerializers

@api_view(['GET'])
def shop_products_with_reviews_view(request):
    products = Product.objects.prefetch_related('reviews').all()
    
    result = []
    for product in products:
        reviews = product.reviews.all()
        
        if reviews:
            average_rating = sum(review.stars for review in reviews) / len(reviews)
            average_rating = round(average_rating, 1)
        else:
            average_rating = None
        
        reviews_data = ReviewListSerializers(reviews, many=True).data
        product_data = ProductListSerializers(product).data
        
        product_data['reviews'] = reviews_data
        product_data['average_rating'] = average_rating
        
        result.append(product_data)
    
    return Response(data=result)


@api_view(['GET'])
def shop_list_category_view(request):
    # Вытаскиваем все объекты
    category = Category.objects.all()
    # Формотируем все объекты
    data = CategoryListSerializers(category, many=True).data
    for i, cat in enumerate(category):
        data[i]['products_count'] = cat.products.count()
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
    data['products_count'] = category_one.products_count
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