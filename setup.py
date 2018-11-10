import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rpi-sprinkler-control",
    version="0.0.1",
    author="Joseph Luccisano",
    author_email="joseph.luccisano@gmail.com",
    description="Control your sprinkler system via a Raspberry PI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jluccisano/rpi-sprinkler-control",
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

