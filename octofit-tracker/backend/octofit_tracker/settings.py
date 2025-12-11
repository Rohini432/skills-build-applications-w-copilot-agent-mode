# Django settings for octofit_tracker project

INSTALLED_APPS = [
    'octofit_tracker',
    'rest_framework',
    'djongo',
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = ['*']
CORS_ALLOW_METHODS = ['*']
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'octofit_db',
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
            'host': 'localhost',
            'port': 27017,
            'username': '',
            'password': '',
            'authSource': '',
        },
    }
}

ROOT_URLCONF = 'octofit_tracker.urls'
