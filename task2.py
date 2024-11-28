#! python3
"""
###### Task 2
Ask the user to enter in the prices of 5 items in dollars.cents (eg 10.34).  Find the total value of all items and then calculate the total price including 5% GST and 7% PST

Sample:
Enter in price of item #1: 10.25
Enter in price of item #2: 11.45
Enter in price of item #3: 13.85
Enter in price of item #4: 9.25
Enter in price of item #5: 10.25
Your subtotal is 55.05
Your GST is 2.75
Your PST is 3.85
Your total is 61.65
"""
subtotal = 0
for i in range(5):
    itemnum = i + 1
    price = float(input(f'Enter in price of item #{itemnum}: '))
    subtotal = subtotal + price
print(f'Your subtotal is {subtotal}')
gst = round((subtotal * 0.05), 2)
print(f'Your GST is {gst}')
pst = round((subtotal * 0.07), 2)
print(f'Your PST is {pst}')
total = gst + pst + subtotal
print(f'Your total is {total}')

#done