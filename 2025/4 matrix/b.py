def read_lines(fn):
    with open(fn, 'r') as f:
        return f.readlines()


def hasneighbour(i,coli,lines):
    ll=len(lines)
    cl=len(lines[i])
    if lines[i][coli]=='.':
        return 0
    count = 0
    if i>0 and coli>0 and lines[i-1][coli-1]=='@':
        count+=1
    if i > 0 and coli > -1 and lines[i - 1][coli] == '@':
        count += 1
    if i > 0 and coli < cl-1 and lines[i - 1][coli+1] == '@':
        count += 1
    if i > -1 and coli > 0 and lines[i][coli-1] == '@':
        count += 1
    if i > -1 and coli <cl-1  and lines[i][coli+1] == '@':
        count += 1
    if i <ll-1  and coli > 0 and lines[i + 1][coli-1] == '@':
        count += 1
    if i <ll-1 and coli > -1 and lines[i + 1][coli] == '@':
        count += 1
    if i <ll-1 and coli < cl-1 and lines[i + 1][coli+1] == '@':
        count += 1
    if count>3:
        return 0
    else:
        print(i,coli)
        return 1


lines = read_lines('sample')
lines = read_lines('input')

# print(lines[:5])  # preview
s = 0
while True:
    removed=0
    for i in range(len(lines)):
        for j in range(len(lines)):
            # print(line)
            hn=hasneighbour(i,j, lines)
            if hn==1:
                removed=1
                lines[i]=lines[i][:j] + '.' + lines[i][j + 1:]
            print('removed', i, j)
            s = s +hn
    #break
    if removed==0:
        break
print(s)
