from setuptools import setup
import sys

extra = { }

if sys.version_info >= (3,):
    extra['use_2to3'] = True
    raise NotImplementedError("2to3 conversion has not been tested!")

setup(
    name='stereocode',
    version = '1.0',
    description='Source code stereotypeing tool that annotates srcML-i-fied with method stereotypes.',
    author='SDML',
    author_email='',
    package_dir = {'': 'src'},
    packages = ['stereocode'],
    test_suite = ''#,
    # **extra

    license = "GPL",
    keywords = "static-analysis stereotype stereocode srcML SDML",
    url = "www.sdml.com",
    long_description="",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
    ],

)