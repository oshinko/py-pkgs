import importlib.metadata

print(__file__, 'Hello!')

distribution_name = __name__

version = None

try:
    metadata = importlib.metadata.metadata(distribution_name)
    version = metadata['version']
    print(__file__, 'metadata', dict(metadata))
except importlib.metadata.PackageNotFoundError:
    pass

print(__file__, 'version', version)
