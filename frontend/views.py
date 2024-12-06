from django.shortcuts import render

# ویوهای خود را در اینجا ایجاد کنید.


# ویوی list برای رندر کردن قالب list.html
def list(request):
    return render(request, "frontend/list.html")
