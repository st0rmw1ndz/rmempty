from pathlib import Path

import click

from rmempty import __version__


@click.command(context_settings=dict(help_option_names=["-h", "--help"]))
@click.version_option(__version__)
@click.argument(
    "path",
    nargs=1,
    default=".",
    type=click.Path(exists=True, file_okay=False, dir_okay=True),
)
def cli(path: str) -> None:
    """Removes empty directories from a directory tree.

    By default, it will use the current directory if no PATH is given.

    Copyright (c) 2024 frosty.
    """

    def rmempty(directory: Path) -> None:
        if not any(directory.iterdir()):
            directory.rmdir()
            click.echo(f"Removed '{directory}'")
            if directory.parent != Path():
                rmempty(directory.parent)

    for directory in list(Path(path).rglob("")):
        rmempty(directory)


if __name__ == "__main__":
    cli()
