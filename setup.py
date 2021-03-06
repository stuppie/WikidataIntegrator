import os
from setuptools import setup, find_packages
from subprocess import check_output
from subprocess import CalledProcessError

setup_path = os.path.dirname(__file__)

print("setup_path: {}".format(setup_path))


def read(fname):
    return open(os.path.join(setup_path, fname)).read()

MAJOR_VERSION = 0
MINOR_VERSION = 0
REPO_URL = 'https://github.com/sebotic/WikidataIntegrator'

try:
    MICRO_VERSION = int(check_output("git rev-list --count master", shell=True).decode('utf-8').strip('\n'))
except:
    MICRO_VERSION = 1

# Calculate commit hash
try:
    commit_hash = check_output("git rev-parse HEAD", shell=True).decode('utf-8').strip('\n')
except CalledProcessError:
    commit_hash = ''

f = open('./.git-commit-hash', 'w')
f.write("{}.git\n{}".format(REPO_URL, commit_hash))
f.close()

setup(
    name='WikidataIntegrator',
    version="{}.{}.{}".format(MAJOR_VERSION, MINOR_VERSION, MICRO_VERSION),
    author='Sebastian Burgstaller-Muehlbacher, Gregg Stupp, Andra Waagmeester',
    author_email='sburgs@scripps.edu',
    description='Python package for reading and writing to/from Wikidata',
    license='AGPLv3',
    keywords='Wikidata biology chemistry medicine',
    url=REPO_URL,
    packages=find_packages(),
    include_package_data=True,
    long_description=read('README.md'),
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2.7",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GPL License",
        "Operating System :: POSIX",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Intended Audience :: Science/Research",
        "Topic :: Utilities",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ],
    install_requires=[
        'requests',
    ],
)
