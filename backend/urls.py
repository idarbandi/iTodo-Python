from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # مسیر مدیریت جنگو
    path("admin/", admin.site.urls),
    # مسیرهای مربوط به API
    path("api/", include("api.urls")),
    # مسیرهای مربوط به قسمت فرانت‌اند
    path("", include("frontend.urls")),
]
