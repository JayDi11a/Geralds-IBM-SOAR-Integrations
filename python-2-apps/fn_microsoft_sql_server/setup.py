#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_microsoft_sql_server',
    version='1.0.0',
    license='<<insert here>>',
    author='<<your name here>>',
    author_email='you@example.com',
    description="Resilient Circuits Components for 'fn_microsoft_sql_server'",
    long_description="Resilient Circuits Components for 'fn_microsoft_sql_server'",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'pyodbc'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "MicrosoftSqlQueryFunctionComponent = fn_microsoft_sql_server.components.microsoft_sql_query:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_microsoft_sql_server.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_microsoft_sql_server.util.customize:customization_data"]
    }
)