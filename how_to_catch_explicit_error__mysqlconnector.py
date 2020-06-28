
how to display the error message 

https://dev.mysql.com/doc/connector-python/en/connector-python-api-errors-error.html

except mysql.connector.Error as err:
  if err.errno == 1054:
    print("please check at original file at see whether there is empty value at certain area")
  else:
    print("Another error")
