from django.db import models


class Category(models.Model):
    name = models.CharField(unique=True, max_length=32)
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


class Equipment(models.Model):

    class Meta:
        unique_together = ('name', 'category',)

    name = models.CharField(max_length=64)
    # CASCADE, SET_NULL, PROTECTED
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_own_shop = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}/{self.category}'