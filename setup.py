

from setuptools import setup

APP_NAME = 'Pdf Corgi'
APP = ['App.py']
DATA_FILES = []
OPTIONS = {
    'resources': [
        'CalcUI.ui',
        'Resources/Avangard_4.csv',
        'Resources/Avangard_TEEN.csv',
        'Resources/Motus_2_CS.csv',
        'Resources/Motus_2_CV.csv',
        'Resources/SavedPath.txt'],
    'packages': ['PyPDF2', 'timeit', 'csv'],
    'argv_emulation': True
}

setup(
    app=APP,
    name=APP_NAME,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
