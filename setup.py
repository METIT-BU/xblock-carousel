import os
from setuptools import setup


def package_data(pkg, root_list):
    """Generic function to find package_data for `pkg` under `root`."""
    data = []
    for root in root_list:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


setup(
    name='xblock-multimedia-carousel',
    version='1.0',
    description='XBlock - Multimedia-Carousel',
    packages=['carousel'],
    install_requires=[
        'XBlock',
    ],
    entry_points={
        'xblock.v1': 'carousel = carousel:CarouselBlock',
    },
    package_data=package_data("carousel", ["templates", "public"]),
)
