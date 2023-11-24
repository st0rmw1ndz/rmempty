import argparse
import os


def rmempty(directory: str) -> None:
    """Removes empty directories."""
    for root, dirs, files in os.walk(directory, topdown=False):
        if not dirs and not files:
            os.rmdir(root)
            print(f"Removed: {root}")
            parent = os.path.dirname(root)
            while parent and parent != ".":
                if not os.listdir(parent):
                    os.rmdir(parent)
                    print(f"Removed: {parent}")
                parent = os.path.dirname(parent)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="rmempty",
        description="Remove empty directories from a directory tree",
        epilog="Source code: https://github.com/st0rmw1ndz/rmempty",
    )
    parser.add_argument(
        "path",
        type=str,
        nargs="?",
        default=".",
        help="path to remove empty directories from (default: current directory)",
    )
    args = parser.parse_args()
    rmempty(args.path)
