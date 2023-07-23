from setuptools import setup, find_packages

def parse_requirements(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return [line for line in lines if not line.startswith("-")]

required = parse_requirements('requirements.txt')

setup(
    name='elements',
    version='0.1.0',
    url='https://github.com/ZackPlauche/elements',
    author='Zack Plauche',
    author_email='zackknowspython@gmail.com',
    description='An OOP Python Selenium WebElement wrapper for with convenience methods and a structure for easier working with elements on a page.',
    packages=find_packages(),
    install_requires=required,
)
