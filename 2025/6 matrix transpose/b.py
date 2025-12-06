def read_lines(fn):
    with open(fn, 'r') as f:
        return [l.replace('\n','')+'   ' for l in f.readlines()]


def jolt(line):
    first = max(line[:-2])
    second = max(line[line.find(first) + 1:])
    print(line, first, 'x', second)
    return int(first + second)


lines = read_lines('sample')
lines = read_lines('input')
lines=list(zip(*lines)) #transpose
print(lines)  # preview

s = 0
sums=[]
prods=[]
op=''

for line in lines:
    print(line)
    if all([c==' ' for c in line]):
        s=s+subtot
        print('empty',s)
        continue
    n=int(''.join(list(line)[:-1]))
    print('s'+str(n)+'s')
    op=line[-1]
    print(op)
    if op == '+':
        subtot=0
        oo=op
    elif op == '*':
        subtot=1
        oo=op
    if oo == '+':
        subtot+=n
        # print(i, s, op)
    elif oo == '*':
        subtot*=n
        # print(i, s, op)

#     splits=line.split()
#     if splits[0].strip()=='*' or  splits[0].strip()=='+' :
#         print(splits)
#         ops=[o.strip() for o in splits]
#         for i,op in enumerate(splits):
#
#             if op=='+':
#                 s=s+sums[i]
#                 print(i,s,op)
#             else:
#                 s=s+prods[i]
#                 print(i,s,op)
#     else:
#         cols = [ int(x) for x in splits]
#         for i in range(len(cols)):
#             print(i, cols[i])
#             if len(sums)<i+1:
#                 sums.append(0)
#             sums[i]=sums[i]+cols[i]
#             if len(prods) < i + 1:
#                 prods.append(1)
#             prods[i] = prods[i] * cols[i]
#
#         print(cols)
#     #s = s + jolt(line)
#
# print(sums, prods)
print(s)
#7329974023757 too high