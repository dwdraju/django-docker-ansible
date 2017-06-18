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
  extras_require       = {
                            "test": [
                              "colorama>=0.3.3",
                              "coverage>=4.0.3",
                              "django-nose>=1.4.2",
                              "nose>=1.3.7",
                              "pinocchio>=0.4.2"
                            ]
                         }
)                        