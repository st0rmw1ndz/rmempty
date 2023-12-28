# rmempty

rmempty is a tool to remove all empty directories from a directory tree. It's a simple command to call from the terminal, and should also work when imported from other Python modules.

```
$ rmempty "D:\rmempty"
Removed: D:\rmempty\folderup\alittlelower\really\woahh
Removed: D:\rmempty\folderup\alittlelower\really
Removed: D:\rmempty\folderup\alittlelower
Removed: D:\rmempty\folderup
Removed: D:\rmempty\overhere\hahayeah\itsreal
Removed: D:\rmempty\overhere\hahayeah
Removed: D:\rmempty\overhere\whoops
Removed: D:\rmempty\overhere
Removed: D:\rmempty
```

**Note:** in the snippet provided, it deleted the directory I gave it. This is because it was empty after deleting all the empty folders inside it. rmempty will not remove any folders if there's content inside.

## Dependencies

- Python (`>=3.11`) with `click` installed

## Usage

rmempty uses [Click](https://click.palletsprojects.com/en/) for the command line interface. The text snippet is taken from the help menu accessed via `rmempty --help`.

```
Usage: rmempty [OPTIONS] [PATH]

  Remove empty directories from a directory tree.

  By default, it will use the current directory if no PATH is given.

  Copyright (c) 2023 frosty.

Options:
  -h, --help  Show this message and exit.

  Source code: https://github.com/st0rmw1ndz/rmempty
```

## Installation

Installation is a simple `pip` command using the git repo as the URL. It should be able to automatically download the dependencies.

```
pip install git+https://github.com/st0rmw1ndz/rmempty
```