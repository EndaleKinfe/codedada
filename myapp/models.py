from django.db import models

# Create your models here.

class Search(models.Model):
    searche = models.CharField(max_length=345)
    createdon = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.searche)

    class Meta:
        verbose_name_plural = "Searches"