### with try: Since the try block raises an error, the except block will be executed.  
'''
try:  
  print(y  )
except:  
  print("An exception occurred")  
x=2  
print(x)  
'''

The output:  
'''
An exception occurred
2
'''
### Without try: Without the try block, the program will crash and raise an error:   
'''
print(y)  
x=2  
print(x)  
'''
The output:  
'''
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)  
<ipython-input-9-5630af6d0bf1> in <module>  
----> 1 print(y)  
      2 x=2  
      3 print(x)  

NameError: name 'y' is not defined  
'''
### use raise:Without the try block, the program will crash and raise an error:  
'''
x = -1  
if x < 0:  
  raise Exception("Sorry, no numbers below zero")  
x=2  
print(x)  
'''  
The output:  

'''

---------------------------------------------------------------------------
Exception                                 Traceback (most recent call last)
<ipython-input-10-02a2457f3f89> in <module>
      2 
      3 if x < 0:
----> 4   raise Exception("Sorry, no numbers below zero")
      5 x=2
      6 print(x)

Exception: Sorry, no numbers below zero  
'''
