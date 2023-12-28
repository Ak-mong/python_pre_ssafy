def compound_interest_amount(p,r,t,n):
    return p * (1 + r/n)**(n * t)

a = compound_interest_amount(1500000, 0.043, 6, 4)
print(a)

b = compound_interest_amount(1500000, 0.043, 6, 1/2)
print(b)
