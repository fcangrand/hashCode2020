# Reversing a string in Python
a ="GeeksForGeeks"
print("Reverse is", a[::-1]) 


# Chaining Of Comparison Operators.
n = 10
result = 1 < n < 20
print(result) 
result = 1 > n <= 9
print(result) 


# Return Multiple Values From Functions.
def x(): 
    return 1, 2, 3, 4
a, b, c, d = x() 
  
print(a, b, c, d) 


# Check The Memory Usage Of An Object.
import sys 
x = 1
print(sys.getsizeof(x)) 

# Print string N times.
n = 2; 
a ="GeeksforGeeks"; 
print(a * n); 

# get last element 
my_list = ['geeks', 'practice', 'contribute'] 
print(my_list[-1]) 

# join
my_list = ['geeks', 'for', 'geeks'] 
print(''.join(my_list)) 