from setuptools import setup, find_packages

setup(
    name="DividendQuery",
    version="0.1",
    packages=find_packages(),
    scripts=['pardiv.py'],

    install_requires=['bs4>=4.6.0'],

    author="Ving Trung",
    author_email="svingt@gmail.com",
    description="This is an Example Package",
    license="MIT",
    keywords="dividend query tool",
    url="https://github.com/vtrung/nasdaq-dividend-parser",  
    project_urls={
        "Documentation": "https://github.com/vtrung/nasdaq-dividend-parser",
        "Source Code": "https://github.com/vtrung/nasdaq-dividend-parser",
    }
)