from setuptools import setup

setup(
    name='OCC_Slicer',
    version='0.0.1',
    author='Maximillian Merritts',
    author_email='merrittsmax@gmail.com',
    packages=['Slicer'],
    py_modules=[],
    scripts=[],
    url='https://github.com/ExordiumAndTerminus/OCC_Slicer',
    license='LICENSE.txt',
    description='An un-described package.',
    long_description=open('README.md').read(),
    install_requires=[
        'shapely',
        'OCC',
        'UnitAlg'
    ],
    python_requires='~=3.7'
)