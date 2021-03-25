from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="editpdf",
    version='0.1.1',
    description='PDF File title editing CLI application',
    author='Kaspian Jakobsson',
    author_email='kaspian.jakobsson@gmail.com',
    url='https://github.com/kar-re/pdftitle',
    license='MIT',
    long_description=long_description,      
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      
    python_requires='>=3.6',                
    py_modules=['metachange'],
    install_requires=[
        'Click',
        'pdfrw',
    ],
    entry_points='''
        [console_scripts]
        editpdf=metachange:cli
    ''',
)