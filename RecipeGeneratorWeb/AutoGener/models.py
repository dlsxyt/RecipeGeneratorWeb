from django.db import models

# Create your models here.

class DishType(models.Model):
    """The type of the dish. A dish can have multiple types."""
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class CanGet(models.Model):
    """ the ingredients user can get"""
    name = models.CharField(max_length=10)
    cal = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class CanDo(models.Model):
    """ the meal user can do"""
    # TYPE_CHOICES = (
    #     ('荤', '荤'),
    #     ('素', '素'),
    #     ('both', 'both'),
    #     ('暂不选择', '暂不选择'),
    #     ('主食', '主食')
    # )
    name = models.CharField(max_length=100)
    type = models.ManyToManyField(DishType)
    ingre = models.ManyToManyField(CanGet, blank=True)

    def __str__(self):
        return self.name


class Compose(models.Model):
    """the ingredient of a dish. A dish can have multiple ingredients."""
    dish = models.ForeignKey(CanDo, models.PROTECT)
    ingre = models.ForeignKey(CanGet, models.PROTECT)

    def __str__(self):
        return self.dish.name


