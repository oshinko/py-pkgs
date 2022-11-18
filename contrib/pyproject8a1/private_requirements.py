import os
import pathlib

current_dir = pathlib.Path.cwd()

pri_reqs_file = current_dir / 'private-requirements.txt'
pri_reqs = pri_reqs_file.read_text(encoding='utf8').split()

local_pri_reqs_file = current_dir / 'local-private-requirements.txt'


def _format(distribution_path):
    dist = pathlib.PurePosixPath(distribution_path).name
    path = (current_dir / distribution_path).resolve()
    no_leading_slash = str(path).replace(os.sep, '/').lstrip('/')
    return f'{dist} @ file:///{no_leading_slash}'


def pep508ify(reqs):
    return tuple(map(_format, reqs))


def get():
    return pep508ify(pri_reqs)


if __name__ == '__main__':
    local_pri_reqs_file.write_text('\n'.join(get()), encoding='utf8')
