from distutils.core import setup

with open('requirements.txt', 'r') as fid:
    requirements = [line for line in fid]

setup(name='<package_name>',
      version='<major>.<minor>',
      description='',
      author='',
      author_email='',
      url='',
      packages=['<package_name>'],
      install_requires=requirements
     )
