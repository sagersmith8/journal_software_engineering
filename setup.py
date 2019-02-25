from setuptools import setup
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

if os.getenv("TRAVIS_TAG"):
    setup(
        name="journal-software-engineering",
        version_format='{tag}.dev{commits}+{sha}',
        setup_requires=['very-good-setuptools-git-version'],
        py_modules=["journal"],
        package_dir={'': 'src'},
        install_requires=['GitPython==2.1.11', 'colorama==0.4.1'],
        test_suite='nose.collector',
        tests_require=['nose'],
        # metadata to display on PyPI
        author="Sage Smith",
        author_email="sagersmith8@gmail.com",
        description="Provides tooling for scrum based engineering journal",
        long_description=long_description,
        long_description_content_type="text/markdown",
        license="Apache Commons 2.0",
        url="http://github.com/sagersmith8/journal",
        platforms=[2.7],
        classifiers=[
            "Programming Language :: Python :: 2",
            "License :: OSI Approved :: Apache Software License",
            "Operating System :: OS Independent",
        ]
    )
else:
    setup(
        name="journal-software-engineering",
        version="test",
        py_modules=["journal"],
        package_dir={'': 'src'},
        install_requires=['GitPython==2.1.11', 'colorama==0.4.1'],
        test_suite='nose.collector',
        tests_require=['nose'],
        # metadata to display on PyPI
        author="Sage Smith",
        author_email="sagersmith8@gmail.com",
        description="Provides tooling for scrum based engineering journal",
        long_description=long_description,
        long_description_content_type="text/markdown",
        license="Apache Commons 2.0",
        url="http://github.com/sagersmith8/journal",
        platforms=[2.7],
        classifiers=[
            "Programming Language :: Python :: 2",
            "License :: OSI Approved :: Apache Software License",
            "Operating System :: OS Independent",
        ]
    )
