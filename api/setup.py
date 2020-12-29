from setuptools import find_packages, setup

run_requirements = [
    'requests==2.25.1',
    'beautifulsoup4==4.9.3',
    'celery==5.0.5',
    'starlette==0.13.6',
    'pydantic==1.7.3',
    'fastapi==0.63.0',
    'uvicorn[standard]==0.13.2',
    'gunicorn==20.0.4',
    'mysqlclient==1.4.6',
    'SQLAlchemy==1.3.22',
]

setup(
    name="pricemonitoring",
    version='1.0.0',
    author="Matheus Sena Vasconcelos",
    author_email="sena.matheus14@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=run_requirements,
    python_requires='>=3.9',
)