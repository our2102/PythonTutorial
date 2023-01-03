s = 'abc'
t = 'ahbhc'
len_t = 0
len_s = 0
counter = 0
while len_s < len(s) and len_t < len(t):
    if s[len_s] == t[len_t]:
        len_s += 1
        counter += 1
    len_t += 1
if counter == len(s):
    print(True)
else:
    print(False)            