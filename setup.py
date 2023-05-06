from setuptools import setup, find_packages
from datetime import datetime

setup(
    name='host_tool',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'datetime',
    ],
    entry_points={
        'console_scripts': [
            'my_script=my_project.my_script:main',
        ],
    },
    author='razvan.ghetiu',
    author_email='razvan.ghetiu@gmail.com',
    description='Hosts connections logs tool',
    url='https://github.com/raxghetiu/host_tool',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.10',
    ],
    keywords='host, logs, challenge'
)
