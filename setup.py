from setuptools import setup


setup(
    name='cldfbench_grollemund_et_al2015',
    py_modules=['cldfbench_grollemund_et_al2015'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'grollemund_et_al2015=cldfbench_grollemund_et_al2015:Dataset',
        ]
    },
    install_requires=[
        'phlorest',
        'openpyxl',
        'cldfbench',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
