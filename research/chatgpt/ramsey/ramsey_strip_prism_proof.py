"""Verify the quotient model and enumerate the five cases without closure labels or route files."""
from itertools import combinations
X=list(combinations(range(4),2));P=list(combinations(range(6),2));T=[t for t in combinations(P,3) if len(set(sum(t,())))==6];g=(0,2,1,3);e=[X.index(tuple(sorted(g[i] for i in x))) for x in X];tr=lambda p:tuple(sorted(e[i] for i in p));r=[P.index(tr(p)) for p in P]+[15+T.index(tuple(sorted(map(tr,t)))) for t in T];rep=lambda x:min(x,r[x]);labels={16:'A',3:'B',18:'C',4:'D',10:'a0',23:'b0',2:'c0',22:'d0',12:'a1',20:'b1',1:'c1',19:'d1'};E=set();edge=lambda x,y:tuple(sorted((x,y)));ext={}
for i,p in enumerate(P):
 for j,t in enumerate(T,15):
    if p not in t:continue
    x,y=rep(i),rep(j)
    if x in labels and y in labels:E.add(edge(labels[x],labels[y]))
    elif (x in labels)!=(y in labels):ext.setdefault(y if x in labels else x,set()).add(labels.get(x,labels.get(y)))
expected={edge(x+k,y+k) for k in '01' for x,y in zip('abcd','bcda')}|{edge(x.upper(),x+k) for x in 'abcd' for k in '01'};assert E==expected and ext=={0:{'A'},14:{'C'},26:{'B'},29:{'D'}}
V=set(labels.values());cases=[]
def grow(p):
 if p[-1]=='B':
    if len(p)==10:
        u,v=sorted(V-set(p));bits=p[2][0]=='b',p[-3][0]=='a';ok=edge(u,v) in E;assert ok==(bits[0]==bits[1]);cases.append((p,u,v,bits,ok))
    return
 for x in sorted(V-set(p)):
    if edge(x,p[-1]) in E:grow(p+[x])
grow(['A','a0']);assert len(cases)==5
for p,u,v,bits,ok in cases:print(' '.join(p),'|',u,v,'|',bits,ok)
