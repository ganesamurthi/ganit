from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from courses.models import Course, Lesson, Package

class PackageListView(ListView):
    model = Package


class CourseDetailView(View):

    def get(self,request,grade, *args, **kwargs):

        course_qs = Course.objects.filter(grade=grade)
        if course_qs.exists():
            context = {
                'object' : course_qs
            }
        return render(request,"courses/course_detail.html",context)

class LessonDetailView(View):

    def get(self, request, course_slug, lesson_slug, *args, **kwargs):

        course_qs = Course.objects.filter(slug=course_slug)
        if course_qs.exists():
            course = course_qs.first()

        lesson_qs = course.lessons.filter(slug=lesson_slug)
        if lesson_qs.exists():
            lesson = lesson_qs.first()

        context ={
            'object':lesson
        }

        return render(request,"courses/lesson_detail.html",context)
