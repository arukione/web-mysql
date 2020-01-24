from setuptools import setup

"""
name项目名称，和顶层目录名称一致;
version项目当前的版本
description简单描述
url为项目访问地址
author项目开发人员名称
author_email项目开发人员联系邮件
license遵循的授权许可
classifiers参考官方文档
keywords本项目的关键词
packages本项目包含哪些包
"""
setup(
    name='web_mysql',
    version='1.0.0.dev1',
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
    keywords='hive client python',
    packages=['web_mysql']
)

