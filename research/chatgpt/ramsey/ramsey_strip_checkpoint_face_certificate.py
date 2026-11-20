"""Five-case certificate for checkpoint ambiguity, from the prism's face twists and fixed spine alone. No cage numbering, prefix census or path enumeration. Labels (v,bit) are the two lifts; midpoint candidates use only three neighbor expansions."""
from collections import defaultdict
N=defaultdict(set)
def link(a,b):N[a].add(b);N[b].add(a)
def liftedge(a,b,twist):
 for bit in (0,1):link((a,bit),(b,bit^twist))
for i,(a,b) in enumerate(zip('abcd','bcda')):
 for layer in (0,1):
    liftedge(a+str(layer),b+str(layer),int(i==3)^layer);liftedge(a+str(layer),a.upper(),0)
 for sheet in (0,1):link((a.upper(),sheet),a.upper()+'*')
for a,b in [('A*','AC'),('C*','AC'),('AC','BD'),('BD','B*'),('BD','D*')]:link(a,b)
assert len(N)==30 and all(len(x)==3 for x in N.values());
def sphere(a,used):
 reached={a};front={a}
 for _ in range(3):
    front=set.union(*(N[v] for v in front))-used-reached if front else set();reached|=front
 return front
for word in ('AabBbcCcdD','AabcCcbadD','AadcCcbadD','AadcbBbadD','AadcbBbcdD'):
 layer=0;w=[]
 for i,x in enumerate(word):
    if x.isupper():w.append(x);layer^=int(0<i<9)
    else:w.append(x+str(layer))
 p=['A*',('A',0)]
 for v in w[1:]:x,=[n for n in N[p[-1]] if isinstance(n,tuple) and n[0]==v];p.append(x)
 p+=['D*'];q=['A*']+[(x,1-y) for x,y in p[1:-1]]+['D*'];extra=[]
 for k,b in ((4,10),(7,1)):
    used=set(p)|set(q[1:4] if k==4 else q[8:11]);m=sphere(q[k],used)&sphere(q[b],used);assert q[11-k] in m;extra.append(sorted(m-{q[11-k]}))
 spare={'B','C'}-set(w);bad=[u for u in spare if u.lower()+'0' in w and u.lower()+'1' in w];assert [v[0] for block in extra for v in block]==bad
 print(word,'check 4 extra',extra[0],'check 7 extra',extra[1])
