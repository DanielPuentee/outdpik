
from distutils.core import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
  name = 'outdpik',        
  packages = ['outdpik'],   
  version = '1.3',     
  license= 'GNU',     
  description = 'The fundamental toolkit for outliers search and visualization',   
  author = 'Iker Cumplido',                  
  author_email = 'ikumpli@gmail.com',     
  url = 'https://github.com/DanielPuentee/outdpik',   
  download_url = 'https://github.com/DanielPuentee/outdpik/archive/refs/tags/1.3.tar.gz',   
  keywords = ['OUTLIERS', 'VISUALIZATION', 'PANDAS'],  
  long_description=long_description,
  long_description_content_type='text/markdown',
  install_requires=[           
          'pandas',
          'numpy',
          'seaborn',
          'scipy',
          'matplotlib',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',     
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU Affero General Public License v3',  
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)