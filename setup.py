import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PythonPackage-SpencerWBarnes", # Replace with your own username
    version="1.0",
    author="Spencer Barnes",
    author_email="SWilliamBarnes@google.com",
    description="Package to give a greeting to the globe",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SpencerWBarnes/PythonPackage",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)