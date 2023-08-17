from setuptools import setup

readme = open('./README.md', 'r')

setup(
    name='simplesqlite',
    packages=['simplesqlite'],
    version='0.0.1',
    description='Simplesqlite is a sqlite3 based python library that provides a simple interface to communicate with a sqlite database',
    long_description=readme.read(),
    long_description_content_type='text/markdown',
    author_email='carlos.bramila98@gmail.com',
    author='Carlos Brayan',
    url='',
    download_url='',
    keywords=['db', 'sqlite'],
    classifiers=[],
    license='Creative Commons',
    include_package_data=True

)