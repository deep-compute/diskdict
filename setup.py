from setuptools import setup, find_packages

version = '0.2'
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
        'deeputil==0.2.5',
        'basescript==0.2.5',
        'sqlitedict==1.5.0',
    ],
    package_dir={'diskdict': 'diskdict'},
    packages=find_packages('.'),
    include_package_data=True,
    test_suite='test.suitefn',
    entry_points={
        "console_scripts": [
            "diskdict = diskdict:main",
        ]
    }

)
