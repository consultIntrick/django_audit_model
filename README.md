# django_audit_model

django_audit_model audits the user activity on all the records in a django model

# Installation

- Put 'audit_model' in your INSTALLED_APPS setting.
- Run the command manage.py makemigrations followed by manage.py migrate.
- Add audit_model.middleware.AuditUserMiddleware to MIDDLEWARE_CLASSES.

# Detailed documentation

For a detailed documentation of django_audit_model refer: [django_audit_model documentation](https://django_audit_model.intrick.com)