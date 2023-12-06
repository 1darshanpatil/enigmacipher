from setuptools import setup, find_packages
from enigmacipher import __version__

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='enigmacipher',  
    version=__version__,
    author="Darshan P.",
    author_email="drshnp@outlook.com",
    license="MIT",
    description="PIN encrypted enigma machine cipher texts",
    long_description=long_description,
    url="https://github.com/1darshanpatil/enigmacipher", 
    packages=find_packages(),
    package_data={
        'enigmacipher': ['defaultRotor.txt'],
    },
    entry_points={
        "console_scripts": [
            "enigma=enigmacipher.cliengine:main",
        ]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    include_package_data=True,
    keywords="enigma, cipher, encryption",
    project_urls={
        "Documentation": "https://github.com/1darshanpatil/enigmacipher#readme",
        "Source": "https://github.com/1darshanpatil/enigmacipher",
        "Tracker": "https://github.com/1darshanpatil/enigmacipher/issues",
    },
)
