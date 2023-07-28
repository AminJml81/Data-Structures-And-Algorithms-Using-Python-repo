from liststack import Stack
from balanced_delimiter import check_delimiters

# expression1 = '(5+6-3)'
# expression2 = '(5+(6-3))'
# expression3 = '(5(+6)-(3))'
# expression4 = '(5+((6-3))'
# expression5 = ')'
#
#
# expressions = [expression1, expression2, expression3, expression4, expression5]
# for expression in expressions:
#     print(check_delimiters(expression=expression))

files = ['liststack.py', 'pyliststack.py', 'GuessNum.java']
for file in files:
    print(check_delimiters(file=file))
