rent= int(input("Enter the amount of rent: "))
food= int(input("Enter the amount of total food: "))
Electricity= int(input("Enter the total electricity spend: "))
charge_per_unit= int(input("Enter the charge of per unit: "))
person= int(input("Enter the number of person in room: "))

electricity_bill = Electricity*charge_per_unit

output= (rent + food + electricity_bill) // person

print(output)