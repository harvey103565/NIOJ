import re
from functools import reduce

def order_weight(strng):
    # your code
    if not strng:
        return strng

    weights = re.split(r"\s+", strng)
    weights.sort()

    reg = dict()
    for weight in weights:
        num = reduce(lambda x, y: x + y, (int(d) for d in weight))
        if num in reg:
            reg[num] = reg[num] + ' ' + weight
        else:
            reg[num] = weight
    
    nums = list(reg.keys())
    nums.sort()

    results = list()
    for num in nums:
        results.append(reg[num])

    return ' '.join(results)

order1 = order_weight("") 

order1 = order_weight("103 123 4444 99 2000") 
print(order1 == "2000 103 123 4444 99")

order2 = order_weight("2000 10003 1234000 44444444 9999 11 11 22 123")
print(order2 == "11 11 2000 10003 22 123 1234000 44444444 9999")