print map(lambda x: 'FizzBuzz' if x%15 == 0 else 'Fizz' if x%3 == 0 else 'Buzz' if x%5 == 0 else x, range(100))
