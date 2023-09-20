"""
demokit
This is a demo kit.
"""

# Add imports here
from .demokit import RMSF

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
