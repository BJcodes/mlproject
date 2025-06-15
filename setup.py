# this file is reponsible for creating and deploying the ML application as a package. 

from setuptools import find_packages, setup
from typing import List
HYPEN_E_DOT = '-e .'
def get_reqs (file_path:str)->List[str]:
    '''
     this function will return the list of libraries from the requirenments.txt file to be installed.
    '''
    reqList = []
    with open(file_path) as file:
        reqList=file.readlines()
        #replace the \n with blank
        reqList=[req.replace("\n","") for req in reqList]
        if HYPEN_E_DOT in reqList:
            reqList.remove(HYPEN_E_DOT)

        return reqList

setup(
    name = 'mlproject',
    version ='0.0.1',
    author = 'bjan',
    author_email = 'bilal.jan.bilal@gmail.com',
    packages = find_packages(),
    install_requires = get_reqs('requirenments.txt')
    #install_requires = ['pandas','numpy','seaborn']
)

