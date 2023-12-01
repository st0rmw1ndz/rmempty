import argparse
import os


def rmempty(directory: str) -> None:
    """removes empty directories from a directory tree"""

    for root, dirs, files in os.walk(directory, topdown=False):
        if not dirs and not files:
            os.rmdir(root)
            print(f"removed: {root}")
            parent = os.path.dirname(root)
            while parent and parent != ".":
                if not os.listdir(parent):
                    os.rmdir(parent)
                    print(f"removed: {parent}")
                parent = os.path.dirname(parent)


def main():
    parser = argparse.ArgumentParser(
        prog="rmempty",
        description="removes empty directories from a directory tree",
        epilog="source code: https://github.com/st0rmw1ndz/rmempty",
    )
    parser.add_argument(
        "path",
        help="path to remove empty directories from (default: current directory)",
        nargs="?",
        default=".",
    )
    args = parser.parse_args()
    rmempty(args.path)


if __name__ == "__main__":
    main()
