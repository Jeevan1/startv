from django.db import models

from utils.model_mixins import BaseModel

# Create your models here.

class MenuItems(BaseModel):
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

class Article(BaseModel):
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to='images/')
    # author = models.CharField(max_length=100)


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
    