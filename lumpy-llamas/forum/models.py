from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Thread(models.Model):
    start_date = models.DateTimeField('Date created', auto_now_add=True)
    title = models.CharField(max_length=120)

    def __str__(self):
        return self.title


class ThreadMessage(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET("Deleted"))
    date = models.DateTimeField('Date created', auto_now_add=True)
    message = models.TextField()

    def __str__(self):
        return (f'Message by {self.user} created {self.date} | '
                f'{self.message}'
                )
