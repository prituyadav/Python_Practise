array=[1,2,3,5,5]
for x in array:
    if(x==5):
        break
    else:
        print(x)
        
        
        
print("range function---")

for x in range(1,6):
     print(x)

        
        
print("else in for loop")
for x in range(6):
  print(x)
else:
  print("Finally finished!")
  

    
    
print("pass in loop---it will remain empty loop without any error") 
 
 for x in [0, 1, 2]:
  pass 



  print("nested loop")
  
  adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
