def calcul_moyenne(*arg):
    moy=sum(arg)/len(arg)
    return moy
print(calcul_moyenne(12,34,15,67,78))


def eval(numbers):
    total = 0
    count=0
    for num in numbers:
        total+=num
        count+=1
    return total/count
numbers=[12,34,15,67,78]
print(eval(numbers))