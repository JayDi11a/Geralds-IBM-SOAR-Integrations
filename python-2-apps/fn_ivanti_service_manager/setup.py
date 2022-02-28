#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_ivanti_service_manager',
    version='1.0.0',
    license='<<insert here>>',
    author='<<your name here>>',
    author_email='you@example.com',
    url='<<your company url>>',
    description="Resilient Circuits Components for 'fn_ivanti_service_manager'",
    long_description="Resilient Circuits Components for 'fn_ivanti_service_manager'",
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
            "IvantiCreateIncidentFunctionComponent = fn_ivanti_service_manager.components.ivanti_create_incident:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_ivanti_service_manager.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_ivanti_service_manager.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_ivanti_service_manager.util.selftest:selftest_function"]
    }
)