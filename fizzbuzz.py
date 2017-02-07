def fizz_buzz(numb):
  
  if numb%15 == 0: 
    return "FizzBuzz"

  elif numb%3==0:
    return "Fizz"

  elif numb%5==0:
    return "Buzz"

  else:
    return numb