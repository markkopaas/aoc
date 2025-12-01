def read_lines():
    with open('input','r') as f:
        return f.readlines()

lines = read_lines()
pos=50
count=0
print(lines[:5])  # preview
for line in lines:
    signsymbol, distance = line[0], int(line[1:])
    sign = 1 if signsymbol == 'R' else -1
    pos=(pos+sign*distance+100)%100
    if pos==0:
        count=count+1
print(count)