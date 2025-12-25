from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="racquet-lab",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python library for Tennis Equipment Physics and Customization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/racquet-lab",
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/racquet-lab/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Physics",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.7",
)
