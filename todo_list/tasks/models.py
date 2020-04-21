from django.db import models
# from django.contrib.auth.models import User

# Create your models here.
#capital is convention
#inherits features from model module
class Task(models.Model):
    title = models.CharField(max_length=50, unique=True)
    is_complete = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    # def snippet(self):
    #     if len(self.body) > 50:
    #         return self.body[:50] + "..."
    #     return self.body
