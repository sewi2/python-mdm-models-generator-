import codecs
from os import path

from setuptools import setup, find_packages


here = path.abspath(path.dirname(__file__))

with codecs.open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with codecs.open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    requirements = [
        line for line in f.readlines()
        if line and not line.startswith('#')
    ]

setup(
    name='python-mdm-models-generator',
    packages=find_packages(),
    version='0.1.2',
    license='MIT',
    description='This library allows us to generate django models and drf serializers using an OpenAPI schema',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Dmitry Nikolaev',
    author_email='sewi0018@gmail.com',
    url='https://github.com/sewi2/python-mdm-models-generator',
    download_url='https://github.com/sewi2/python-mdm-models-generator/archive/refs/tags/0.1.2.tar.gz',
    keywords=['mdm', 'models', 'serializers', 'generator', ],
    install_requires=[requirements],
    python_requires='~=3.6',
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.10',
    ],
)
