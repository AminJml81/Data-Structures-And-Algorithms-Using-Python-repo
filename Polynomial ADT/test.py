from polynomial import Polynomial

poly1 = Polynomial()
poly2 = Polynomial()
for i in range(5):
    poly1.add_term(i, i*2)
for i in range(3):
    poly2.add_term(i, i*3)

poly3 = poly1 + 5
poly4 = poly2 + poly1
poly5 = poly1 - poly2
poly6 = poly2 - poly1
print(poly3)
print(poly2)
print(poly3)
print(poly4)
print(poly5)
print(poly6)
print(poly1[4], poly1[3], poly1[2], poly1[1], poly1[0])


