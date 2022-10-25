.. prueba documentation master file, created by
   sphinx-quickstart on Tue Sep 27 14:55:03 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.
##################
Outdpik: The fundamental toolkit for outliers search and visualization
##################


.. toctree::
   :maxdepth: 2
   :caption: Contents:

.. note:: Usage in programme lenguages

   This package is only designed to be used in Python.


********************
General Parameters
********************

.. .. py:function:: def outliers(df = None, columns = "all", method = "all"):
..    :rtype: dict

.. * ``df``: The set to explore.
..   - Types: ``pandas.DataFrame``, ``pandas.Series``, ``numpy.ndarray``, ``list``
..   - Default: ``None``
.. * ``columns``: Selected columns, by default = "all". "all" parameter will return the outliers for all the numeric columns.
..    - Types: ``str``, ``list``
..    - Default: ``"all"``
.. * ``method``: Method to use for outliers search. "all" parameter will return the outliers for all the methods.
..    - Types: ``str``, ``list``
..    - Default: ``"all"``

   // .. py:class:: outdpik()


First, outdpik class is instanciated = ``outdpik = outdpik()``. It requieres no arguments.


Searching for outiers:

.. py:function:: def outliers(df, columns, method):

   It returns a dictionary with the columns selected and the outliers

   :param df: The set to explore
   :type df: pandas.DataFrame, pandas.Series, numpy.array and list, optional(default = None)
   :param columns: Selected columns, by default = "all". "all" parameter will return the outliers for all the numeric columns.
   :type columns: list and string, optional(default = "all")
   :param method: Method to use for outliers search. "iqr", "zscore" and 'all' are available. "all" parameter will return the outliers for all the methods.
   :type method: string, optional(default = "all")
   :return: Dictionary of outliers
   :rtype: dict

   .. .. code-block:: python

   ..    import outdpik as out
   ..    outdpik = out.outdpik()
   ..    outdpik.outliers(df, columns = "all", method = "all")
   
   .. warning:: The columns selected must be numeric.

Plot outiers:

.. py:function:: def outliers_plot(df, columns, method, size, palette):

   It returns a strip plot with the outliers marked in other color

   :param df: The set to explore
   :type df: pandas.DataFrame, pandas.Series, numpy.array and list, optional(default = None)
   :param columns: Selected column. Only one and numeric column can be selected.
   :type columns: list and string, optional(default = None)
   :param method: Method to use for outliers search. "iqr", "zscore" and 'all' are available. "all" parameter will return the outliers for all the methods. 
   :type method: string, optional(default = "all")
   :param size: Size of the plot. 
   :type size: list, optional(default = [5, 7])
   :param palette: Color palette to use. It must be a tuple of 3 elements each
   :type palette: tuple, optional(default = ((133/255, 202/255, 194/255), (38/255, 70/255, 83/255))))
   :return: Strip plot of the selected column
   :rtype: plt.figure

   .. .. code-block:: python

   ..    import outdpik as out
   ..    outdpik = out.outdpik()
   ..    outdpik.outliers_plot(df, columns = "all", method = "all", size = [5, 7], palette = ((133/255, 202/255, 194/255), (38/255, 70/255, 83/255))))
   
   .. warning:: The columns selected must be numeric.


.. * :ref:`genindex`
.. * :ref:`modindex`
.. * :ref:`search`
