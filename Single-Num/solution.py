from functools import reduce

#Single num

# Brut Force method time complexity linear O(n) but needed extra space
def single_num(arr):
    valid = dict()
    for i in range(len(arr)):
        if arr[i] not in valid:
            valid[arr[i]] = True
        else:
            valid[arr[i]] = False
    #print(valid)
    for key,value in valid.items():
        if value == True:
            return key
    return None

print(single_num([2,2,1]))
print(single_num([4,1,2,1,2]))


# using xor bitwise operation

def single_num1(arr):
    result = arr[0]
    for i in range(1,len(arr)):
        result ^= arr[i]
    return result

print('---',single_num1([2,2,1]))
print('---',single_num1([4,1,2,1,2]))



# more readable efficient way
def single_num2(arr):
     return reduce((lambda x,y: x ^ y),arr)


print('------',single_num2([2,2,1]))
print('------',single_num2([4,1,2,1,2]))