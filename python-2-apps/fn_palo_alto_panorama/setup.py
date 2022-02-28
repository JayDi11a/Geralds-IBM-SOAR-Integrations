`#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_palo_alto_panorama',
    version='1.0.0',
    license='<<insert here>>',
    author='<<your name here>>',
    author_email='you@example.com',
    url='<<your company url>>',
    description="Resilient Circuits Components for 'fn_palo_alto_panorama'",
    long_description="Resilient Circuits Components for 'fn_palo_alto_panorama'",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'xmltodict',
        'bs4',
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "PaloAltoCreateSecurityPolicyRuleFunctionComponent = fn_palo_alto_panorama.components.palo_alto_create_security_policy_rule:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_palo_alto_panorama.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_palo_alto_panorama.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_palo_alto_panorama.util.selftest:selftest_function"]
    }
)