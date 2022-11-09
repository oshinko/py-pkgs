__version__ = '0.0.0'

import importlib.metadata

distribution_name = None
distribution_summary = None
distribution_version = None

packages = importlib.metadata.packages_distributions()
distributions = set(packages.get(__name__, ()))

if len(distributions) == 1:
    distribution_name, = distributions
    metadata = importlib.metadata.metadata(distribution_name)
    distribution_summary = metadata.get('summary')
    distribution_version = metadata.get('version')

print(f'{__name__}.__version__:', __version__)
print(f'{__name__}.distribution_name:', distribution_name)
print(f'{__name__}.distribution_summary:', distribution_summary)
print(f'{__name__}.distribution_version:', distribution_version)
