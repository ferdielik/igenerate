from setuptools import setup

setup(name='igenerate',
      description='Easy generate apple watch and ios icons with one command.',
      long_description='Easy generate apple watch and ios icons with one command.',
      version='1.0.2',
      url='https://github.com/ferdielik/igenerate',
      author='Ferdi Elik',
      author_email='elikferdi@gmail.com',
      license='Apache2',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python :: 3'
      ],
      scripts=['igenerate/igenerate'],
      install_requires=[
          'pillow'
      ],
      ),
