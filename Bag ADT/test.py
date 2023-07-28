from random import randint
from linearbag import Bag
from countingbag import CountingBag

bag = Bag()
bag.add(1)
bag.add(2)
bag.add(3)
bag.add(4)
bag.add(5)
bag.add(6)
bag.add(7)

print(10 in bag)
print(5 in bag)
bag.remove(5)
for elm in bag:
    print(elm)
print(len(bag))
# bag.remove(20)

# cbag = CountingBag()
# cbag.add(1)
# cbag.add(2)
# cbag.add(2)
# cbag.add(3)
# cbag.add(3)
# cbag.add(3)
# print(cbag)
# cbag.remove(1)
# cbag.remove(1)
# cbag.remove(1)
# cbag.remove(1)
# for elm in cbag:
#     print(elm)