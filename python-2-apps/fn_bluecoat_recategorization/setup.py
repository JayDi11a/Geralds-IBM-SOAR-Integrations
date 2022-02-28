#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_bluecoat_recategorization',
    version='1.0.0',
    license='<<insert here>>',
    author='<<your name here>>',
    author_email='you@example.com',
    url='<<your company url>>',
    description="Resilient Circuits Components for 'fn_bluecoat_recategorization'",
    long_description="Resilient Circuits Components for 'fn_bluecoat_recategorization'",
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
            "BluecoatSiteReviewRecategorizationFunctionComponent = fn_bluecoat_recategorization.components.bluecoat_site_review_recategorization:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_bluecoat_recategorization.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_bluecoat_recategorization.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_bluecoat_recategorization.util.selftest:selftest_function"]
    }
)