a = int(input('Enter first number: ') ) 
b = int(input('Enter second number: ')  )

print(a,b)


a = int(input('Enter first number: ') ) 
b = int(input('Enter second number: ')  )

 print(a,b)



# # Function definition is here
def sum( arg1, arg2 ):
  # Add both the parameters and return them."
  total = arg1 + arg2
  print ("Inside the function : ", total)
  return total

# Now you can call sum function
total = sum( a, b )
print ("Outside the function : ", total )
