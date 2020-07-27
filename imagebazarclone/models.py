from django.db import models

# Model for categories.
class Categories(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.title



class Images(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True)
    tags = models.CharField(max_length=100)
    image = models.ImageField(upload_to='imagebazarclone/images/')
    add_date = models.DateTimeField(auto_now_add=True)
    cat = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
