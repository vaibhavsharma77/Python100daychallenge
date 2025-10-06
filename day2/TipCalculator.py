print("Welcome to Tip Calculator")
amount=input("What is your total bill in euro : ")
tip=input("How much percentage you would like to tip : ")
person=input("How many people to split the bill : ")

tip_amount=((float(tip)/100)*(float(amount)))
total_cost=float(amount)+tip_amount
individual_cost=float(total_cost)/int(person)

print("Each Person has to pay",round(individual_cost,2),"for the lunch")