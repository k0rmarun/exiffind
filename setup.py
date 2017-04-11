from setuptools import setup

setup(
    name='exiffind',
    version='0.0.5',
    packages=['exiffind'],
    url='https://github.com/k0rmarun/exiffind',
    license='MIT',
    author='Kormarun',
    author_email='kormarun@gmail.com',
    description='Find images by their exif tags',
    long_description=""""Find images bei their exif tags.
- before: date to be digitized before in format YY-MM-DD (other date formats might work)
- after: date to be digitized after in format YY-MM-DD (other date formats might work)
- ext: search only for files with $EXT extensions
- orientation: horizontal, vertical
- author: 
- software:
- width: search by image with (supports ranges)
- height: search by image height (supports ranges)
- manufacturer: search by camera manufacturer
- model: search by camera model
- speed: search by speed (ISO value, supports ranges)
- exposure: search by exposure time (supports ranges)
- aperture: search by aperture value (supports ranges)
- fnumber: search by f-number (supports ranges)
- xresolution: search by resolution in x direction (supports ranges)
- yresolution: search by resolution in y direction (supports ranges)
    """,

    entry_points={
        "console_scripts": [
            "exiffind = exiffind.exiffind:main"
        ]
    },
    install_requires=[
        "exifread",
        "python-dateutil"
    ],

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Desktop Environment :: File Managers',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Utilities',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)
