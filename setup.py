from setuptools import setup, find_packages
from io import open

setup(
    name='hunaccent',
    version='1.0.0',
    description='Accentize Hungarian text.',
    author='Judit Ács',
    author_email='judit@sch.bme.hu',
    url='https://github.com/juditacs/hunaccent',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    install_requires=['setuptools'],
    packages=['hunaccent'],
    include_package_data=True,
    license='MIT',
    python_requires=">=3.6"
)