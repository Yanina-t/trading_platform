from django.db import models

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название продукта')
    model = models.CharField(max_length=50, verbose_name='Модель')
    release_date = models.DateField(verbose_name='Дата выпуска на рынок')

    def __str__(self):
        return self.model


class Suppliers(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название объекта сети')
    email = models.EmailField(verbose_name='Email')
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    house_number = models.CharField(max_length=20, verbose_name='Номер дома')
    products = models.ManyToManyField(Product, verbose_name='Продукты')
    supplier = models.ForeignKey('self', on_delete=models.CASCADE, **NULLABLE,
                                      verbose_name='Поставщик объекта сети')
    debt_to_supplier = models.DecimalField(max_digits=20, decimal_places=2, default=0, verbose_name='Задолженность')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    level = models.IntegerField(default='Empty', editable=False, verbose_name='Уровень')  # Поле для хранения уровня

    def save(self, *args, **kwargs):
        """Переопределение метода save() для обновления уровня при сохранении"""
        if self.supplier is None:
            # Узел верхнего уровня (например, завод)
            self.level = 0
        else:
            # Узел подчиненного уровня (уровень предыдущего узла + 1)
            self.level = self.supplier.level + 1
            if self.level >2:
                raise ValueError('Ошибка в уровнях, всего возможно 3 Уровня иерархии (0,1,2)')
                self.level = new_level
        super(Suppliers, self).save(*args, **kwargs)  # Сохранение объекта

    def __str__(self):
        """
        Возвращает строковое представление поставщика.
        """
        return self.name

    class Meta:
        verbose_name = 'Объект сети'
        verbose_name_plural = 'Объекты сети'


class Employee(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
