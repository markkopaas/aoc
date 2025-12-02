def read_lines(fn):
    with open(fn, 'r') as f:
        return f.readlines()

def all_equal(li):
    for x in li[1:]:
        if x != li[0]:
            return False
    return True

def inPair(x):
    l=len(str(x))
    for d in range(1,l//2+1):
        if l%d==0:
            li=[int(x[i:i+d]) for i in range(0,l,d)]
            if all_equal(li):
                return True
    return False

lines = read_lines('sample')
lines = read_lines('input')
ranges=lines[0].split(',')

# print(ranges[:5])  # preview
sum=0
for rang in ranges:
    # print(rang)
    start, end=rang.split('-')
    for z in range(int(start),int(end)+1):
        # print(z)
        if inPair(str(z)):
            sum=sum+z
print(sum)