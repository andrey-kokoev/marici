"""14-case exact certificate for two B-triangles joined by two B-defects and
exactly two mixed fillers in a hypothetical 18-node (3,6) critical graph.
Does not search graphs: iterates four possible filler neighbor choices and
a 5x5 incidence matrix under local forced incidence rules.
"""
from itertools import product,combinations
from collections import Counter
U=(0,1,2);V=(3,4,5);X=tuple(range(6,11));Y=tuple(range(11,16)); F=(16,17);N=18
pairs={frozenset((0,3)),frozenset((2,4))}
F_choices=[(0,2),(0,3),(4,2)]

def graph_from_choice(ax,bx,ay,by,rr):
    g=[[False]*N for _ in range(N)]
    def a(i,j):g[i][j]=g[j][i]=True
    for S in [X,Y]:
        for t in range(5): a(S[t],S[(t+1)%5])
    for i in U:
        for j in V:
            if (i,j) not in [(0,3),(1,4)]:a(i,j)
    for i,ids in enumerate([(1,3),(1,4),(0,2)]):
        for j in ids:a(U[i],Y[j]);a(V[i],X[j])
    for i,j,k in [(0,3,16),(1,4,17)]:a(i,k);a(j,k)
    a(16,17)
    for x,y in [(ax,16),(bx,17)]:a(X[x],y)
    for y,f in [(ay,16),(by,17)]:a(Y[y],f)
    for i in range(5):
        for j in range(5):
            if (rr[i]>>j)&1:a(X[i],Y[j])
    return g

all_cases=[]
for ax,bx in F_choices:
 for ay,by in F_choices:
  rowdeg=[2,1,2,2,2]; rowdeg[ax]-=1;rowdeg[bx]-=1
  coldeg=[2,1,2,2,2]; coldeg[ay]-=1;coldeg[by]-=1
  rows=[]
  for i,d in enumerate(rowdeg):
   opts=[]
   for bits in range(32):
    ss=frozenset(j for j in range(5) if (bits>>j)&1)
    if len(ss)!=d or (len(ss)==2 and ss not in pairs):continue
    if (i==ax and ((bits>>ay)&1)) or (i==bx and ((bits>>by)&1)):continue
    opts.append(bits)
   rows.append(opts)
  for rr in product(*rows):
   cc=[frozenset(i for i in range(5) if (rr[i]>>j)&1) for j in range(5)]
   if any(len(cc[j])!=coldeg[j] or (len(cc[j])==2 and cc[j] not in pairs) for j in range(5)):continue
   all_cases.append((ax,bx,ay,by,rr))
assert len(all_cases)==14,len(all_cases)

for ix,(ax,bx,ay,by,rr) in enumerate(all_cases,1):
 g=graph_from_choice(ax,bx,ay,by,rr)
 assert all(sum(row)==5 for row in g)
 assert not any(g[i][j] and g[i][k] and g[j][k] for i,j,k in combinations(range(N),3))
 violations=[]
 for i,j in combinations(range(N),2):
    if not g[i][j]:
      common=tuple(w for w in range(N) if g[i][w] and g[j][w])
      if len(common)>=3:violations.append((i,j,common))
 assert violations
 simplest=min(violations,key=lambda x: (len(x[2]),x[0]//6,x[1]//6))
 print(f'{ix:2}: FX={ax,bx} FY={ay,by} XY={list(rr)}  B pair {simplest[:2]} has A-witnesses {simplest[2]}')
print('CERTIFIED: all 14 residual cases violate the two-witness limit.')
