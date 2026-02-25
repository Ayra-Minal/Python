from collections import Counter

s = "racecar"
c = Counter(s)
t = "carrace"
c2 = Counter(t)
print(c)
print(c2)
print(c == c2)