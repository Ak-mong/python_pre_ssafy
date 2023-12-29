def primeNumber(num):
    N= list(range(2,num+1))
    N2 = N[:] # N을
    emptyList =[]
    for s in N2: #N 으로 둘 경우
                 #인덱스 순서대로 숫자가 올라가는 반면 인덱스의 값들이 제거되기 때문에
                 # 모든 인덱스를 확인하는 작업이 이루어지지 않
        if s < 10:
            if s != 2 and s % 2 == 0: N.remove(s)
            elif s != 3 and s % 3 == 0: N.remove(s)
            else: emptyList.append(s)
        else:
            if s%2 !=0 and s%3 != 0 and s%5!=0 and s%7 != 0:
                emptyList.append(s)
    return emptyList

print(primeNumber(30))
