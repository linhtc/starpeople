from setuptools import setup, find_packages


setup(
    name='sphinxcontrib-httpdomain',
    version="1.5.0",
    description='Sphinx domain for HTTP APIs',
    author='Hong Minhee',
    author_email='eric@ericholscher.com',
    url='https://pypi.python.org/pypi/sphinxcontrib-httpdomain',
    packages=find_packages(),
    include_package_data=True,
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
