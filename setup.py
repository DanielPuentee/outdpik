
from distutils.core import setup
setup(
  name = 'pyodv',        
  packages = ['pyodv'],   
  version = '1.0',     
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'The fundamental toolkit for outliers search and visualization',   
  author = 'DanielPuentee',                   # Type in your name
  author_email = 'daniel.puenteviejo@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/DanielPuentee/pyodv',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/DanielPuentee/pyodv/archive/refs/tags/v_1.0.tar.gz',    # I explain this later on
  keywords = ['OUTLIERS', 'VISUALIZATION', 'PANDAS'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'pandas',
          'numpy',
          'seaborn',
          'scipy',
          'matplotlib',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license    #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)