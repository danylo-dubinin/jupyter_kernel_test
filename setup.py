from setuptools import setup

from jupyter_kernel_test import __version__

setup(
    name = 'jupyter_kernel_test',
    version = __version__,
    description = "README.rst",
    author = "Jupyter Development Team",
    author_email = "jupyter@googlegroups.com",
    home_page = "https://github.com/jupyter/jupyter_kernel_test",
    packages = ['jupyter_kernel_test'],
    install_requires = [
        'tornado', # [1]
        'jupyter_kernel_mgmt>=0.3',
        'jupyter-protocol',
        'jsonschema',
    ],
    python_requires = '>=3.4',
)

# ## References
# [1]: `tornado` is not included in original project.toml but is explicitly
#   imported
