"""
Project's setuptool configuration.

This should eggify and in theory upload to pypi without problems.

Oisin Mulvihill
2008-12-23

"""
try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages


Name='evasion-docs'
ProjecUrl="" #""
Version='1.0.0'
Author='Oisin Mulvihill'
AuthorEmail='oisinmulvihill at gmail dot com'
Maintainer=' Oisin Mulvihill'
Summary='This package used to aid in sphinx documentation generation for the evasion project.'
License='Evasion Project CDDL License'
ShortDescription=Summary
Description=Summary

TestSuite = ''

needed = [
    'docutils',
	'pygments',
	'sphinx',
    
    # evasion deps:
    'evasion-web',
    'evasion-messenger',
    'evasion-agency',
    'evasion-director',
]

#  find lib/director/viewpoint -type d -exec touch {}//__init__.py \;
#
# If new directories are added then I'll need to rerun this command.
#
EagerResources = [
    'evasion',
]

ProjectScripts = [
]

PackageData = {
    # If any package contains *.txt or *.rst files, include them:
    '': ['*.*'],
}

# Make exe versions of the scripts:
EntryPoints = {
}


setup(
#    url=ProjecUrl,
    zip_safe=False,
    name=Name,
    version=Version,
    author=Author,
    author_email=AuthorEmail,
    description=ShortDescription,
    long_description=Description,
    license=License,
    test_suite=TestSuite,
    scripts=ProjectScripts,
    install_requires=needed,
    packages=find_packages(),
    package_data=PackageData,
    eager_resources = EagerResources,
    entry_points = EntryPoints,
    namespace_packages = ['evasion'],
)
