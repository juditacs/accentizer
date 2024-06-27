from setuptools import setup
from io import open

setup(
    name='hunaccent',
    packages=['hunaccent'],
    version='1.0.0',
    description='Accentize Hungarian text.',
    author='Judit Ács',
    author_email='judit@sch.bme.hu',
    url='https://github.com/juditacs/hunaccent',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    install_requires=['setuptools'],
    license='MIT',
    python_requires=">=3.6",
    classifiers=(
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Programming Language :: Python :: 3.12",
            "Programming Language :: Python :: 3 :: Only",
            "Intended Audience :: Developers",
            "Intended Audience :: Education",
            "Intended Audience :: Science/Research",
            "Topic :: Text Processing",
        )
)