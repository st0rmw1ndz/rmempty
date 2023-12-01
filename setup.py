from pathlib import Path

import setuptools

with Path.open("README.md", mode="r") as f:
    long_description = f.read()

setuptools.setup(
    name="rmempty",
    version="1.0.1",
    author="st0rm",
    author_email="inthishouseofcards@gmail.com",
    description="Remove empty directories from a directory tree",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/st0rmw1ndz/rmempty",
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": [
            "rmempty=rmempty.__main__:main",
        ]
    },
    python_requires=">=3.11",
)
