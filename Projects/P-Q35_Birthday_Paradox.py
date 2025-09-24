import random

def check_duplicates(birthdays):

    return len(birthdays)!= len(set(birthdays))


def experiments(n,trials=1000):

    count=0
    for _ in range(trials):
        birthdays=[random.randint(1,365) for _ in range(n)]

        if check_duplicates(birthdays):
            count+=1

    return count/trials

for i in range(5,101,5):
    probability= experiments(i)
    print(f"for {i} persons group , the probablity of re-occuring birthdays will be {probability:.2f} ")