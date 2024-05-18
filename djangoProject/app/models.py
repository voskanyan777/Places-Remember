from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class UserImage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    image = models.TextField(verbose_name="ссылка на изображение")

    class Meta:
        db_table = 'user_image'
        verbose_name = "Изображение пользователя"
        verbose_name_plural = "Изображении пользователей"

    def __str__(self):
        return str(self.user.username)


class Place(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False, verbose_name="Название посещенного места" )
    description = models.CharField(max_length=400, blank=False, null=False, verbose_name="Описание посещенного места")
    longitude = models.FloatField(null=False, blank=False, verbose_name="Широта посещенного места")
    latitude = models.FloatField(null=False, blank=False, verbose_name="Долгота посещенного места")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")

    class Meta:
        db_table = 'place'
        verbose_name = "Посещенное место"
        verbose_name_plural = "Посещенные места"