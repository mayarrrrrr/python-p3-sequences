#!/usr/bin/env python3

def print_fibonacci(length):
    # [0,1,1,2,3,5,8]
    # empty string when length is 0
    # 
    if (length == 0):
        print ([])
        return []
        
        
    if (length == 1):
        print ([0])
        return [0]
        
    fibonacci_list = [0,1]
    
    while len(fibonacci_list) < length:
        next_num = fibonacci_list[-1] + fibonacci_list[-2]
        fibonacci_list.append(next_num)
    print(fibonacci_list)
    return (fibonacci_list)
print(print_fibonacci(1))  
    
    

    