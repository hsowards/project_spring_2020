import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="RSR", 
    version="0.0.1",
    author="Hayley Sowards",
    author_email="hayley.sowards@gmail.com",
    description="This package aims to help process data for analysis using the fine-mapping programs SuSiE and DAP-G",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hsowards/project_spring_2020",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)