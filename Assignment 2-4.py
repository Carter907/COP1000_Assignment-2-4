# input statements
salary = float(input())
numDependents = float(input())

# calculate taxes here
stateTax = .065 * salary
federalTax = .280 * salary
dependentDeduction = 0
for i in range(int(numDependents)):
    dependentDeduction+=.025 * salary;

totalWithholding = stateTax + federalTax + dependentDeduction
takeHomePay = salary - totalWithholding

# output statements
print("State Tax: $" + str(stateTax))
print("Federal Tax: $" + str(federalTax))
print("Dependents: $" + str(dependentDeduction))
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))
