from distutils.core import setup
from Cython.Build import cythonize
setup(
    name='dnngp pyx',
    ext_modules=cythonize('dnngp.pyx')
)
