from setuptools import setup, find_packages

with open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(name = 'lumache_test',
    version = '0.1',
    description = 'API to lumache recipe',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://github.com/melaniecheah/lumache_test',
    author = 'Melanie',
    author_email = 'melaniecheah46@gmail.com',
    install_requires = ['furo'],
)
