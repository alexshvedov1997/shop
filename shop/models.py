from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length= 250, verbose_name="Название категории", unique=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ("name", )

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete= models.CASCADE, related_name="products", verbose_name="Категория")
    name = models.CharField(max_length=250, verbose_name="Название товара")
    slug = models.SlugField(unique=True, verbose_name="Слаг")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places= 2, verbose_name="Цена")
    available = models.BooleanField(default=False, verbose_name="В наличии")
    created = models.DateTimeField(auto_now=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now_add=True, verbose_name="Дата обновления")
    product_image = models.ImageField(upload_to = "products", blank = True, verbose_name="Изображение")

    class Meta:
        ordering = ("name",)
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def get_absolute_url(self):
        return reverse('detail', args=[self.id, self.slug])



