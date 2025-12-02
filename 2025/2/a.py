def read_lines(fn):
    with open(fn, 'r') as f:
        return f.readlines()

def inPair(x):
    l=len(str(x))
    if l%2>0:
        return False
    if x[0:l//2] == x[l//2:]:
        return True


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