from setuptools import setup, find_packages

setup (
  name                 = "myproject",
  version              = "0.1.0",
  description          = "myProject for Django pipeline",
  packages             = find_packages(),
  include_package_data = True,
  scripts              = ["manage.py"],
  install_requires     = ["Django>=1.10.6"
                        ],