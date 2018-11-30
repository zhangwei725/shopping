import os

# 项目根目录
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# 加密秘钥
SECRET_KEY = '4i4o+f=f=n^om&*u%956_!@4!bhwn^%_bep*%*451s(e!=09+0'
# 开发模式(上线设置为False)
DEBUG = True
# 允许访问的ip地址(上线需要配置)
ALLOWED_HOSTS = []
# 注册app
SYS_APPS = ['django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            ]
# 第三方的模块注册
EXT_APPS = [
    # 必要组件
    'xadmin',
    'crispy_forms',
    # 非必要,主要用于修改主题样式
    'reversion',
    'django_ajax',
]

# 自定义功能模块注册
CUSTOM_APPS = [
    'apps.account',
    'apps.cate',
    'apps.detail',
    'apps.main',
    'apps.search',
    'apps.cart',
]

INSTALLED_APPS = SYS_APPS + EXT_APPS + CUSTOM_APPS
# 中间注册
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# 根路由配置 一般不需要修改
ROOT_URLCONF = 'shopping.urls'

# 模板配置
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            # 模板全局变量配置
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
# 启动应用程序配置(一般不需要修改)
WSGI_APPLICATION = 'shopping.wsgi.application'
# 数据配置
DATABASES = {
    # 默认数据配置(可以配置多个)
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'shopping',
        'USER': 'root',
        'PASSWORD': 'root',
    }
}

# 用户密码验证配置(一般不需要修改)
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
# 语言配置(开发中设置成中文)
LANGUAGE_CODE = 'zh-hans'
# 时区设置 设置成中国时区
TIME_ZONE = 'Asia/Shanghai'
# 国际化配置,自动转化多个语言
USE_I18N = True

USE_L10N = True
# 开启django时区 如果不需要django时区可以设置成False(建议设置成False)
USE_TZ = False
# 访问静态文件的路径配置
STATIC_URL = '/static/'
# 配置静态文件整理的根目录
STATIC_ROOT = 'static_root'
# 静态文件目录配置
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'apps/main/static'),
    os.path.join(BASE_DIR, 'apps/cart/static'),
)
# 配置访问多媒体的路径
MEDIA_URL = '/media/'
# 配置文件上传的目录
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

AUTH_USER_MODEL = 'main.User'
LOGIN_URL = '/account/login/'
# ========== 缓存的配置=========
# pip install django-redis
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        # 缓存地址
        "LOCATION": "redis://112.74.42.138:6379",
        "OPTIONS": {
            # 'PASSWORD':123
            # 使用线程池管理连接
            "CONNECTION_POOL_KWARGS": {"max_connections": 100}
        }
    },
    'session': {
        'BACKEND': 'django_redis.cache.RedisCache',
        # 缓存地址
        "LOCATION": "redis://112.74.42.138:6379/3",
        "OPTIONS": {
            # 'PASSWORD':123
            # 使用线程池管理连接
            "CONNECTION_POOL_KWARGS": {"max_connections": 100}
        }
    },
}

# ========SESSION 缓存配置======
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "session"

# session失效的时间 7天
SESSION_COOKIE_AGE = 7 * 24 * 60 * 60  # Session的cookie失效日期（2周） 默认1209600秒

# =======邮件配置=======
EMAIL_HOST = 'smtp.163.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = '18614068889@163.com'
EMAIL_HOST_PASSWORD = 'py1805'
EMAIL_USE_TLS = True

# =======日志配置=======
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG',
        },
    }
}
