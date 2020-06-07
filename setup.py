import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="BrowseAwareCore", 
    version="20.0.4",
    author="Sreeram Ganesan",
    author_email="sreeram2910@gmail.com",
    description="A package to extract, pre-process and manipulate data from the URLs and to scientifically predict distractions while browsing.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sreeram-gsan/BrowseAwareCore",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          'requests','bokeh','beautifulsoup4'
      ],
    python_requires='>=3.6',
)