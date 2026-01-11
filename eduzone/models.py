from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from django.db import migrations
from django_ckeditor_5.fields import CKEditor5Field
from django_ckeditor_5.widgets import CKEditor5Widget
from django.contrib.auth.models import User

# Class Course for home page courses
class Course(models.Model):
    title = models.CharField(max_length=200)
    rating = models.IntegerField()
    image = models.CharField(max_length=255, help_text="Path to image in static folder, e.g., 'images/courses/python.png'")
    linked_page = models.ForeignKey('PageCourse', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


# Class PageCourse for course page
class PageCourse(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True)
    rating = models.IntegerField()
    image = models.CharField(max_length=255, help_text="Path to image in static folder, e.g., 'images/courses/python.png'")
    content = CKEditor5Field(config_name='extends')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course_detail', kwargs={'slug': self.slug})

# class for adding member to show in about page
class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField()

    def __clstr__(self):
        return self.name

# class for making quiz    
class Quiz(models.Model):
    course = models.ForeignKey(PageCourse, on_delete=models.CASCADE, related_name='quizzes')
    title = models.CharField(max_length=200)

    def __str__(self):
        # return f"{self.course.title} - {self.title}"
        return f"{self.title}"

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    op1 = models.CharField(max_length=200)
    op2 = models.CharField(max_length=200)
    op3 = models.CharField(max_length=200)
    op4 = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)

# class for showing result
class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    total = models.IntegerField()
    percent = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)