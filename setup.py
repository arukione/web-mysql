from setuptools import setup

setup(
    name='Web-MySQL',
    version='1.0.3',
    description='A pure Python mysql connect tool which base on PyMysql',
    long_description='A toolkit that simplifies the operation of Python website connecting to MySQL database.\
Just set MySQL settings and you can fetchone,fetchall,executor function to operate MySQL database.',
    url='https://github.com/arukione/Web-MySQL',
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
