def isLeapYear(year):
 if(year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
  return True
 else:
    return False
year = int(input("Enter a year : "))

if isLeapYear(year):
   print('{} is a leep year.'.format(year))
else:
    print('{} is not a leep year.'.format(year))
