from django.urls import path
from courses.views import CourseDetailView, LessonDetailView, PackageListView

app_name = 'courses'

urlpatterns = [
    path('', PackageListView.as_view(), name='package'),
    path('<int:grade>', CourseDetailView.as_view(), name='detail'),
    path('<course_slug>/<lesson_slug>',LessonDetailView.as_view(), name='lesson_detail')
]
