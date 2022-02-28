#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_ip_address',
    version='1.0.0',
    license='<<insert here>>',
    author='<<your name here>>',
    author_email='you@example.com',
    url='<<your company url>>',
    description="Resilient Circuits Components for 'fn_ip_address'",
    long_description="Resilient Circuits Components for 'fn_ip_address'",
    install_requires=[
        'resilient_circuits>=30.0.0'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "GetIpAddressFunctionComponent = fn_ip_address.components.get_ip_address:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_ip_address.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_ip_address.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_ip_address.util.selftest:selftest_function"]
    }
)