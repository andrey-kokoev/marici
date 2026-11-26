"""One nested extension, not a prediction of maximum orders."""
import json
from ramsey_retention_slice import D,check
P=D.parent;z=json.loads((P/'ramsey_square_44_to_66.json').read_text());a=z['red_masks'];L=[[],z['left'][:7],z['left'][7:]];R=[[],z['right'][:7],z['right'][7:]]
for t in range(7,11):
 for side,inside,outside in [(L,1,0),(R,0,1)]:
  n=len(a);side.append(list(range(n,n+3)));a.extend([0]*3)
  for j in range(n,n+3):
   for i in range(j):
    if (inside if i>=n else outside):a[i]|=1<<j;a[j]|=1<<i
M=[]
for l in range(4,11):
 row=[]
 for k in range(4,11):
  p=sum(1<<i for i in list(range(17))+sum(L[:k-3],[])+sum(R[:l-3],[]));assert check(a,p,l,k);row.append(p.bit_count())
 M.append(row)
print(M);(P/'ramsey_nested_44_to_1010.json').write_text(json.dumps(dict(orders=M,red_masks=a,k_groups=L,l_groups=R))+'\n')
