import warnings

__version__ = "1.1.2"

warnings.warn(
    "dns-benchmark-tool is deprecated and no longer maintained. "
    "migrate to: pip install net-benchmark — "
    "https://github.com/net-benchmark/net-benchmark",
    DeprecationWarning,
    stacklevel=2,
)
