from django.db import models

STATUS_CHOICES = [('Active', 'Активно'), ('Blocked', 'Заблокировано')]


class GuestBook(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="Имя автора")
    email = models.EmailField(max_length=50, null=False, blank=False, verbose_name="Почта")
    text = models.TextField(max_length=2000, null=False, blank=False, verbose_name="Текст Записи")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="Active", verbose_name="Статус")

    def __str__(self):
        return f"{self.pk} {self.title} {self.email} {self.status}"

    class Meta:
        db_table = "GuestBook"
        verbose_name = "Запись"
        verbose_name_plural = "Записи"

