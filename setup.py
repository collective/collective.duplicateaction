from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='collective.duplicateaction',
      version=version,
      description="Adds additional action to content actions menu for duplicating content.",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='plone contentaction duplicate',
      author='Lukas Zdych',
      author_email='lukas.zdych@gmail.com',
      url='http://github.com/collective/collective.duplicateaction',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Products.CMFPlone'
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
