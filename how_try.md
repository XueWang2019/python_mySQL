### with try:
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
### Without try:    
print(y)  
x=2  
print(x)  

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
