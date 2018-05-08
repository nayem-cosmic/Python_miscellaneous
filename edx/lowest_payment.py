balance = 1000
annualInterestRate = .18
monthlyPayment = 0
months = 12
monthlyInterestRate = annualInterestRate/12
tBalance = balance

while tBalance>0:
    monthlyPayment += 10
    tBalance = balance
    for i in range(months):
        monthlyUnpaidBalance = tBalance - monthlyPayment
        tBalance = monthlyUnpaidBalance + monthlyUnpaidBalance*monthlyInterestRate


print("Lowest Payment:", monthlyPayment)
