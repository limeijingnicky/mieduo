#开发环境的配置文件

"""
Django settings for meiduo project.

Generated by 'django-admin startproject' using Django 3.2.18.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--o=9vwhxwyag3y5%*f0fdgi)!%_0tyvu@=g=xqa#)7=4+f2b#f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users.apps.UsersConfig',

    # 注册过滤模块
    'django_filters',

    # 注册restframework
    'rest_framework',

    'classview.apps.ClassviewConfig',
    'booktest.apps.BooktestConfig',
]

##对全局的drf框架进行认证的设置
REST_FRAMEWORK = {
    ##权限设置
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',  ##基本认证
        'rest_framework.authentication.SessionAuthentication',  ##session认证
    ),
    ##流量设置，用户分类和频次
    'DEFAULT_THROTTLE_CLASSES': (
        # 'rest_framework.throttling.AnonRateThrottle',
        # 'rest_framework.throttling.UserRateThrottle',

        'rest_framework.throttling.ScopedRateThrottle',  # 对不同视图限制访问次数
    ),
    'DEFAULT_THROTTLE_RATES': {
        # 'anon': '1/day', ##匿名用户
        # 'user': '200/day', ##登录用户 second, minute,hour,day

        # 'bookview': '100000/day'
    },

    # 过滤filtering
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'],

    # 分页设置
    'DEFAULT_PAGINGATION_CLASS': (
        'django_filters.rest_framework.pagination.PageNumberPagination'),
    'PAGE_SIZE': 10,  # 设置每页数目

    ##更改异常捕捉方法
    # 'EXCEPTION_HANDLER': 'rest_framework.views.exception_handler', 默认的方法
    'EXCEPTION_HANDLER': 'exceptions.exception_handler',

    # api文档设置
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema'
}

##中间键用来监听 请求处理前  和 响应
##在请求处理之前从上而下执行，请求处理之后即响应是从下往上执行
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    ##注册中间键
    'middleware.my_middleware',
]

# 工程配置的路由文件入口
ROOT_URLCONF = 'meiduo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'environment':  'jinja2_env.environment',
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'meiduo.wsgi.application'

# Database 换成需要的数据库种类
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'POST': '3306',
        'USER': 'root',
        'PASSWORD': '1234',
        'NAME': 'meiduo'
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
# 静态文件访问路由前缀
STATIC_URL = '/static/'
# 配置静态文件加载存储目录
STATICFILES_DIRS = [

    os.path.join(BASE_DIR, 'static_files'),

]

##设置session的存储，使用redis存储，是一种高速存取的数据库，适用于键值对形式数据
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    "session": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "session"  ##普通缓存在default里的0, session缓存在session里的1 完成分库



##admin 管理网页里上传的图片储存的位置
MEDIA_ROOT = os.path.join(BASE_DIR, 'static_files/media')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

