from setuptools import setup, find_packages

setup(
    name='buttersalt_saltapi',
    description='The ButterSalt wrapper around the salt-api',
    long_description='ButterSalt-saltapi is a wrapper for salt rest_cherrypy API!',
    version='1.0.7',
    author='lfzyx',
    author_email='lfzyx.me@gmail.com',
    url='https://github.com/lfzyx/ButterSalt-saltapi',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    python_requires='~=3.6',
    install_requires=[
          'requests',
      ],
    keywords='buttersalt saltapi',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),

)
