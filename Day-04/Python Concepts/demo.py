d = "Welcome User"

def prntnumber():
    print("Printing 10 numbers")
    for i in range(1,11):
        print(i,end=",")
    return

class Student:
    '''
        Example for Student Class 
    '''
    g = "Good Evening"
    
    def read_data():
        rn = input("Enter Roll Number: ")
        gh = input("Enter Your details: ").split()
        return