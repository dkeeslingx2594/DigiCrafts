#1
count = 0 
while count in range(0,10):
    count += 1
    print count

#2
n = int(input("Where would you like to start? "))
m = int(input("Where would you like to end? "))
count = n-1
while count in range(n-1, m):
     count += 1
     print count

#3
count = 1 
while count in range(1, 10):
     print count
     count += 2

#4
count = 0 
while count < 5:
     print "*" * 5
     count += 1

#5
count = 0
big = int(input("How big is the square? "))
while count < big:
     print "*" * big
     count += 1

#6
count = 0 
h = int(input("How tall is your square? "))
w = int(input("How wide is your square?"))
print "*"*w
while count < h-2:
    print "*" + (" "*(w-2)) + "*"
    count += 1
print "*"*w

#7
count = 1
while count < 24:
    print ("*" * count).center(24)
    count += 2

#8
height = int(input("How tall is your triangle? "))
count = 1
while count < height*2:
     print ("*" * count).center(height*2-1)
     count += 2

#9
for i in range(1, 11):
    n = 1
    while n < 11:
        print str(i) + " x "+ str(n) + " = " + str(i*n)
        n += 1
