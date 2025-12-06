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

# print(lines[:5])  # preview
s = 0
sums=[]
prods=[]
for line in lines:
    # print(line)
    splits=line.split()
    if splits[0].strip()=='*' or  splits[0].strip()=='+' :
        print(splits)
        ops=[o.strip() for o in splits]
        for i,op in enumerate(splits):

            if op=='+':
                s=s+sums[i]
                print(i,s,op)
            else:
                s=s+prods[i]
                print(i,s,op)
    else:
        cols = [ int(x) for x in splits]
        for i in range(len(cols)):
            print(i, cols[i])
            if len(sums)<i+1:
                sums.append(0)
            sums[i]=sums[i]+cols[i]
            if len(prods) < i + 1:
                prods.append(1)
            prods[i] = prods[i] * cols[i]

        print(cols)
    #s = s + jolt(line)

print(sums, prods)
print(s)
