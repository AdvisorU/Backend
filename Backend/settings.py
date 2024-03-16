"""
Django settings for Backend project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

from dotenv import load_dotenv
load_dotenv()
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # RESTful
    'rest_framework',
    'rest_framework_simplejwt',
    # CORS
    'corsheaders', 
    # EventStream
    # 'django_eventstream',
    # Model
    'Backend.models',
]

MIDDLEWARE = [
    # CORS
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # JWT
    'Backend.middlewares.jwt_auth.JWTAuthenticationMiddleware', 
]

ROOT_URLCONF = 'Backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'Backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 数据库引擎
        'NAME': os.environ.get('MYSQL_DATABASE'),  # 数据库名称
        'HOST': os.environ.get('MYSQL_HOST'),  # 数据库地址
        'PORT': int(os.environ.get('MySQL_PORT')),  # 端口
        'USER': os.environ.get('MYSQL_USER'),  # 数据库用户名
        'PASSWORD': os.environ.get('MYSQL_PASSWORD'),  # 数据库密码
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

LANGUAGE_CODE = 'zh-cn'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'models.User'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'EXCEPTION_HANDLER': 'Backend.handlers.exception_handler.custom_exception_handler', 
}

# JWT

SIMPLE_JWT = {
    'AUTH_COOKIE': 'Session-ID',  # 设置 JWT 存储在 Cookie 中的名称
    #'AUTH_COOKIE_SECURE': True,  # 仅在 HTTPS 连接下传输 Cookie
    #'AUTH_COOKIE_SECURE': True,  # 仅在 HTTPS 连接下传输 Cookie
    #'AUTH_COOKIE_SAMESITE': 'Lax',  # 限制跨站点请求
    'AUTH_COOKIE_SECURE': False,  # 仅在 HTTPS 连接下传输 Cookie
    'AUTH_COOKIE_SECURE': False,  # 仅在 HTTPS 连接下传输 Cookie
    'AUTH_COOKIE_SAMESITE': 'None',  # 限制跨站点请求
    'AUTH_HEADER_TYPES': ('SessionID'),
}

# CORS

CORS_ORIGIN_WHITELIST = (
    'http://localhost:8081',
    'http://localhost:5173', 
    'https://advisoru.binrz.com'
)

CORS_ALLOW_CREDENTIALS = True  # 允许携带cookie

# Snowflake

SNOWFLAKE = {
    'WORKER_ID': int(os.environ.get('SNOWFLAKE_WORKER_ID')),
    'DATACENTER_ID': int(os.environ.get('SNOWFLAKE_DATACENTER_ID')),
}

# Langchain

from Backend import langchain
langchain.init()
