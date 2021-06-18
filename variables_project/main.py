#create a tip calculator where it displays (cost of meal, tax, total before tip, total after tip) with the cost_of_meal being whatever you want and the tax = 8%
'''
Cost before tax: X
tax: x
cost after tax: 

total:
tip:

grand total:
'''
cost_of_meal = 58
tax_percent = .08
tax = tax_percent * cost_of_meal
total_pretip = tax + cost_of_meal
tip_percentage = .15 
tip_amount = tip_percentage * total_pretip
total_after_tip = tip_amount + total_pretip

#print totals 
print ("Cost before tax: " + str(cost_of_meal))
print ("Tax: " + str(tax))
print ()
print ("Cost after tax: " + str(total_pretip))

print ("Tip: " + str(tip_amount))
print ()
print ("Grand total: " + str(total_after_tip))

#trying out string formatting % stuff

print (("""Cost before tax: %.2f
Tax: %.2f

Cost after tax: %.2f

Tip: %.2f

Grand total: %.2f""") % (cost_of_meal, tax, total_pretip, tip_amount, total_after_tip))

#turns out you have to have another () thing to print in Py 3 omegalul.

'''things I learned. 1) how to name my variables in a less confusing way. 2) different types of variables. 
3) how to print + how to print w/ formatting. 4) block commentting / single line. 5) differences between py 2 + 3. 6) Modulo'''