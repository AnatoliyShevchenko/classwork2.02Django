from django.db import models

# Create your models here.
class Color(models.Model):
    """Create color for pen."""

    color = models.CharField(
        verbose_name='цвет чернил',
        max_length=20,
    )
    color_title = models.CharField(
        verbose_name='название цвета',
        max_length=20,
    )


    class Meta:
        ordering = ('-id',)
        verbose_name = 'цвет'
        verbose_name_plural = 'цвета'

    def __str__(self) -> str:
        return self.color_title


class Pen(models.Model):
    """Class Pen."""

    MATERIAL_PATTERNS = (
        ('I','IRON'),
        ('W','WOOD'),
        ('A','ACRIL'),
        ('R','RAGE'),
    )

    ink_color = models.ManyToManyField(
        to=Color,
        verbose_name='цвет чернил',
    )
    material = models.CharField(
        choices=MATERIAL_PATTERNS,
        verbose_name='материал',
        max_length=20,
    )
    mass = models.PositiveIntegerField(
        verbose_name='масса изделия в граммах',
        default=50
    )
    size = models.PositiveIntegerField(
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
        blank=True,
        verbose_name='склад'
    )


    class Meta:
        ordering = ('-id',)
        verbose_name = 'склад'
        verbose_name_plural = 'склады'

    def __str__(self) -> str:
        return self.title


class StoreConfig(models.Model):
    """Pens Store."""

    store_title = models.ForeignKey(
        to=Stores,
        on_delete=models.CASCADE,
        blank=True,
        verbose_name='склад'
    )
    count = models.PositiveIntegerField(
        verbose_name='колличество изделий',
        blank=True
    )
    product = models.ForeignKey(
        to=Pen,
        on_delete=models.CASCADE,
        verbose_name='продукт',
        blank=True
    )


    class Meta:
        ordering = ('-id',)
        verbose_name = 'склад'
        verbose_name_plural = 'склады'

    def __str__(self) -> str:
        return self.store_title