from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Rooms(models.Model):
    name = models.CharField(max_length=100)
    online = models.ManyToManyField(User, blank=True)

    def get_online_count(self):
        return self.online.count()

    def join(self, user):
        self.online.add(user)
        self.save()

    def leave(self, user):
        self.online.remove(user)
        self.save()

    def __str__(self):
        return self.name


class Messages(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.user.username}: {self.content}: [{self.timestamp}]'