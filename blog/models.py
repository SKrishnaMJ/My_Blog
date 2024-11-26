from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email_address = models.EmailField()

    def fullname(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.fullname()


class Tag(models.Model):
    caption = models.CharField(max_length=150)

    def __str__(self):
        return self.caption


class Post(models.Model):
    slug = models.SlugField(max_length=20, unique=True, db_index=True)
    title = models.CharField(max_length = 150)
    image_name = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=200)
    content = models.TextField(validators=[MinLengthValidator(10)])
    date = models.DateField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.title}"
