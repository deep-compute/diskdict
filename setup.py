from setuptools import setup, find_packages

version = '0.2.5'
setup(
    name="diskdict",
    version=version,
    description="A dict like datastructure on disk",
    keywords='diskdict',
    author='Deep Compute, LLC',
    author_email="contact@deepcompute.com",
    url="https://github.com/deep-compute/diskdict",
    download_url="https://github.com/deep-compute/diskdict/tarball/%s" % version,
    license='MIT License',
    install_requires=[
        'deeputil==0.2.7',
        'basescript==0.2.9',
        'plyvel==1.0.4',
        'cmph-cffi==0.3.0',
        'diskarray==0.1.9',
        'numpy==1.14.3',
    ],
    package_dir={'diskdict': 'diskdict'},
    packages=find_packages('.'),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 2.7",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
    ],
    test_suite='test.suitefn',
    entry_points={
        "console_scripts": [
            "diskdict = diskdict:main",
        ]
    }

)
