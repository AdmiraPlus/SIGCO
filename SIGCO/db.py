# Archivo de configuración de Bases de Datos.

from pathlib import Path
from os import getenv
from dotenv import load_dotenv


# Cargar las variables de entorno del archivo .env
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# Configuración para SQLite:
SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

MySQL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'HOST': getenv('HOST'),
		'PORT': getenv('PORT'),
		'NAME': getenv('DATABASE_NAME'),
        'USER': getenv('USER_DB'),
        'PASSWORD': getenv('PASS_UDB'),
    }
}