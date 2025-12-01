def read_lines(fn):
    with open(fn, 'r') as f:
        return f.readlines()


lines = read_lines('input')
#lines = read_lines('sample')
pos = 50
count = 0
clicks = 0
nulls =0
print(lines[:5])  # preview
for line in lines:
    signsymbol, distance = line[0], int(line[1:])
    sign = 1 if signsymbol == 'R' else -1
    for i in range(distance):
        pos = (pos + sign) % 100
        if pos == 0:
            count = count + 1

print("b", count)
