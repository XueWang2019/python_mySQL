#### numpy.random.rand:
Create an array of the given shape and populate it with random samples from a uniform distribution over [0, 1).  

For example:  
split our dataset into train and test sets, 80% of the entire data for training, and the 20% for testing:

msk = np.random.rand(len(df)) < 0.8  
train = cdf[msk]  
test = cdf[~msk]  
