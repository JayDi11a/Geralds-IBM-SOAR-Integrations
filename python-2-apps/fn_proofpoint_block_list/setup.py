#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_proofpoint_block_list',
    version='1.0.0',
    license='<<insert here>>',
    author='<<your name here>>',
    author_email='you@example.com',
    url='<<your company url>>',
    description="Resilient Circuits Components for 'fn_proofpoint_block_list'",
    long_description="Resilient Circuits Components for 'fn_proofpoint_block_list'",
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
            "ProofpointAddToBlockGroupFunctionComponent = fn_proofpoint_block_list.components.proofpoint_add_to_block_group:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_proofpoint_block_list.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_proofpoint_block_list.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_proofpoint_block_list.util.selftest:selftest_function"]
    }
)