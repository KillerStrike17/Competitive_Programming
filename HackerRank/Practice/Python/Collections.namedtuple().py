# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
data = namedtuple('student_record','ID MARKS CLASS NAME')

N = int(input())
avg = sum_ = 0
column_name = input().split()
for i in range(N):
    new_data = input().split()
    # print(column_name.index("ID"))
    val = data(ID = new_data[column_name.index("ID")] , MARKS = new_data[column_name.index("MARKS")], CLASS = new_data[column_name.index("CLASS")], NAME = new_data[column_name.index("NAME")])
    sum_ = sum_ + int(val.MARKS)

avg = sum_/N
print("%1.2f"%avg)
