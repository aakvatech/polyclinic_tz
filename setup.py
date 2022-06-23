from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in polyclinic_tz/__init__.py
from polyclinic_tz import __version__ as version

setup(
	name="polyclinic_tz",
	version=version,
	description="Polyclinic TZ",
	author="Aakvatech Limited",
	author_email="info@aakvatech.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
