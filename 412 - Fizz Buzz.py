def fizzBuzz(n):
    result = []

    for i in range(1,n+1):

        if i%5 == 0 and i%3 == 0:
            result.append('FizzBuzz')
        elif i%3 == 0:
            result.append('Fizz')
        elif i%5 == 0:
            result.append('Buzz')
        else:
            result.append('%s'%i)
    
    return result


    # def fizzBuzz(self, n):
    #     """
    #     :type n: int
    #     :rtype: List[str]
    #     """
    #     ls=[]
    #     for i in range(1,n+1):
    #         if i%3==0 and i%5==0:ls.append("FizzBuzz")
    #         elif i%3==0:ls.append("Fizz")
    #         elif i%5==0:ls.append("Buzz")
    #         else:ls.append(str(i))
    #     return ls