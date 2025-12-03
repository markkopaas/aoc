def read_lines(fn):
    with open(fn, 'r') as f:
        return f.readlines()


def jolt(line):
    first = max(line[:-2])
    second = max(line[line.find(first) + 1:])
    print(line, first, 'x', second)
    return int(first + second)


lines = read_lines('sample')
lines = read_lines('input')

# print(lines[:5])  # preview
s = 0
for line in lines:
    # print(line)
    s = s + jolt(line)

print(s)
