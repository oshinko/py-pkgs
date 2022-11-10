import setuptools

import private_requirements

setuptools.setup(
    name='project7a',
    version='0.0.0',
    packages=['package7a'],
    install_requires=private_requirements.get(),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ]
)
