from setuptools import setup, find_packages


# allows to get version via python setup.py --version
__version__ = "0.1.0"


setup(
    name="torchfid",
    version=__version__,
    description="Installable FID score calculation",
    url="https://github.com/rromb/torchfid",
    author="mseitzer et al",
    author_email="R.Rombach@stud.uni-heidelberg.de",
    license="MIT",
    packages=['torchfid'],
    install_requires=[
        "tqdm",
        "numpy",
        "scipy",
        "torch", 
        "torchvision"
    ],
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
)
