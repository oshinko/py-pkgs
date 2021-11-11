__version__ = '0.0.0'

import importlib.metadata
import pathlib

me = pathlib.Path(__file__)
distribution_name = me.parent.name

print(me, 'Hello!')
print(me, '__version__', __version__)

version = __version__

try:
    metadata = importlib.metadata.metadata(distribution_name)
    version = metadata['version']
    print(me, 'metadata', dict(metadata))
except importlib.metadata.PackageNotFoundError:
    pass

print(me, 'version', version)
