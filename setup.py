from setuptools import setup, find_packages
import os

version = '0.2.2'

setup(
    name='emencia.django.countries',
    version=version,
    description='List of manageable countries for your Django projects',
    long_description=open('README.rst').read() + '\n' +
                    open('HISTORY.rst').read(),
    keywords='django, countries',
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.4',
        'Framework :: Django :: 1.5',
        'Framework :: Django :: 1.6',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    author='Fantomas42',
    author_email='support@emencia.com',
    url='https://github.com/emencia/emencia-django-countries',

    license='BSD License',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=[
        'emencia',
        'emencia.django',
    ],
    include_package_data=True,
    install_requires=[
        'setuptools',
    ],
    zip_safe=False,
)
