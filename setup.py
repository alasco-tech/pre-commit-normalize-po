from setuptools import setup


setup(
    name='pre_commit_dummy_package',
    version='0.0.0',
    install_requires=['polib ~= 1.1.0'],
    entry_points={
        'console_scripts': [
            'normalize-po = normalize_po_files:main'
        ]
    },
    py_modules=['normalize_po_files'],
)
