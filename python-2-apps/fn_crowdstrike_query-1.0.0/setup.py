#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_crowdstrike_query',
    version='1.0.0',
    license='<<insert here>>',
    author='<<your name here>>',
    author_email='you@example.com',
    description="Resilient Circuits Components for 'fn_crowdstrike_query'",
    long_description="Resilient Circuits Components for 'fn_crowdstrike_query'",
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
            "QueryMalwareUserConnectionFunctionComponent = fn_crowdstrike_query.components.query_malware_user_connection:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_crowdstrike_query.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_crowdstrike_query.util.customize:customization_data"]
    }
)