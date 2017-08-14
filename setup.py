import io
from setuptools import setup, find_packages
import sys

def readfile(filename):
    with io.open(filename, encoding="utf-8") as stream:
        return stream.read().split("\n")

requires = readfile("requirements.txt")

setup(
    name='sphinxcontrib-httpdomain',
    version="1.5.0",
    description='Sphinx domain for HTTP APIs',
    author='Hong Minhee',
    author_email='eric@ericholscher.com',
    url='https://github.com/linhtc/starpeople',
    download_url='https://pypi.python.org/pypi/sphinxcontrib-httpdomain/1.5.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['sphinxcontrib'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
	'Intended Audience :: Developers',
	'License :: OSI Approved :: BSD License',
	'Operating System :: OS Independent',
	'Programming Language :: Python',
	'Topic :: Documentation',
	'Topic :: Utilities'
    ],
)

