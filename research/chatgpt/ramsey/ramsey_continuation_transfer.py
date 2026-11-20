"""Compare direct budget thinning with decoding from its signature; test (4,4) separately."""
from itertools import combinations, combinations_with_replacement
from collections import defaultdict

def case13():
    def trans(t,d):return sum(1<<((x+d)%13) for x in t)
    reps=((0,2,4,6),(0,2,6,9),(0,3,6,9))
    Q=[trans(t,d) for t in reps for d in range(13)]; T=[*Q[:3],*Q[13:26],Q[26],Q[29],Q[34]]
    rows=sorted({s&q for s in range(8192) for q in Q});full={s:sum(1<<i for i,q in enumerate(Q) if not s&q) for s in rows}
    for rr in (Q,rows):
        groups=defaultdict(list); falsepos=0; example=None
        for s in rr:groups[tuple(q for q in T if not q&s)].append(s)
        for s,t in combinations_with_replacement(rr,2):
            if full[s]&full[t] and all(s&q or t&q for q in T):
                falsepos+=1
                if example is None:example=(s,t)
        collisions=[(s,t,u) for g in groups.values() for s,t in combinations(g,2) for u in rr if bool(full[s]&full[u])!=bool(full[t]&full[u])];print('rows/signatures/false accepts/distinguishing collisions',len(rr),len(groups),falsepos,len(collisions))
        for label,ex in [('false accept',example),('collision',next(iter(collisions),None))]:
            if ex:print(label,[[i for i in range(13) if s>>i&1] for s in ex])

def case44(n):
    red={x*x%17 for x in range(1,17)};full=(1<<n)-1
    def monochrome(t,c):return all(((j-i)%17 in red)==c for i,j in combinations(t,2))
    assert not any(monochrome(t,c) for t in combinations(range(n),4) for c in (0,1))
    triangles=[[sum(1<<i for i in t) for t in combinations(range(n),3) if monochrome(t,c)] for c in (0,1)]
    # Independent subset recurrence: clique number after adding vertex i is max
    # of old clique number and 1 + clique number on its old neighbors.
    omega=[]
    for c in (0,1):
        adj=[sum(1<<j for j in range(i) if (((i-j)%17 in red)==c)) for i in range(n)];v=bytearray(1<<n)
        for s in range(1,1<<n):
            i=s.bit_length()-1;t=s^(1<<i);v[s]=max(v[t],1+v[t&adj[i]])
        omega.append(v)
    count=0
    for s in range(1<<n):
        ok=not any((s&t)==t for t in triangles[1]) and not any(((full^s)&t)==t for t in triangles[0]);assert ok==(omega[1][s]<3 and omega[0][full^s]<3);count+=ok
    print('Paley prefix, triangle counts, valid columns:',n,list(map(len,triangles)),count)

if __name__=='__main__':case13();case44(16);case44(17)
