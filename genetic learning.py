import math as m
import random
import time as t

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
strings = []
dummy = []

fitness = []

target = ['h','e','l','l','o','w','o','r','l','d']

def median(lst):
    n = len(lst)
    s = sorted(lst)
    return (sum(s[n//2-1:n//2+1])/2.0, s[n//2])[n % 2] if n else None


def mix(list1, list2):
    tem = [list1[0], list1[1], list1[2], list1[3], list1[4], list2[5], list2[6], list2[7], list2[8], list2[9]]
    if(random.random() < 0.1):
        tem[random.randint(0,9)] = letters[random.randint(0,len(letters)-1)]
    return tem

for i in range(100):
    for j in range(10):
        dummy.append(letters[random.randint(0,len(letters)-1)])
    strings.append(dummy)
    dummy = []
    fitness.append(0)

#print(strings)

for j in range(100):
    for i in range(100):
        fitness[i] = 0
    count = [0,0,0,0,0,0,0,0,0,0,0]
    living = []
    num = 0
    cunt = 0
    temp = []

    for i in range(len(strings)):
        for j in range(len(strings[i])):
            if(strings[i][j] == target [j]):
                fitness[i] += 1

    med = median(fitness)

    for i in range(len(fitness)):
        count[fitness[i]] += 1

    for i in range(len(count)): 
        num += count[i]
        if(i == med):
            overshoot = num-50 


    for i in range(len(fitness)):
        if(fitness[i] > med):
            living.append(i)
            #print(fitness[i])
        elif (overshoot > cunt and fitness[i] == med):
            cunt += 1
            living.append(i)
            #print(fitness[i], 'a')

    for i in range(25):
        temp.append(mix(strings[living[2*i]], strings[living[2*i+1]]))
        temp.append(mix(strings[living[2*i+1]], strings[living[2*i]]))
        temp.append(mix(strings[living[2*i]], strings[living[2*i+1]]))
        temp.append(mix(strings[living[2*i+1]], strings[living[2*i]]))
        
##        temp.append(mix(strings[living[i]], strings[living[len(living)-i-1]]))
##        temp.append(mix(strings[living[len(living)-i-1]], strings[living[i]]))
##        temp.append(mix(strings[living[i]], strings[len(living)-i-1]))
##        temp.append(mix(strings[living[len(living)-i-1]], strings[living[i]]))        

    for i in range(len(strings)):
                    strings[i] = temp[i]
    print("".join(strings[0]))
    #t.sleep(0.3)
    #print(count)
print('//////////////////////////////////////////////////////////')
#for i in range(len(strings)-1):
    #print("".join(strings[i]))
#print(count)
#print(med)

