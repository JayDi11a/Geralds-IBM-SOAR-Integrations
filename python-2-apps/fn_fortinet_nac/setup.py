#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_fortinet_nac',
    version='1.0.0',
    license='<<insert here>>',
    author='<<your name here>>',
    author_email='you@example.com',
    description="Resilient Circuits Components for 'fn_fortinet_nac'",
    long_description="Resilient Circuits Components for 'fn_fortinet_nac'",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'xmltodict'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "NacQueryFunctionComponent = fn_fortinet_nac.components.nac_query:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_fortinet_nac.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_fortinet_nac.util.customize:customization_data"]
    }
)