from setuptools import setup, find_packages

setup(
    name="kruncherclient",
    version='0.1.2',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'requests',
        'python-dotenv'
    ],
) 