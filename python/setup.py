"""
    Setup file for handypy.
    Use setup.cfg to configure your project.

    This file was generated with PyScaffold 4.5.
    PyScaffold helps you to put up the scaffold of your new Python project.
    Learn more under: https://pyscaffold.org/
"""
from setuptools import setup
import os


def version_func(b):
    return "1.0."


def local_version_func(b):
    build_num = os.getenv("BUILD_NUMBER")
    if not build_num:
        return "999999"
    else:
        return build_num


if __name__ == "__main__":
    try:
        # Version issue fix
        # https://github.com/pypa/setuptools_scm
        # https://github.com/pypa/setuptools_scm/issues/536
        # https://pyscaffold.org/en/v4.0.2/faq.html
        # python setup.py --version
        # setup(use_scm_version={"version_scheme": "no-guess-dev"})
        setup(
            use_scm_version={
                "root": "..",
                "relative_to": __file__,
                "version_scheme": version_func,
                # "local_scheme": "node-and-timestamp"
                "local_scheme": local_version_func,
            }
        )
    except:  # noqa
        print(
            "\n\nAn error occurred while building the project, "
            "please ensure you have the most updated version of setuptools, "
            "setuptools_scm and wheel with:\n"
            "   pip install -U setuptools setuptools_scm wheel\n\n"
        )
        raise
