#!/usr/bin/env python3
from setuptools import setup

setup(
    name='dev_aberto_yuritaba',
    version='0.1',
    packages=['dev_aberto'],
    author='Yuri Tabacof',
    python_requires='>=3.6',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Development Status :: 3 - Alpha',
    ],
    scripts=['scripts/hello.py'],  # Adicionando um script de linha de comando, se necessário
    install_requires=[
        'requests>=2.25.1',   # Exemplo de dependência para chamadas de API
        'python-dateutil>=2.8.1',  # Exemplo para lidar com datas
    ],
    entry_points={
        'console_scripts': [
            'hello=dev_aberto.hello:hello',  # Adicionando um script de linha de comando, se necessário
        ],
    },
)