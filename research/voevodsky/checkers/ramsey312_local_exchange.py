"""Test whether a first support can be charged irrevocably to an anchor, with a single legal charging of its entire link. Edges recomputed from raw independent tens."""
from ramsey312_google_two_step import *
from collections import Counter

def main():
 row=next(l.split() for l in (D/'ramsey312_five_neg_domains.txt').open() if l.startswith('18 37 39 41 44 '));d=list(map(int,row[:5]));s=list(map(int,row[7:]));h=F^sum(1<<i for i in d);A=[s.index(adj[i]&h) for i in d];ts=list(sets(h,10));miss=[sum(1<<j for j,t in enumerate(ts) if not t&x) for x in s];assert len(set(s))==len(s)==82 and all(miss) and all(s)
 N=[{j for j,y in enumerate(s) if not x&y or not miss[i]&miss[j]} for i,x in enumerate(s)];B=[{k for k,v in enumerate(A) if v not in n} for n in N];hist=Counter();tight=Counter();samples=[];cert=[]
 # Tight families Q are the only ones whose current union is already at capacity. Every surviving candidate must contribute a fresh blocker.
 def walk(q,c,u):
    if len(q)==len(u):
        tight[len(q)]+=1;assert all(B[x]-u for x in c)
    for i in sorted(c):walk(q+[i],{j for j in c&N[i] if j>i},u|B[i])
 walk([],set(range(len(s))),set())
 for i,n in enumerate(N):
    wins=[]
    for k in B[i]:
        lit=lambda j,c:5*j+c+1
        with Solver(name='g4') as sl:
            for j in n:sl.add_clause([lit(j,c) for c in B[j]-{k}]);
            for j in n:
                for z in n&N[j]:
                    if j<z:
                        for c in B[j]&B[z]-{k}:sl.add_clause([-lit(j,c),-lit(z,c)])
            if sl.solve():
                m=set(sl.get_model());assignment={j:next(c for c in B[j]-{k} if lit(j,c) in m) for j in n};assert all(assignment[j]!=assignment[z] for j in n for z in n&N[j]);wins.append(k);cert.append(dict(pivot=i,charge=k,assignment=assignment))
    hist[len(B[i]),len(wins)]+=1
    if not wins:samples.append(i)
 residual={i:next(iter(B[i])) for i in samples};assert all(residual[i]!=residual[j] for i in samples for j in N[i]&set(samples));edges=[(i,j) for i in samples for j in samples if i<j and j in N[i]]
 out=dict(residual_charge=residual,residual_edges=edges,d=d,supports=s,anchors=A,tight=dict(tight),hist={str(k):v for k,v in sorted(hist.items())},unresolved=samples,cert=cert);(D/'ramsey312_local_exchange.json').write_text(json.dumps(out));print('tight',tight,'hist',hist,'unresolved',samples)
if __name__=='__main__':main()
