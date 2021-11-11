import setuptools

setuptools.setup(packages=[x for x in setuptools.find_namespace_packages()
                           if x == 'project' or x.startswith('project.')])
