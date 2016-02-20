from gh_parse import __version__

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

dependencies = ['docopt', 'termcolor']


def publish():
    os.system("python setup.py sdist upload")

if sys.argv[-1] == "publish":
    publish()
    sys.exit()

setup(
    name='gh_parse',
    version=".".join(str(x) for x in __version__),
    description='Github archive parser',
    long_description=open('README.rst').read(),
    url='http://www.github.com/github-compass/gh-archive-parser',
    license="MIT License",
    author='Ben Balaran',
    author_email='bbalaran@icloud.com',
    install_requires=dependencies,
    packages=['gh_parse', ],
    entry_points={
        'console_scripts': [
            'gh_parse=gh_parse.main:start'
        ],
    },
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ),
)
