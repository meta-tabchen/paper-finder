import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="paper_finder",
    version="0.0.4",
    author="TabChen",
    author_email="2808581543@qq.com",
    description="Finder papers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/meta-tabchen/paper-finder",
    project_urls={
        "Bug Tracker": "https://github.com/meta-tabchen/paper-finder/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.5",
    include_package_data=True,
    install_requires=['requests','pandas','tqdm','beautifulsoup4'],
)