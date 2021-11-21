from django.db import models
from django.urls import reverse
from embed_video.fields import EmbedVideoField
# from memberships.models import Membership
class Package(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    description = models.TextField()
    grade = models.IntegerField(default=6)
    # allowed_memberships = models.ManyToManyField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('courses:detail',kwargs={'grade':self.grade})

    @property
    def courses(self):
        return self.course_set.filter(grade=self.grade)


class Course(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    description = models.TextField()
    grade = models.IntegerField(default=6)
    package = models.ForeignKey(Package, on_delete=models.SET_NULL, null = True)

    # allowed_memberships = models.ManyToManyField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('courses:detail',kwargs={'grade':self.grade})

    @property
    def lessons(self):
        return self.lesson_set.all().order_by('position')


class Lesson(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null = True)
    position = models.IntegerField()
    # body = models.TextField(blank=True,null=True)
    url = EmbedVideoField(default='https://youtu.be/cdbJv7amERc')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('courses:lesson_detail',
            kwargs={
                'course_slug':self.course.slug,
                'lesson_slug':self.slug
                })
