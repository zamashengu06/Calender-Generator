# Program that accepts the name of the month and a year as input and prints out the calenger for that month
# Zamahshengu Tshabalala
# TSHZAM011
# 31 March 2024

import math

def is_leap(year):
   if year%400 != 0 and year%100 == 0 and year%4 == 0:
      leap_year = True
   elif year% 4 != 0:
      leap_year = False        
   else: 
      leap_year = True
   return leap_year

def day_of_week(day, month, year):
   d = day
   m = month
   y = year
   if m == 1 or m== 2:
      m = m +12
      y = y-1
   h = (d + 13*(m+1)//5 + y + y%100 - math.floor(y/100) + math.floor(y/400)) % 7
   result =  ((h+6)%7)+1
   return result

def month_num(month_name):
   if month_name ==  "January" or month_name == "JANUARY" or month_name == "january":
      return 1
   elif month_name ==  "Febuary" or month_name == "FEBUARY" or month_name == "febuary":
      return 2
   elif month_name ==  "March" or month_name == "MARCH" or month_name == "march":
      return 3
   elif month_name ==  "April" or month_name == "APRIL" or month_name == "april":
      return 4
   elif month_name ==  "May" or month_name == "MAY" or month_name == "may":
      return 5
   elif month_name ==  "June" or month_name == "JUNE" or month_name == "june":
      return 6
   elif month_name ==  "July" or month_name == "JULY" or month_name == "july":
      return 7
   elif month_name ==  "August" or month_name == "AUGUST" or month_name == "august":
      return 8
   elif month_name ==  "September" or month_name == "SEPTEMBER" or month_name == "september":
      return 9
   elif month_name ==  "October" or month_name == "OCTOBER" or month_name == "october":
      return 10   
   elif month_name ==  "November" or month_name == "NOVMEBER" or month_name == "november":
      return 11
   elif month_name ==  "December" or month_name == "DECEMBER" or month_name == "december":
      return 12    

def num_days_in(month_num, year):
   if month_num == 4 or month_num == 6 or month_num == 7 or month_num == 11:
      return 30
   elif month_num == 2 and is_leap(year):
      return 29
   elif month_num == 2:
      return 28
   else:
      return 31
    
def num_weeks(month_num, year):
   first = day_of_week(1,month_num,year)
   if month_num == 4 or month_num == 6 or month_num == 7 or month_num == 11:
      return 30
   elif month_num == 2 and is_leap(year):
      return 29
   elif month_num == 2:
      return 28
   else:
      return 31   
   num_weeks = math.ceil((num_days + first - 1) / 7)
   return num_week


def week(week_num, start_day, days_in_month):
   week = ''
   for i in range(7):
      day_n = (week_num - 1) * 7 + i + 1 - (start_day-1)
      if day_n < 1:
         week += ""
      elif day_n > days_in_month:
         week += ""
   else:
      if day_n < 10:
         week += " " + str(day_n) + " "
      else:
         week += str(day_n) + " "
   return week

def main():
   month= input('Enter month:\n')
   year = int(input('Enter year:\n'))
   month_n = month_num(month)
   num_weeks = num_weeks(month_num, year)
   week = 1
   print(month)
   print('Mo Tu We Th Fr Sa Su')
   for i in range(num_weeks):
      week = week(week_num, day_of_week(1, month_num_value, year),num_days_in(month_num, year))
      print(week)
      week_num += 1


if __name__=='__main__':
    main()






