import setuptools

ROOT_PACKAGES = ['package', 'package6']

setuptools.setup(packages=[x for x in setuptools.find_namespace_packages()
                           for y in ROOT_PACKAGES
                           if x == y or x.startswith(y + '.')])
