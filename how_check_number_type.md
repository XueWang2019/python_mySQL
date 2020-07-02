#### how to check a number in python is one of the integer type. In Pthon, you want to use the type of a number in logic check, how:

#### Below is ok:
 if type(2) == int:
    print(2)  

#### But as below is wrong

np.ones(1)[0]
1.0

type(np.ones(1)[0])
numpy.float64

if int(1.0)==1.0:
2
    print('1.0 is int')
1.0 is int

#### Solution:
You can use isinstance with a tuple argument containing the types of interest.

To capture all python and numpy integer types use:

isinstance(value, (int, np.integer))

example:
vals = [3, np.int32(2), np.int64(1), np.float64(0)]
[(e, type(e), isinstance(e, (int, np.integer))) for e in vals]
