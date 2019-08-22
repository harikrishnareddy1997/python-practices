def fact(n):
  """ Function to find factorial """
  if n == 1:
    return 1
  else:
    return (n * fact(n-1))


def check_num(a):

  """ Function to check positive/Negative number """
  if a > 0:
    print (a ," is a positive number.")
  elif a == 0:
    print ("Number is zero.")
  else:
    print (a ," is negative number.")



