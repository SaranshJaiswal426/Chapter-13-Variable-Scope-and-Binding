a = 5 
def funct():
    a = 10
    print("local a:",a)\
    
    print("global a: ",a)
    funct()
    print("global a: ",a)
