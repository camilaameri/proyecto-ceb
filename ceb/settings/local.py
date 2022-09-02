from .base import*


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-0)ba@)^-548+ozky_3e2mj+8bcp15fxz_71d-1^=vetot^!no='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

'''
DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME':'TPFINAL',
        'Trusted_Connection':'yes',
        'HOST': 'localhost',
        'OPTIONS':{
            'driver':'SQL Server Native Client 11.0',
        }
    },
}
'''