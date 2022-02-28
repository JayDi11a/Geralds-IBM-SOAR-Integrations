#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_palo_alto_wildfire',
    version='1.0.0',
    license='<<insert here>>',
    author='<<your name here>>',
    author_email='you@example.com',
    url='<<your company url>>',
    description="Resilient Circuits Components for 'fn_palo_alto_wildfire'",
    long_description="Resilient Circuits Components for 'fn_palo_alto_wildfire'",
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
            "PaloAltoWildfireFileSubmissionArtifactFunctionComponent = fn_palo_alto_wildfire.components.palo_alto_wildfire_file_submission_artifact:FunctionComponent",
            "PaloAltoWildfireFileSubmissionAttachmentFunctionComponent = fn_palo_alto_wildfire.components.palo_alto_wildfire_file_submission_attachment:FunctionComponent",
            "PaloAltoWildFireUrlSubmission = fn_palo_alto_wildfire.components.palo_alto_wildfire_url_submission:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_palo_alto_wildfire.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_palo_alto_wildfire.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_palo_alto_wildfire.util.selftest:selftest_function"]
    }
)