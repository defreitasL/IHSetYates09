from setuptools import setup, find_packages

setup(
    name='IHSetYates09',
    version='1.1.2',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'numpy',
        'xarray',
        'numba',
        'datetime',
        'spotpy',
        'IHSetCalibration @ git+https://github.com/defreitasL/IHSetCalibration.git'
    ],
    author='Lucas de Freitas Pereira',
    author_email='lucas.defreitas@unican.es',
    description='IH-SET Yates et al. (2009)',
    url='https://github.com/defreitasL/IHSetYates09',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)