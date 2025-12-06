def read_lines(fn):
    with open(fn, 'r') as f:
        return [l.strip() for l in f.readlines()]


def jolt(line):
    first = max(line[:-2])
    second = max(line[line.find(first) + 1:])
    print(line, first, 'x', second)
    return int(first + second)


lines = read_lines('sample')
lines = read_lines('input')

ranges=[]
i=0
while True:
    if lines[i]=='':
        break
    ranges.append(lines[i])
    i+=1
    if i>=len(lines):
        break
ids=lines[i+1:]
print(ranges)
print(ids)

# print(lines[:5])  # preview
s = 0
for id in ids:
    # print(line)
    for r in ranges:
        start, end=r.split('-')
        if int(id)>=int(start) and int(id)<=int(end):
            s=s+1
            break

print(s)
