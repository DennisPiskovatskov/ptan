"""
PTAN stands for PyTorch AgentNet -- reimplementation of AgentNet library for pytorch
"""
import setuptools


requirements = ['torch==1.3.1', 'gym', 'atari-py', 'numpy', 'opencv-python']


setuptools.setup(
    name="ptan",
    author="Max Lapan",
    author_email="max.lapan@gmail.com",
    license='GPL-v3',
    description="PyTorch reinforcement learning framework (with torch=1.3.1, upgrade version to 0.6.1)",
    version="0.6.1",
    packages=setuptools.find_packages(),
    install_requires=requirements,
)
