import setuptools
from setuptools.command.install import install


class InstallWithCompile(install):
    def run(self):
        from babel.messages.frontend import compile_catalog

        compiler = compile_catalog(self.distribution)
        option_dict = self.distribution.get_option_dict("compile_catalog")
        compiler.domain = [option_dict["domain"][1]]
        compiler.directory = option_dict["directory"][1]
        compiler.run()
        super().run()


setuptools.setup(
    setup_requires=[
        "Babel>=2.9.0",
    ],
    cmdclass={"install": InstallWithCompile},
    package_dir={"": "src"},
    package_data={"": ["locale/*/*/*.mo", "locale/*/*/*.po"]},
    packages=setuptools.find_packages(where="src"),
)
