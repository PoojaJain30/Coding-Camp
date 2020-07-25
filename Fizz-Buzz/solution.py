# FizzBuzz game
def str_reps(num):
    result = list()
    for i in range(1,num+1):
        if i%5 == 0 and i%3 == 0:
            result.append('FizzBuzz')
        elif i%5 == 0:
            result.append('Buzz')
        elif i%3 == 0:
            result.append('Fizz')
        else:
            result.append(str(i))
    return result

print(str_reps(27))
