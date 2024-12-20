from django.db import models

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=255)
    born_date = models.DateField(null=True, blank=True)
    born_location = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.fullname}'

class Tag(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)

    def __str__(self):
        return f"{self.name}"

class Quote(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    quote = models.TextField()
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f'{self.quote}'
