from rest_framework import serializers
from .models import Category, Product, Review

# Создаем класс категори деталей, чтобы вывести все значения в json формате
class CategoryDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

# Создаем класс CategoryListSerializers, чтобы вывести все значения в json формате
class CategoryListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

# Создаем класс ProductListSerializers, чтобы вывести все значения в json формате
class ProductListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

# Создаем класс ProductDetailSerializers, чтобы вывести все значения в json формате
class ProductDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

# Создаем класс ReviewListSerializers, чтобы вывести все значения в json формате
class ReviewListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

# Создаем класс ReviewDetailSerializers, чтобы вывести все значения в json формате
class ReviewDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

# Создаем класс ReviewSerializers, чтобы вывести значения id text product stars в json формате
class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id text product stars']

# Создаем класс ReviewSerializers, чтобы вывести все значения в json формате
class ProductWithReviewsSerializer(serializers.ModelSerializer):
    # Проходимся по каждому айди, тексту, продукту, отзыву, чтобы зафиксировать это в БД
    reviews = ReviewSerializers(many=True)
    # Когда запросят запрос - создатся, до этого по просту этой переменной нету. Нужен чтобы не хранить пустый бессконечный рейтинг
    # Проще говоря, создался - сделал - ушел
    average_rating = serializers.SerializerMethodField()

    # Обычный класс мета
    class Meta:
        model = Product
        fields = ['__all__']

    # функция для получения среднего значения
    def get_average_rating(self, obj):
        # Получаем все отзывы по данную значению
        reviews = obj.reviews.all()
        # Делаем проверку, если есть значение
        if reviews:
            # Возвращаем среднее арифмитическое
            # sum - суммирует, внутри цикл генерирует списки, и проходит по всем спискам, после делим на все отзывы
            return sum(review.stars for review in reviews) / len(reviews)
        # иначе вернем - ничего
        return None
