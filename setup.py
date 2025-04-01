from setuptools import setup, find_packages

setup(
    name='BrainSim-X',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'tensorflow==2.8.0',
        'scikit-learn==1.0.2',
        'numpy==1.20.0',
        'matplotlib==3.4.3',
        'pandas==1.3.3',
        'MNE==0.24.0',
        'qiskit==0.36.2',
        'Brian2==2.4.0'
    ],
    description='A neural network framework for simulating human brain functions',
    author='Nawman Baig',
    author_email='support@brainsim-x.in',
    url='https://github.com/BrainSim-X/BrainSim-X',
)
