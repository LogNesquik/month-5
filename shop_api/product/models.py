from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255) # Создаем поле


    def __str__(self):
        return self.name # выводим
    
    # Создаем обычную мету
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Product(models.Model):
    title = models.CharField(max_length=66) # Создаем поле названия
    description = models.TextField() # Создаем поле описания
    price = models.DecimalField(max_digits=10, decimal_places=2) # Создаем поле суммы
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products') # Создаем поле с катигорией

    def __str__(self):
        return self.title # Выводим
    

class Review(models.Model):
    text = models.TextField()# Создаем поле текста
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews') # Создаем отношение в БД Один к многим
    
    # Список звезд; P.s одно значение в БД другое на отображение
    choices = [
        (1, '⭐'),
        (2, '⭐⭐'),
        (3, '⭐⭐⭐'),
        (4, '⭐⭐⭐⭐'),
        (5, '⭐⭐⭐⭐⭐'),
    ]

    # Отображаем 
    stars = models.IntegerField(choices=choices, default=1, null=True)

    # выводим
    def __str__(self):
        return f'отзыв на {self.product.title}'