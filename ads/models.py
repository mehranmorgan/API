from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


class Ad(models.Model):
    date_add = models.DateTimeField(default=now)
    title = models.CharField(max_length=30)
    caption = models.TextField()
    image = models.ImageField(upload_to='media')
    is_publish = models.BooleanField(default=False, help_text='it will ad when check')
    publisher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ad')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-date_add',)
        get_latest_by = 'date_add'
