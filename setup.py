from setuptools import setup

setup(
    name='kodi-release-helper',
    version='1.0.3',
    description='Kodi Release Helper',
    author='asciidisco',
    author_email='public@asciidisco.com',
    py_modules=['kodi-release-helper'],
    install_requires=['semver', 'gitchangelog'],
    license='MIT License',
    zip_safe=False,
    keywords='kodi release helper',
    scripts=['bin/kodi-release'],
    classifiers=['Packages', 'kodi-release-helper'])
