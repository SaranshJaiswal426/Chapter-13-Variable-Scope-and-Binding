x = 'Hi'
def change_global_x():
 global x
 x = 'Bye'
 print(x)
change_global_x() # prints Bye
print(x)