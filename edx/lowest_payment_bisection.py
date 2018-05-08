balance = 1000
annualInterestRate = .18
monthlyPayment = 0
monthlyInterestRate = annualInterestRate/12
tBalance = balance
lowBound = balance/12
upBound = (balance*(1+annualInterestRate)**12)/12.0
monthlyPayment = (upBound+lowBound)/2
while abs(tBalance)>0.01:
    tBalance = balance
    for i in range(12):
        monthlyUnpaidBalance = tBalance - monthlyPayment
        tBalance = monthlyUnpaidBalance + monthlyUnpaidBalance*monthlyInterestRate
    if tBalance>0:
        lowBound = monthlyPayment
    else:
        upBound = monthlyPayment
    monthlyPayment = (upBound+lowBound)/2.0


print("Lowest Payment:", monthlyPayment)
