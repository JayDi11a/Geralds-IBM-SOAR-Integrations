#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_passive_total',
    version='1.0.0',
    license='<<insert here>>',
    author='<<your name here>>',
    author_email='you@example.com',
    description="Resilient Circuits Components for 'fn_passive_total'",
    long_description="Resilient Circuits Components for 'fn_passive_total'",
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
            "PassiveTotalQueryFunctionComponent = fn_passive_total.components.passive_total_query:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_passive_total.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_passive_total.util.customize:customization_data"]
    }
)