try:
    from setuptools import setuptools

except Import Error:
    from distutils.core import setuptools

config = [
    'description': 'My project',
    'author': 'Chuba Ezeks',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'ezekschuba@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'projectname'
]

setup(**config)
