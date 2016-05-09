from django.conf import settings


AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')
CREATED_BY = getattr(settings, 'CREATED_BY', 'created_by')
UPDATED_BY = getattr(settings, 'UPDATED_BY', 'updated_by')
CREATED_AT = getattr(settings, 'CREATED_AT', 'created_at')
UPDATED_AT = getattr(settings, 'UPDATED_AT', 'updated_at')
