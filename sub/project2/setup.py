import pathlib

import setuptools

NAME = 'project2'
PACKAGES = ['project', 'project2']

here = pathlib.Path(__file__).parent
package_data = {x: [] for x in PACKAGES}

for package in PACKAGES:
    package_path = here / package.replace('.', '/')
    package_data_path = package_path / 'data'
    for path in package_data_path.glob('**/*'):
        if path.is_file():
            path = path.relative_to(package_path)
            package_data[package].append(str(path))

about_script = (here / 'about.py').read_text(encoding='utf8')
about = {}
exec(about_script, about)

readme = (here / 'README.md').read_text(encoding='utf8')
readme_mimetype = 'text/markdown'

setuptools.setup(
    name=about['name'],
    version=about['version'],
    description=about['description'],
    long_description=readme,
    long_description_content_type=readme_mimetype,
    author=about['author'],
    author_email=about['author_email'],
    url=about['url'],
    packages=PACKAGES,
    package_data=package_data,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ]
)
