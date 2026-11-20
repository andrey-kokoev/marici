"""Route-free secant test on induced residuals of the duad/partition graph. Any outside vertex has >=2 outside neighbors (lies on cycle), hence all common neighbors of same-side residual pairs must themselves be residual. Reduce left four-duad sets up to S6; classify candidates without listing half-routes."""
from itertools import combinations,permutations
from collections import Counter
D=list(combinations(range(6),2));M=[set(x) for x in combinations(range(15),3) if len(set(sum((D[i] for i in x),())))==6];N=[{j for j,m in enumerate(M) if i in m} for i in range(15)];S={frozenset(x) for x in combinations(range(15),4)};perms=[[D.index(tuple(sorted((p[a],p[b])))) for a,b in D] for p in permutations(range(6))];out=Counter();bad=[]
while S:
 A=min(S,key=lambda a:tuple(sorted(a)));orb={frozenset(p[i] for i in A) for p in perms};S-=orb
 forced={j for j,m in enumerate(M) if len(m&A)>=2};
 if len(forced)>4:continue
 for extra in combinations(set(range(15))-forced,4-len(forced)):
    B=forced|set(extra)
    if any(len(N[i]&B)>1 for i in set(range(15))-A):continue
    if any(not N[i]&B for i in A) or any(not M[j]&A for j in B):continue
    mat=sum(all(i in M[j] for i,j in zip(sorted(A),p)) for p in permutations(B));out[mat]+=len(orb)
    if mat!=1:bad.append((A,B,mat,len(orb)))
print('secant-closed without isolates, grouped by matching count:',out,'exception representatives',len(bad));print(bad[:5])
for A,B,m,w in bad:
 G={**{i:{15+j for j in N[i]-B} for i in set(range(15))-A},**{15+j:M[j]-A for j in set(range(15))-B}};F={v:{u for u in ns if len(ns)==2 or len(G[u])==2} for v,ns in G.items()};todo=set(F);cc=[]
 while todo:
    v=todo.pop();comp={v};stack=[v]
    while stack:
        ns=F[stack.pop()]&todo;todo-=ns;comp|=ns;stack.extend(ns)
    cc.append((len(comp),min(len(F[v]) for v in comp),max(len(F[v]) for v in comp)))
 # A spanning cycle must omit exactly one link at each degree-three vertex and none at degree two.
 H={v for v in G if len(G[v])==3};types=Counter()
 def covers(todo,omit):
    if todo:
        v=min(todo)
        for u in G[v]&todo:covers(todo-{u,v},omit|{(v,u),(u,v)})
        return
    todo=set(G);lengths=[]
    while todo:
        v=todo.pop();stack=[v];k=1
        while stack:
            v=stack.pop();ns={x for x in G[v]&todo if (v,x) not in omit};k+=len(ns);todo-=ns;stack.extend(ns)
        lengths.append(k)
    types[tuple(sorted(lengths))]+=1
 covers(H,set());print(m,w,'cycle-cover sizes',types);assert (22,) not in types
