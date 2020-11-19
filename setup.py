import setuptools

setuptools.setup(
    setup_requires=[
        "Babel>=2.9.0",
        "pbr>=2.0.0",
    ],
    pbr=True,
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)
