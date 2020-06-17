### When we deal with data in python, it is important to understand what kind of datatype we deal with
For example: df: DataFrame  
* df['col1']: series
* df['col1'].values: values is property,Return a Numpy representation of the DataFrame. 
* df['col1'].value_counts(): value_counts is methode.
* df.cols.values: Return Series as ndarray or ndarray-like depending on the dtype.
* df['col1'][0]: 




#### Error
* df['col1'](0): TypeError: 'Series' object is not callable
