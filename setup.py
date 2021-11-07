import pathlib
import setuptools

PACKAGE = 'project'

here = pathlib.Path(__file__).parent
package_path = here / PACKAGE.replace('.', '/')

about_script = (package_path / 'about.py').read_text(encoding='utf8')
about = {}
exec(about_script, about)

readme = (here / 'README.md').read_text(encoding='utf8')
readme_mimetype = 'text/markdown'

# import json
# setuptools.setup = lambda **kwargs: print(json.dumps(kwargs, indent=2))

setuptools.setup(
    name=about['name'],
    version=about['version'],
    description=about['description'],
    long_description=readme,
    long_description_content_type=readme_mimetype,
    author=about['author'],
    author_email=about['author_email'],
    url=about['url'],
    packages=[PACKAGE],
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
