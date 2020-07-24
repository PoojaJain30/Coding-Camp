# reverse array of char

# with reverse method space complexity o(1) and time complexity o(n)

def rever_array(char):
    char.reverse()
    return char

# with slicing time complexity o(k) :k is the size of slice in this case o(n) and space complexity o(1)

def rever_array1(char):
    #print("2nd fun",char)
    return char[::-1]

inp1 = ["h","e","l","l","o"]
inp2 = ["H","a","n","n","a","h"]

print(rever_array(inp1))
print(rever_array(inp2))
print(rever_array1(inp1))
print(rever_array1(inp2))