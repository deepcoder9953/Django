from django.contrib import admin
from django.urls import path, include
from web.views import StudentView



urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('web/', include('web.urls'))
     path('students/', StudentView.as_view(), name='student_list'),
]
