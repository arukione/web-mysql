from setuptools import setup

setup(
    name='web-mysql',
    version='1.0.0.dev2',
    description='A pure Python mysql connect tool which base on PyMysql',
    url='https://github.com/arukione/web-mysql',
    author='aruki',
    author_email='zqljiebin@gmail.com',
    license='MIT',
    install_requires=['pymysql'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords='web-mysql',
    packages=['web_mysql']
)

