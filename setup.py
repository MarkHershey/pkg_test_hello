from setuptools import setup, find_packages

MAJOR = 0
MINOR = 0
MICRO = 1
VERSION = "%d.%d.%d" % (MAJOR, MINOR, MICRO)

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="pkg_test_hello",
    version=VERSION,
    author="Mark Huang",
    author_email="mark.h.huang@gmail.com",
    description="pkg_test_hello",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MarkHershey/pkg_test_hello",
    package_dir=({"": "src"}),
    packages=find_packages(where="src"),
)
