def read_lines(fn):
    with open(fn, 'r') as f:
        return f.readlines()



def jolt(line, l):
    first = max(line[:-(l)])
    if l==1:
        return first
    second = jolt(line[line.find(first) + 1:],l-1)
 #   print(line, first, 'x', second)
    return first + second


lines = read_lines('sample')
lines = read_lines('input')

# print(lines[:5])  # preview
s = 0
for line in lines:
    # print(line)
    s = s + int(jolt(line,12))

print(s)
