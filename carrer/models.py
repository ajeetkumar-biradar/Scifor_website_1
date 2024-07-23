from django.db import models
from django.db.models.base import ModelState
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
import pandas as pd


# Create your models here.
class Jobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    position = models.CharField(max_length=500)
    location = models.CharField(max_length=500)
    jobType = models.CharField(max_length=500)
    openings = models.IntegerField()
    experiences = models.CharField(max_length=500)
    educationLevel = models.CharField(max_length=500, null=True)
    description = models.CharField(max_length=6000)
    requirements = models.TextField(max_length=6000)

    def __str__(self):
        return self.position


class Application(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    mob = models.CharField(max_length=10)
    mailID = models.CharField(max_length=50)
    resume = models.FileField(upload_to="resume/")


class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    job = models.CharField(max_length=255, blank=True, null=True)  # Job title
    linkedin = models.URLField(max_length=255, blank=True, null=True)  # LinkedIn profile URL
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    testimonial = models.TextField()

    def __str__(self):
        return self.name


class CaseStudy(models.Model):
    case_study = models.TextField()
    short_desc = models.TextField(max_length=500, blank=True, null=True)  # Adding Short Description field
    short_description = models.TextField(max_length=500, blank=True, null=True)  # Adding Short Description field
    description = models.TextField()
    image = models.ImageField(upload_to='case_study/', blank=True, null=True)

    def __str__(self):
        return self.case_study


class Article(models.Model):
    TECH_BLOGS = 'TECH BLOGS'
    TECH_NEWS = 'TECH NEWS'
    INDUSTRY_UPDATES = 'INDUSTRY UPDATES'

    CATEGORY_CHOICES = [
        (TECH_BLOGS, 'Tech Blogs'),
        (TECH_NEWS, 'Tech News'),
        (INDUSTRY_UPDATES, 'Industry Updates'),
    ]

    title = models.TextField()
    content = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default=TECH_BLOGS)
    headline_image = models.ImageField(upload_to='articles/')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])
