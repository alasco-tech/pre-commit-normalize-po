from setuptools import setup


setup(
    name='normalize_po',
    version='1.1.0',
    install_requires=['polib ~= 1.1.0'],
    entry_points={
        'console_scripts': [
            'normalize-po = normalize_po_files:main'
        ]
    },
    py_modules=['normalize_po_files'],
)
