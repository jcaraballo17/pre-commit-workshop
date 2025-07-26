import argparse
from typing import Sequence

from custom_hook.check import validate_filename


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog='validate-filename')
    parser.add_argument(
        'filenames',
        nargs='*',
        help='Filenames to process.',
    )
    parser.add_argument(
        '--prefix',
        default='ba_',
        type=str,
        help='Prefix the filenames need to have.',
    )

    args = parser.parse_args(argv)

    results = [validate_filename(filename, args.prefix) for filename in args.filenames]
    return int(any(results))
