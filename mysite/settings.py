"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 4.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-=i%nsj885*l1bxd-++*zd3f*zaewlx6n2)hlo*l$^zpwhc+=cb'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'multi_captcha_admin', #https://github.com/a-roomana/django-multi-captcha-admin
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize', #https://docs.djangoproject.com/en/4.2/ref/contrib/humanize/
    'django_extensions', #https://github.com/django-extensions/django-extensions?tab=readme-ov-file
    'django.contrib.sites', #https://docs.djangoproject.com/en/4.2/ref/contrib/sites/
    'django.contrib.sitemaps', #https://docs.djangoproject.com/en/4.2/ref/contrib/sitemaps/
    'robots', # https://pypi.org/project/django-robots/
    "debug_toolbar", #https://django-debug-toolbar.readthedocs.io/en/latest/installation.html 
    "taggit", # https://django-taggit.readthedocs.io/en/latest/getting_started.html 
    "django_summernote", # https://github.com/summernote/django-summernote 
    "captcha", #https://django-simple-captcha.readthedocs.io/en/latest/usage.html#installation
    
    # 'blog.apps.BlogConfig',
    'blog',
    'website',
    'jalali_date',#!https://pypi.org/project/django-jalali-date/
]

MULTI_CAPTCHA_ADMIN = {
    'engine': 'simple-captcha',
}

#! و آیدی شماره ۱ مراجعه میکند django_site برای اینکه بفهمه آدرس سایت من چیه؟....خب مستقیم به پایگاه داده 
SITE_ID = 1 #https://docs.djangoproject.com/en/4.2/ref/contrib/sites/

#https://django-robots.readthedocs.io/en/latest/#sitemaps
ROBOTS_USE_SITEMAP = True
# https://django-robots.readthedocs.io/en/latest/#host-directive
ROBOTS_USE_HOST = True

#!https://pypi.org/project/django-jalali-date/
#! default settings (optional)
JALALI_DATE_DEFAULTS = {
   # if change it to true then all dates of the list_display will convert to the Jalali.
   'LIST_DISPLAY_AUTO_CONVERT': False,
   'Strftime': {
        'date': '%y/%m/%d',
        'datetime': '%H:%M:%S _ %y/%m/%d',
    },
    'Static': {
        'js': [
            # loading datepicker
            'admin/js/django_jalali.min.js',
            # OR
            # 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.core.js',
            # 'admin/jquery.ui.datepicker.jalali/scripts/calendar.js',
            # 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.datepicker-cc.js',
            # 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.datepicker-cc-fa.js',
            # 'admin/js/main.js',
        ],
        'css': {
            'all': [
                'admin/jquery.ui.datepicker.jalali/themes/base/jquery-ui.min.css',
            ]
        }
    },
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        "DIRS": [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

SUMMERNOTE_CONFIG = {
    # Using SummernoteWidget - iframe mode, default
    'iframe': True,

    # Or, you can set it to `False` to use SummernoteInplaceWidget by default - no iframe mode
    # In this case, you have to load Bootstrap/jQuery sources and dependencies manually.
    # Use this when you're already using Bootstrap/jQuery based themes.
    # 'iframe': False,

    # You can put custom Summernote settings
    'summernote': {
        # As an example, using Summernote Air-mode
        'airMode': False,

        # Change editor size
        'width': '1000px',
        'height': '480',

        # Use proper language setting automatically (default)
        # 'lang': None,

        # Toolbar customization
        # https://summernote.org/deep-dive/#custom-toolbar-popover
        'toolbar': [
            ['style', ['style']],
            ['font', ['bold', 'underline', 'clear']],
            ['fontname', ['fontname']],
            ['color', ['color']],
            ['para', ['ul', 'ol', 'paragraph']],
            ['table', ['table']],
            ['insert', ['link', 'picture', 'video']],
            ['view', ['fullscreen', 'codeview', 'help']],
        ],
    } 
}

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

#! https://pypi.org/project/django-jalali-date/
#! (Optional) If you want the names of the dates to be displayed in Farsi, please add the following command to the settings.
# LANGUAGE_CODE = 'fa'
# import locale
# locale.setlocale(locale.LC_ALL, "Persian_Iran.UTF-8")

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'statics/'
STATIC_ROOT = BASE_DIR / 'statics'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media/'
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# ! چهار خط کد بالا به صورت پیش فرض برای اپ ها می باشد
# ! ولی خط زیر یعنی آقا علاوه بر ۴ خط کدبالا که ماله پیش فرض هست
# ! این دایرکتوری هایی که داخل لیست زیر برات نوشتم را نیز در نظر بگیر
# ! BASE_DIR / "static", الان یک مسیر گلوبال 
# ! براش تنظیم کردیم
STATICFILES_DIRS = [
    BASE_DIR / "static",
    # "/var/www/static/",
]
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

INTERNAL_IPS = [
    "127.0.0.1",
]

X_FRAME_OPTIONS = "SAMEORIGIN"