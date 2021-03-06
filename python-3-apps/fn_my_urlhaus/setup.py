#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import glob
import ntpath


def get_module_name(module_path):
    """
    Return the module name of the module path
    """
    return ntpath.split(module_path)[1].split(".")[0]


def snake_to_camel(word):
    """
    Convert a word from snake_case to CamelCase
    """
    return ''.join(x.capitalize() or '_' for x in word.split('_'))


setup(
    name="fn_my_urlhaus",
    display_name="Alternative URLhaus",
    version="1.0.0",
    license="MIT License",
    author="Gerald Trotman",
    author_email="gerald.trotman@ibm.com",
<<<<<<< HEAD
    url="www.ibm.com",
=======
    url="http://www.ibm.com",
>>>>>>> 612b1f1b67525ff93288d22f875dca4fa093c360
    description="Resilient Circuits Components for 'fn_my_urlhaus'",
    long_description="""Resilient Circuits Components for 'fn_my_urlhaus'""",
    install_requires=[
        "resilient-circuits>=43.0.0"
    ],
    python_requires='>=3.6',
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    classifiers=[
        "Programming Language :: Python",
    ],
    entry_points={
        "resilient.circuits.components": [
            # When setup.py is executed, loop through the .py files in the components directory and create the entry points.
            "{}FunctionComponent = fn_my_urlhaus.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_my_urlhaus/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_my_urlhaus.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_my_urlhaus.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_my_urlhaus.util.selftest:selftest_function"]
    }
)
