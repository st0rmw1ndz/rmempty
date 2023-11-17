import argparse
import os


def rmempty(directory: str):
    """Removes empty directories."""
    for root, dirs, files in os.walk(directory, topdown=False):
        if not dirs and not files:
            os.rmdir(root)
            print(f"Removed: {root}")
            parent_dir = os.path.dirname(root)
            while parent_dir and parent_dir != ".":
                if not os.listdir(parent_dir):
                    os.rmdir(parent_dir)
                    print(f"Removed: {parent_dir}")
                parent_dir = os.path.dirname(parent_dir)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="rmempty",
        description="Remove empty directories from a directory tree",
        epilog="Source code: https://codeberg.org/frosty/rmempty",
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
