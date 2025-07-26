"""Custom code quality check implementation."""

from pathlib import Path


def validate_filename(filename: str, prefix: str = 'ba_') -> int:
    name = Path(filename).name

    if failure := not name.startswith(prefix):
        print(f'Name does not start with {prefix!r}: {filename}')

    return int(failure)
