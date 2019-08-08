s = input()
l = int(input())

a = s.count('a')
mul = l//len(s)
counting = a*mul

for i in range(0, (len(s) % l)):
    if s[i] == 'a':
        counting += 1

print(counting)
