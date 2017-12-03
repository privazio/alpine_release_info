# Always prefer setuptools over distutils
from setuptools import setup
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='alpine_release_info',
    version='1.0.1',
    description='Alpine Linux release information',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/privazio/alpine_release_info',

    # Author details
    author='Rafael del Valle',
    author_email='rvalle@valletech.eu',

    # Choose your license
    license='GPLv3',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7'
    ],

    keywords='linux alpine docker ansible puppet',
    packages=['alpine_release_info'],
    install_requires=['commandify', 'PyYAML'],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },

    package_data={
        'alpine_release_info': ['alpine.yml'],
    },

    entry_points={
        'console_scripts': [
            'alpine_release_info=alpine_release_info:main',
        ],
    },

    test_suite="tests"
)
