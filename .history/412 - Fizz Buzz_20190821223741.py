


def fizzBuzz(n):
    result = []

    for i in range(n):

        if i%5 == 0 and i%3 == 0:
            result.append('FizzBuzz')
        elif i%3 == 0:
            result.append('Fizz')
        elif i%5 == 0:
            result.append('Buzz')
        else:
            result.append('%s'%i)
    
    return result
