from setuptools import setup, find_packages

setup(
    name='coalition_service_grpc',
    version='0.0.7',
    packages=find_packages(),
    install_requires=[
        "grpcio",
        "grpcio-tools"
    ],
)