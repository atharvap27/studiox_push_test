from setuptools import setup, find_packages
setup(
    name="google_custom_search_api",
    version="2.0.0",
    description="Python SDK for Google Custom Search API",
    packages=find_packages(),
    install_requires=["requests", "pydantic"],
    python_requires=">=3.7"
)
