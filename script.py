#1 Overall cost of the meal in USD
meal = 44.50 

#2 Converting tax percentage into a decimal number
percentagetax = 6.75
tax = percentagetax / 100

#3 Converting percentage tip into a decimal number
percentagetip = 15.0
tip = percentagetip / 100

#4 Reassigning meal, after tax. 
meal += tax


#5 Total cost
total = meal + meal*tip

#6 Printing out the total 
print(total)