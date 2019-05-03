from setuptools import setup, find_packages

setup(
      name="lazypt",
      version="0.1",
      author_email="moonx2006@gmail.com",
      packages=['lazypt'],
      package_data={},
      license='MIT',
      install_requires=['click', 'pyperclip', 'pyyaml'],
      entry_points={
        'console_scripts': ['lazypt = lazypt.cli:commands']
      }
)
