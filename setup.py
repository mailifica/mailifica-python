from setuptools import setup, find_packages

setup(
    name="mailifica",
    version="1.0.0",
    description="Official Python SDK for Mailifica Email Infrastructure",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Mailifica",
    author_email="team@mailifica.com",
    url="https://github.com/mailifica/mailifica-python",
    packages=find_packages(),
    package_data={"mailifica": ["py.typed"]},
    install_requires=[
        "requests>=2.28.0",
        "typing-extensions>=4.0.0;python_version<'3.10'",
    ],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
