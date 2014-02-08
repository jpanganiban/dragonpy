from setuptools import setup


__name__ = 'dragonpy'
__version__ = '0.0.1'
__author__ = "Jesse Panganiban"


setup(name=__name__,
      version=__version__,
      description="Dragonpay Python library",
      author=__author__,
      author_email="me@jpanganiban.com",
      url="https://github.com/jpanganiban/dragonpy.git",
      py_modules=['dragon'],
      test_suite="test_dragon")
