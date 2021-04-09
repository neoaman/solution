from django.apps import AppConfig
from pymongo import MongoClient

class ToolkitConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'toolkit'
