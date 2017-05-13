from ah.config import VERSION

from distutils.core import setup


## When using setuptools ##
# comment out distutils.core's setup
#
# from setuptools import setup, find_packages
# setup:
# packages=find_packages()
# include_package_data=True


setup(name="AH",
      version=VERSION,
      packages=["ah", "ah/auctionhouse", "ah/db", "ah/game"],
      author="Christian Hall",
      author_email="chris.ant.hall@gmail.com",
      license="",
      description=("Auction House Package"),
      url="gamingmotive.wordpress.com",
)


