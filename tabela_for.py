# Automatizar isso usando um for
# print("| 1 | 2 | 3 |")
# print("| 4 | 5 | 6 |")
# print("| 7 | 8 | 9 |")
for i in range(1, 10):
  print("|", i, end =" ")
  if i%3==0:
    print("|\n", end ="")
