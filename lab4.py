def find_number(nums):
    seen = set()
    for n in nums:
        if n in seen:
            seen.remove(n)   
        else:
            seen.add(n)     
    return seen


arr = list(map(int, input("Entr a list: ").split()))
print("Single a number: ", find_number(arr))