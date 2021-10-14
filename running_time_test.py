import time

# n = 5
# n = 1000
# n = 10000
#
# # Quadratic I
# tic = time.time()
# for i in range(n):
#     for j in range(n):
#         # print(f"({i},{j})",end=' ')
#         x = (i,j)
#     # print('\n')
# toc = time.time()
# print(toc-tic)


# Quadratic II - Gauss sum
# n = 5
# n = 1000
# n = 10000


# tic = time.time()
# for i in range(n):
#     for j in range(i,n):
#         # print(f"({i},{j})",end=' ')
#         x = (i,j)
#     # print('\n')
# toc = time.time()
# print(toc-tic)

# LINEAR

# n = 1000
n = 10000


tic = time.time()
for i in range(n):
    x = (i,i)
for j in range(n):
    x = (j,j)
toc =time.time()
print(toc-tic)

# FACTORIAL

(n-1)! =  -1 (mod n)

n = 1000000
fact = 1
tic = time.time()
for i in range(1,n+1):
    fact = fact * i
toc = time.time()s
print(toc-tic)
print ("The factorial of 23 is : ",end="")
print (fact)

360.93027091026306
10 ^ 6 = 11110100001001000000 in base 2, 20 cifre
