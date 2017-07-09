from django.db import models

class Chat(models.Model):
    unique_name = models.CharField(unique=True,max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.unique_name

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)




