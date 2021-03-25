from setuptools import setup

setup(
    name="pdftitle",
    version='0.1',
    description='PDF File title editing CLI application',
    author='Kaspian Jakobsson',
    author_email='kaspian.jakobsson@gmail.com',
    url='https://github.com/kar-re/pdftitle',
    license='MIT',
    py_modules=['metachange'],
    install_requires=[
        'Click',
        'pdfrw',
    ],
    entry_points='''
        [console_scripts]
        pdftitle=metachange:cli
    ''',
)