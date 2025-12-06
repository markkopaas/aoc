def read_lines(fn):
    with open(fn, 'r') as f:
        return [l.strip() for l in f.readlines()]


def contains(first,second,ranges):
    return ranges[second][0] <= ranges[first][0] <= ranges[first][1] <= ranges[second][1]

def overlap(first,second,ranges):
    return ranges[second][0] <= ranges[first][0] <= ranges[second][1] or  ranges[second][0] <= ranges[first][1] <= ranges[second][1]

lines = read_lines('sample')
lines = read_lines('input')

ranges=[]
i=0
while True:
    if lines[i]=='':
        break
    start, end=lines[i].split('-')

    ranges.append([int(start),int(end)])
    i+=1
    if i>=len(lines):
        break
ids=lines[i+1:]
print(ranges)
print(len(ranges))

# print(lines[:5])  # preview
s = 0
    # print(line)
u=[]
removed=[]
i=0
while i<len(ranges)-1:
    if i in removed:
        print('skip outer', i2)
        i+=1
        continue
    i2=i+1
    while i2<len(ranges) and i<len(ranges)-1:
        if i2 in removed or i in removed:
            i2+=1
            print('skip inner',i2)
            continue
        #join means update and remove the second
        print(i,i2)
        if overlap(i,i2,ranges):
            ranges[i2]=[min(ranges[i][0],ranges[i2][0]),max(ranges[i][1],ranges[i2][1])]
            removed.append(i)
            print('joined', i,i2, ranges[i], ranges[i2])
            #i+=1
            #i2+=i+1
            continue #next i2
        if contains(i, i2, ranges):
            removed.append(i)
            print('removed f', i, ranges[i], ranges[i2])
            i=i+1
            i2=i+1
            continue #next i
        if contains(i2,i,ranges):
            removed.append(i2)
            print('removed sec', i2, ranges[i], ranges[i2])
        i2+=1
    i+=1

for i in range(len(ranges)):
    if i in removed:
        continue
    s=s+ranges[i][1]-ranges[i][0]+1
print(s)
