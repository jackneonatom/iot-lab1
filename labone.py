# def parallel(resistors):
#     for r in (resistors):
#             total_inverse = sum(1 / r)
#             equivalent_resistance = 1 / total_inverse
#             print(equivalent_resistance)
#             return 

#             parallel([3,4,5])

def parallel(r):
    count=0
    eqr=0
    for i in r:
        count=count+1
        if count==len(r):
            
            total=1/sum(i)
            eqr=1/total
        else:
            print(" ")
    return total
parallel([330, 1000, 2200])