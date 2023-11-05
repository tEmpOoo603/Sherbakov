from django.db import models

class Applications(models.Model):
    class Status(models.TextChoices):
        AWAITING = "В ожидании","В ожидании"
        COMPLETED = "Выполнено","Выполнено"
        CANCELED = 'Отменено','Отменено'

    name = models.CharField(max_length=100, verbose_name='Имя клиента')
    phone = models.CharField(max_length=11, verbose_name='Телефон')
    email = models.EmailField(max_length=100, blank=True, verbose_name='Почта')
    comment = models.TextField(max_length=500, blank=True, verbose_name='Комментарий')
    create_time = models.DateTimeField(auto_now=True, verbose_name='Дата создания заявки')
    status = models.TextField(choices=Status.choices, default=Status.AWAITING, blank=True, verbose_name='Статус')

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-create_time']

