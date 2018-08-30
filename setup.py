# setup.py
from distutils.core import setup, Extension
from distutils      import sysconfig

setup(  name='caen_plu_py',
        py_modules=['caen_plu_py.py'],
        ext_modules=[
        Extension('_caen_plu_py',
                 ['caen_plulib.i', 'caen_plulib_wrap.c'],
                   include_dirs = [],
                   define_macros = [],
                   undef_macros = [],
                   library_dirs = ['.'],
                   libraries = ['CAEN_PLUlib']
                 )
        ]
     )