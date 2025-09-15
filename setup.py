import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_desc = f.read()
    
__version__ = "0.0.1"

REPO_NAME = "Text-series-forecasting"
USER_NAME = "MounaSriSai"
SRC_REPO = "timeseries_forecasting"  # package name, lowercase
EMAIL = "msrisai.p@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=USER_NAME,
    author_email=EMAIL,
    description="A small Python package for time series forecasting",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
)
