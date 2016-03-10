import re
import os

from setuptools import setup, find_packages

if __name__ == '__main__':

    # get requirements
    with open('requirements.txt') as f:
        requirements = f.read()
        requirements = [
            r for r in requirements.splitlines() if r != '']
    # exclude pandas requirement for CI testing
    if os.environ('TRAVIS') or os.environ('CI'):
        requirements = [ r for r in requirements if not 'pandas' in r ]
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
          tests_require=['mock'],
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
