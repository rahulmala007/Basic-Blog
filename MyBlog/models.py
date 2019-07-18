from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title=models.CharField(max_length=20)
    text=models.TextField()
    create_date=models.DateTimeField(default=timezone.now)
    publish_date=models.DateTimeField()

    def publish(self):
        self.publish_date=timezone.now()
        self.save()

    def __str__(self):
        return "%s--%s"% (self.author,self.title)