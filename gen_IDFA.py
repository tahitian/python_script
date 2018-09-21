import random


seed = '1234567890ABCDEF'
IDFA = ''.join(random.choices(seed, k=8))+'-'+''.join(random.choices(seed, k=4))+'-'+''.join(random.choices(seed, k=4))+'-'+''.join(random.choices(seed, k=4))+'-'+''.join(random.choices(seed, k=12))
print(IDFA)