from django.db import models
from django.contrib.auth.models import User
from utils.model_mixins import BaseModel
from ckeditor.fields import RichTextField

# Create your models here.

class MenuItem(BaseModel):
    HEADER = 'header'
    FOOTER = 'footer'
    SIDEBAR = 'sidebar'

    POSITION_CHOICES = (
        (HEADER, 'Header'),
        (FOOTER, 'Footer'),
        (SIDEBAR, 'Sidebar'),
    )

    label = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    position = models.CharField(max_length=20, choices=POSITION_CHOICES , default=HEADER)

    def __str__(self):
        return self.label

class Category(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

class Author(BaseModel):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='images/author/', null=True, blank=True)

    def __str__(self):
        return self.user.username

class Article(BaseModel):
    title = models.CharField(max_length=255)
    content = RichTextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, related_name='articles')
    featured_image = models.ImageField(upload_to='images/')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
    
class Contact(BaseModel):
    name = models.CharField(max_length=100, )
    email = models.EmailField(null=True, blank=True)
    subject = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    message = models.TextField()

    def __str__(self):
        return self.name
    