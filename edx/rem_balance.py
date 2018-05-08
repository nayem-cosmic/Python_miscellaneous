balance = 5000
annualInterestRate = .18
monthlyPaymentRate = .02
months = 12

for i in range(months):
    monthlyInterestRate = annualInterestRate/12
    minMonthlyPayment = monthlyPaymentRate*balance
    monthlyUnpaidBalance = balance - minMonthlyPayment
    balance = monthlyUnpaidBalance + monthlyUnpaidBalance*monthlyInterestRate

print(balance)
