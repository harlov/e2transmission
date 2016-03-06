import os
from setuptools import setup, find_packages

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
VERSION = '1.0.0'

setup(
    name='e2transmission',
    version=VERSION,
    packages=find_packages(),
    package_data={'': ['e2transmission.json']},
    data_files=[
         ('/etc/', ['conf/e2transmission.json'])
    ],
    include_package_data=True,
    license='MTI License',
    description='add torrents from email to transmission',
    long_description='Daemon, what check email box(over IMAP) for new messages with torrents file\'s - and send them to transmission daemon.',
    url='https://github.com/harlov/e2transmission',
    download_url = 'https://github.com/harlov/e2transmission/archive/v'+VERSION+'.tar.gz',
    author='Nikita Harlov',
    author_email='nikita@harlov.com',
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Communications :: Email'
    ],

    #для удобства использования , забиндим вызов сервиса на комманду hmakecoffee-cli
    entry_points={'console_scripts': [
        'e2transmission-cli = e2transmission.__main__:main',
        ],
    },
)
