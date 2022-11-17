import setuptools

import private_requirements

setuptools.setup(install_requires=private_requirements.get())
