
from distutils.core import setup
setup(
  name = 'outdpik',        
  packages = ['outdpik'],   
  version = '1.1',     
  license='GNU',     
  description = 'The fundamental toolkit for outliers search and visualization',   
  author = 'Iker Cumplido',                  
  author_email = 'ikumpli@gmail.com',     
  url = 'https://github.com/DanielPuentee/outdpik',   
  download_url = 'https://github.com/DanielPuentee/outdpik/archive/refs/tags/1.1.tar.gz',   
  keywords = ['OUTLIERS', 'VISUALIZATION', 'PANDAS'],  
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
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)