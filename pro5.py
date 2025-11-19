import sys

if len(sys.argv) >= 4:
    p = float(sys.argv[1])
    t = float(sys.argv[2])
    r = float(sys.argv[3])
    print("User input provided.")
else:
    p = 1000
    t = 2
    r = 2

si = (p * t * r) / 100

print("The Principal is :", p)
print("The Time is :", t)
print("The Rate is :", r)
print("The Simple Interest is :", si)
