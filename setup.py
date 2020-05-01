from distutils.core import setup

setup(
    name='screenpoint',
    packages=['screenpoint'],
    version='0.1.0',
    license='MIT',
    description='Project an image centroid to another image using OpenCV',
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