from django.db import models


class TimestampMixin(models.Model):
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def get_timestamp(self):
        print(self.create, self.update)

    class Meta:
        abstract = True

class Category(TimestampMixin):
    name = models.CharField(unique=True, max_length=32)
    is_active = models.BooleanField(default=True)
    # 1. Blob (Bites), 2. На диске
    img = models.ImageField(upload_to='category', blank=True, null=True)

    # models.IntegerField
    # models.TextField
    # models.FloatField
    # models.BooleanField
    # models.JSONField
    # models.DecimalField
    # models.DateField
    # models.DateTimeField
    # models.TimeField
    # models.EmailField
    # models.URLField
    # models.SlugField
    # models.BinaryField
    # models.ImageField
    # models.TextField
    def __str__(self):
        return self.name


class Product(models.Model):
    # cost = models.DecimalField
    cost = models.PositiveIntegerField(default=1)
    name = models.CharField(max_length=64)

# Оборудование ЯВЛЯЕТСЯ Товаром ?
class Equipment(Product, TimestampMixin):

    # class Meta:
    #     unique_together = ('name', 'category',)

    # CASCADE, SET_NULL, PROTECTED
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_own_shop = models.BooleanField(default=False)

    def buy(self):
        print('Вы купили', self.name)

    def __str__(self):
        return f'{self.name}/{self.category}'


class DebugEquipment(Equipment):

    class Meta:
        proxy = True

    def buy(self):
        print(self.create)
        super().buy()
        print(self.update)


class Excursion(Product, TimestampMixin):
    days_count = models.PositiveIntegerField(default=1)