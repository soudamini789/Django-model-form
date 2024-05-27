from django.db import models

# Create your models here.
class topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.topic_name    

class webpage(models.Model):
    topic_name=models.ForeignKey(topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    creater=models.CharField(default='mini',max_length=11)

    def __str__(self):
        return self.name    

class AccessRecords(models.Model):
    name=models.ForeignKey(webpage,on_delete=models.CASCADE)
    date=models.DateField()
    author=models.CharField(max_length=100)
    type=models.CharField(default='a', max_length=50)

    def __str__(self):
        return self.author

