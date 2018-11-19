from django.urls import path
from api2 import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login_jwt/', obtain_jwt_token),
    path('login/',views.login),
    path('students/', views.GenericStudentList.as_view()),
    path('students/<int:student_id>/', views.GenericStudentDetail.as_view())

    # path('post/comments/', views.CommentCreate.as_view()),
    # path('post/<int:post_id>/comments/', views.CommentDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)


