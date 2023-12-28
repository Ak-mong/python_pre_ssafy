def simple_interest(P,r,t):
    return P * r * t

a = simple_interest(1100000,0.05,5/12)
print(a)
    
def simple_interest_amount(p,r,t):
    return p * ( 1 + r * t)

b = simple_interest_amount(1100000, 0.05, 5/12)
print('원리금',b)
    
