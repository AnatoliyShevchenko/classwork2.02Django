from django.db import models

# Create your models here.
class Pen(models.Model):
    """Class Pen."""

    INK_COLORS_PATTERN = (
        ('R','red'),
        ('G','green'),
        ('Y','yellow'),
        ('B','blue'),
        ('P','pink'),
        ('O','orange'),
        ('BL','black'),
        ('PU','purple'),
    )
    MATERIAL_PATTERNS = (
        ('I','IRON'),
        ('W','WOOD'),
        ('A','ACRIL'),
        ('R','RAGE'),
    )

    ink_color = models.CharField(
        choices=INK_COLORS_PATTERN,
        verbose_name='цвет чернил',
        max_length=20,
        default='blue'
    )
    material = models.CharField(
        choices=MATERIAL_PATTERNS,
        verbose_name='материал',
        max_length=20,
        default='ACRIL'
    )
    mass = models.IntegerField(
        verbose_name='масса изделия в граммах',
        default=50
    )
    size = models.IntegerField(
        verbose_name='длина изделия в сантиметрах',
        default=25
    )
    model = models.CharField(
        max_length=30,
        verbose_name='название модели изделия',
        unique=True
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'ручка'
        verbose_name_plural = 'ручки'

    def __str__(self) -> str:
        return self.model


class Stores(models.Model):
    """class for Pens Store."""

    title = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='склад'
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'склад'
        verbose_name_plural = 'склады'

    def __str__(self) -> str:
        return self.title


class Store(models.Model):
    """Pens Store."""

    store_title = models.ForeignKey(
        to=Stores,
        on_delete=models.CASCADE,
        verbose_name='склад'
    )
    count = models.IntegerField(
        verbose_name='колличество изделий',
    )
    product = models.ForeignKey(
        to=Pen,
        on_delete=models.CASCADE,
        verbose_name='продукт'
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'склад'
        verbose_name_plural = 'склады'

    def __str__(self) -> str:
        return self.store_title