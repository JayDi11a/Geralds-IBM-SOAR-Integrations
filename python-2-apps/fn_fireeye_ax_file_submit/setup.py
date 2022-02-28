#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_fireeye_ax_file_submit',
    version='1.0.0',
    license='<<insert here>>',
    author='<<your name here>>',
    author_email='you@example.com',
    url='<<your company url>>',
    description="Resilient Circuits Components for 'fn_fireeye_ax_file_submit'",
    long_description="Resilient Circuits Components for 'fn_fireeye_ax_file_submit'",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'xmltodict',
        'requests',
        'resilient-lib',
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "FireeyeAxMalwareSubmissionFunctionComponent = fn_fireeye_ax_file_submit.components.fireeye_ax_malware_submission:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_fireeye_ax_file_submit.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_fireeye_ax_file_submit.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_fireeye_ax_file_submit.util.selftest:selftest_function"]
    }
)