#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_sentinalone_endpoint_protection',
    version='1.0.0',
    license='<<insert here>>',
    author='<<your name here>>',
    author_email='you@example.com',
    url='<<your company url>>',
    description="Resilient Circuits Components for 'fn_sentinalone_endpoint_protection'",
    long_description="Resilient Circuits Components for 'fn_sentinalone_endpoint_protection'",
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
            "SentinaloneInitiateScanFunctionComponent = fn_sentinalone_endpoint_protection.components.sentinalone_initiate_scan:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_sentinalone_endpoint_protection.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_sentinalone_endpoint_protection.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_sentinalone_endpoint_protection.util.selftest:selftest_function"]
    }
)