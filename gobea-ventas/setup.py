# Es una receta. Es decir, es codigo repetitivo que debemos realizar
# con cada modulo que deseamos instalar como un ejecutable. 

from setuptools import setup

setup(
    name='pv',
    version='0.1',
    py_modules=['pv'],
    install_requires=[
        'Click',
    ],
    entry_points="""
        [console_scripts]
        pv=pv:cli
    """,
)

# Para instalar: pip install --editable .
# Para saber donde quedó instalado: which pv
# pv --help
# pv clients --help