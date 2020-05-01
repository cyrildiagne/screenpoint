from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='screenpoint',
    packages=['screenpoint'],
    version='0.1.1',
    license='MIT',
    description='Project an image centroid to another image using OpenCV',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Cyril Diagne',
    author_email='diagne.cyril@gmail.com',
    url='https://github.com/cyrildiagne/screenpoint',
    download_url=
    'https://github.com/cyrildiagne/screenpoint/archive/v0.1.0.tar.gz',
    keywords=['opencv', 'sift', 'projection'],
    install_requires=[
        'opencv-contrib-python==3.4.2.17',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)