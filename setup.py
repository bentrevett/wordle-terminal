import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="wordle",
    author="Ben Trevett",
    author_email="bentrevett@gmail.com",
    description="Wordle in the terminal.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bentrevett/wordle-terminal",
    project_urls={
        "Bug Tracker": "https://github.com/bentrevett/wordle-terminal/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    scripts=["scripts/wordle"],
    python_requires=">=3.6",
    install_requires=[
        "termcolor",
    ],
)
