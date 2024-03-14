p = "Good Evening All"

def facto():
    t,k = int(input("Enter a number: ")),1
    for i in range(1,t+1):
        k *=i
    return k 
    