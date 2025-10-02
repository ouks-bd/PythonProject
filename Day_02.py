"""
len("hello")
print(type("hello"))
print(int("24")+int("43"))



name_of_the_user = input("What is your name?")
lengthof_name_of_the_user = len(name_0of_the_user)


print(type("numbers of letters in your name:"))
print(type(lengthof_name_of_the_user))
print("numbers of letters in your name:"+str(lengthof_name_of_the_user))


height = 6.1
weight = 98

# Write your code here.
# Calculate the bmi using weight and height.
bmi = weight / (height)

print(round(bmi))
"""

print("Wellcome to the tip calculator!")
#input("what was your total bill? $")
bill = float(input("What is your total bill?"))
tip=int(input("how much tip you like to give? 10 12 15"))
people=int(input("how many people you spilt the bill?"))

tip_as_per= tip / 100
total_tip_amount= bill*tip_as_per
total_bill=bill+ total_tip_amount
bill_split_person=total_bill/people
final_bill=round(bill_split_person,2)
#2 decimal places
print(f"each person should pay: ${final_bill}")

#print("each person should pay:" + str(total_bill))