from setuptools import find_packages, setup
from typing import List
def get_requirements(file_path:str)->List[str]:

    '''
        Reads a requirements.txt file and returns a list of package names.
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if "-e ." in requirements:
            requirements.remove("-e .")

    return requirements

setup(
    name= 'mlproject',
    version='0.0.1',
    author='Ram',
    author_email='ramji.iiitdm2011@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')

)