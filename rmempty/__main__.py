import os

import click

import rmempty

HELP: str = """Remove empty directories from a directory tree.

By default, it will use the current directory if no PATH is given.

Copyright (c) 2023 frosty.
"""


@click.command(
    context_settings=dict(help_option_names=["-h", "--help"]),
    name="rmempty",
    help=HELP,
    epilog="Source code: https://github.com/st0rmw1ndz/rmempty",
)
@click.argument(
    "path",
    nargs=1,
    default=".",
    type=click.Path(exists=True, file_okay=False, dir_okay=True),
)
@click.version_option(rmempty.__version__, "-v", "--version")
def rmempty(path: str) -> None:
    """Removes empty directories from a directory tree.
    :param path: Directory path.
    :return: None.
    """
    for root, dirs, files in os.walk(path, topdown=False):
        if not dirs and not files:
            os.rmdir(root)
            if __name__ == "__main__":
                click.echo(f"Removed: {root}")
            parent = os.path.dirname(root)
            while parent and parent != ".":
                if not os.listdir(parent):
                    os.rmdir(parent)
                    if __name__ == "__main__":
                        click.echo(f"Removed: {parent}")
                parent = os.path.dirname(parent)


if __name__ == "__main__":
    rmempty()
