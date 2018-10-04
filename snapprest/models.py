from django.db import models

class snappide(models.Model):
    paragraph=models.CharField(max_length=225)
    textfield=models.CharField(max_length=225)
    label=models.CharField(max_length=25)
    rating=models.IntegerField()
    switch=models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.paragraph)