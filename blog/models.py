from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Ignore Below import if it displays an errorin VScode
from ckeditor.fields import RichTextField

# Create your models here.


#This is the main blog post model that handles all things related to posts
class Post(models.Model):
    intro_image = models.ImageField(null=True, blank=True, upload_to="images/")
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    snippet = models.CharField(max_length=200)
    body = RichTextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.title + '|' + ' ' + str(self.author) + ' ' + '|' + str(self.date_added)

    class Meta:
        ordering = ['-date_added']  

    def get_absolute_url(self):
        return reverse('article_detail', args=[self.id])



#This model handles all making a new category and submiting it to the database
class Category(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse('category', args=[self.category_name])


#This model handels the Subscribe feature in the blg
class Subscribe(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse('homepage')