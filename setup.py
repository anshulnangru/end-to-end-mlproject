from setuptools import setup, find_packages
from typing import List


def get_reqirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        for req in requirements:
            req=req.replace("\n","")
        if '-e .' in requirements:
            requirements.remove('-e .')
            
    return requirements
setup(
    name='mlProject',
    version='0.0.1',
    author='Anshul',
    author_email='anshulnangru@gmail.com',
    packages=find_packages(),
    install_requires=get_reqirements('requirements.txt')
)