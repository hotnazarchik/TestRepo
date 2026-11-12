def unpaired(numbers):
    for num in numbers:
        if -num not in numbers:
            print(num)
            return
unpaired([1, -1, 2, -2, 3])       
unpaired([-3, 1, 2, 3, -1, -4, -2])  
unpaired([1, -1, 2, -2, 3, 3])    
    
 