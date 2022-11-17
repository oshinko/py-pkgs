import setuptools

import private_requirements

setuptools.setup(
    name='pyproject8a2',
    version='0.0.0',
    packages=['package'],
    install_requires=private_requirements.get(),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ]
)
