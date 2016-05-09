from setuptools import setup

setup(
    name='django_audit_model',
    version='0.1',
    description='django_audit_model audits the user activity on all the records in a django model',
    author='Jagadesh Babu T',
    author_email='jagadesh@intrick.com',
    packages=['audit_model'],
    install_requires=['django>=1.7'],
    license="MIT",
    keywords="django audit_model auditing_model model_auditing model_audit",
    url="https://github.com/consultIntrick/django_audit_model",
)
