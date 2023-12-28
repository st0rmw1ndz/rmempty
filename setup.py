from pathlib import Path

import setuptools

import rmempty

if __name__ == "__main__":
    with Path("README.md").open(mode="r") as f:
        long_description = f.read()

    setuptools.setup(
        name="rmempty",
        version=rmempty.__version__,
        author="frosty",
        author_email="inthishouseofcards@gmail.com",
        description="Remove empty directories from a directory tree",
        long_description=long_description,
        long_description_content_type="text/markdown",
        license="MIT",
        url="https://github.com/st0rmw1ndz/rmempty",
        packages=setuptools.find_packages(),
        entry_points={
            "console_scripts": [
                "rmempty=rmempty.__main__:rmempty",
            ]
        },
        python_requires=">=3.11",
    )
