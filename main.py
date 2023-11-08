def fact_rec(n):
  if n==0 or n==1:
    return 1
  else :
      return n*fact_rec(n-1)
number=2
res = fact_rec(number)
rec=fact_rec(number)
print("the factorial of {} is {}.".format(number,res))