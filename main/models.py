from django.db import models


# Create your models here.
class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimeStamp):
    name = models.CharField(max_length=212)

    def __str__(self):
        return self.name


class Tag(TimeStamp):
    name = models.CharField(max_length=212)

    def __str__(self):
        return self.name


class Author(TimeStamp):
    name = models.CharField(max_length=212)
    image = models.ImageField(upload_to='authors')
    profession = models.CharField(max_length=212)
    description = models.TextField()

    def __str__(self):
        return self.name


class Post(TimeStamp):
    title = models.CharField(max_length=212)
    image = models.ImageField(upload_to='posts')
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class Extra_info(TimeStamp):
    name = models.CharField(max_length=212)
    description = models.TextField()

    def __str__(self):
        return self.name


class About(TimeStamp):
    title = models.CharField(max_length=212)
    body = models.TextField()
    image = models.ImageField(upload_to='about')
    video = models.URLField()
    extra_info = models.ManyToManyField(Extra_info)

    def __str__(self):
        return self.title


class HappyClients(TimeStamp):
    name = models.CharField(max_length=212)
    profession = models.CharField(max_length=212)
    image = models.ImageField(upload_to='clients')
    description = models.TextField()

    def __str__(self):
        return self.name


class Comment(TimeStamp):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=212)
    email = models.EmailField()
    website = models.URLField()
    message = models.TextField()
    image = models.ImageField(upload_to='comment_author')
