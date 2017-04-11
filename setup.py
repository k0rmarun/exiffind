from setuptools import setup

setup(
    name='exiffind',
    version='0.0.4',
    packages=['exiffind'],
    url='https://github.com/k0rmarun/exiffind',
    license='MIT',
    author='Kormarun',
    author_email='kormarun@gmail.com',
    description='Find images by their exif tags',

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
