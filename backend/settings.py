"""
*********************************************************************
*                                                                   *
*                           🗒️ iTodo                                *
*                                                                   *
*        یک برنامه لیست کارهای ساده و موثر که با جنگو و              *
*            جاوااسکریپت خالص ساخته شده است 📋🚀                    *
*                                                                   *
*     تولید کننده: idarbandi                                        *
*     ایمیل: darbandidr99@gmail.com                                 *
*     گیت‌هاب: https://github.com/idarbandi/iTweet                  *
*                                                                   *
*********************************************************************
"""

import os

# ساخت مسیرها در داخل پروژه مانند این: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# تنظیمات توسعه سریع - نامناسب برای تولید
# مشاهده https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# هشدار امنیتی: کلید مخفی استفاده شده در تولید را مخفی نگه دارید!
SECRET_KEY = "2)&r5g1*=8bwjgp!pm7sjq3b*k^ukq4l0%+(af$y279p1m$7q_"

# هشدار امنیتی: در تولید با حالت debug روشن اجرا نکنید!
DEBUG = True

ALLOWED_HOSTS = []


# تعریف برنامه‌ها

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # برنامه‌های داخلی
    "api.apps.ApiConfig",
    "frontend.apps.FrontendConfig",
    # برنامه‌های خارجی
    "rest_framework",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "backend.wsgi.application"


# تنظیمات پایگاه داده
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

# if you are willing to use postgresql

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'todo_db',
#         'USER': 'todo_user',
#         'PASSWORD': 'secret',
#         'HOST': 'db',
#         'PORT': 5432,
#     }
# }


# اعتبارسنجی رمز عبور
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# بین‌المللی سازی
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# فایل‌های استاتیک (CSS، JavaScript، تصاویر)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = "/static/"
