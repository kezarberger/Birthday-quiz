"""
birthday.py
Author: Kezar Berger
Credit: Kotz
Assignment: 

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
name = input("Hello, what is your name? ")
month = input("Hi " + name + ", What was the name of the month you were born in? ")
year = input("And what year were you born in, " + name + "? ")
day = input("And the day? ")
if month in ["December", "January", "Febuary"]: 
    season = "winter"
if month in ["March", "April", "May"]:
    season = "spring"
if month in ["June", "July", "August"]:
    season = "summer"
if month in ["September", "October", "November"]:
    season = "fall"
if year in ["1970", "1971", "1972", "1973", "1974", "1975", "1976", "1977", "1978", "1979"]:
    decade = "stone age"
if year in ["1980", "1981", "1982", "1983", "1984", "1985", "1986", "1987", "1988", "1989"]:
    decade = "eighties"
if year in ["1990", "1991", "1992", "1993", "1994", "1995", "1996", "1997", "1998", "1999"]:
    decade = "nineties"
if year in ["2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009"]:
    decade = "21st century"
print (name + ", you are a " + str(season) + " baby of the " + str(decade) + ".")