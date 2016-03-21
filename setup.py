import re
import os
import sys

from setuptools import setup, find_packages

if __name__ == '__main__':

    # get requirements
    with open('requirements.txt') as f:
        requirements = f.read()
        requirements = [
            r for r in requirements.splitlines() if r != '']
    # exclude pandas requirement for CI testing
    if os.environ.get('TRAVIS') or os.environ.get('CI'):
        requirements = [ r for r in requirements if not 'pandas' in r ]
    # test_requires depending on Python version
    tests_require = []
    if sys.version_info[0] == 2:
        tests_require = ['mock']
        if sys.version_info[1] < 7:
            tests_require.append('unittest2')
    # get readme
    with open('README.rst') as f:
        readme = f.read()
    # get version number
    with open('pgsheets/__init__.py') as f:
        version = f.read()
        version = re.search(
            r'^__version__\s*=\s*[\'"]([\d\.]*)[\'"]\s*$',
            version,
            re.MULTILINE).groups(1)[0]

    setup(name='pgsheets',
          version=version,
          packages=find_packages(exclude=['test', 'test.*']),
          author="Henry Stokeley",
          author_email="henrystokeley@gmail.com",
          description=("Manipulate Google Sheets Using Pandas DataFrames"),
          long_description=readme,
          license="MIT",
          url="https://github.com/henrystokeley/pgsheets",
          install_requires=requirements,
          tests_require=tests_require,
          test_suite='test',
          classifiers=[
              'Development Status :: 3 - Alpha',
              'License :: OSI Approved :: MIT License',
              'Programming Language :: Python :: 3.3',
              'Programming Language :: Python :: 3.4',
              'Programming Language :: Python :: 3.5',
              'Programming Language :: Python :: 2.6',
              'Programming Language :: Python :: 2.7',
              'Topic :: Scientific/Engineering',
              'Topic :: Office/Business :: Financial :: Spreadsheet',
              ],
          keywords='pandas google sheets spreadsheets dataframe',
          )
