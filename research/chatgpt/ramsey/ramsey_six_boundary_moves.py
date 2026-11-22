"""Frozen BRNN/BNRN group action. Construct seed-coordinate cube via a^i b^j r^k; test adjacency in these coordinates (r swaps i,j under left action; instead put r first)."""
from ramsey_six_label_readout import E,X,sol,z3,W,m,mate,P,D,json
from itertools import combinations,product
from collections import Counter
C=list(combinations(range(4),2));ws=set()
while sol.check()==z3.sat:
    w=sum(1<<i for i,x in enumerate(X) if z3.is_true(sol.model().eval(x)));ws.add(w);sol.add(z3.Or(*[z3.Not(x) if w>>i&1 else x for i,x in enumerate(X)]))
assert sol.check()==z3.unsat and len(ws)==288

def rowpair(s):
    p=list(range(4));a,b=s.index('B'),s.index('R');c,d=[i for i,h in enumerate(s) if h=='N'];p[a],p[b]=b,a;p[c],p[d]=d,c;return p

def lift(p):
    f=[C.index(tuple(sorted(p[i] for i in c))) for c in C];q=[P.index(tuple(sorted(f[i] for i in d))) for d in P];return [E.index(tuple(sorted((q[i],q[j])))) for i,j in E]
G=list(map(lift,[rowpair('BRNN'),rowpair('BNRN'),(0,2,1,3)]));A,B,R=[{w:sum((w>>i&1)<<j for i,j in enumerate(g)) for w in ws} for g in G];seed=W(m);assert R[seed]==W(mate);assert all(set(g.values())==ws for g in (A,B,R));res={}
for name,ops in [('row_pairings',[A,B]),('pairings_and_exchange',[A,B,R])]:
    left=set(ws);comp=[]
    while left:
        w=seed if seed in left else min(left);addr={};bits=list(product((0,1),repeat=len(ops)))
        for v in bits:
            y=w
            for b,g in zip(v,ops):
                if b:y=g[y]
            addr[v]=y
        orb=set(addr.values());left-=orb;assert all(g[y] in orb for g in ops for y in orb);free=len(orb)==len(bits);edges={tuple(sorted((y,g[y]))) for y in orb for g in ops if g[y]!=y};pred={tuple(sorted((addr[v],addr[u]))) for u,v in combinations(bits,2) if sum(x!=y for x,y in zip(u,v))==1 and addr[u]!=addr[v]};assert edges==pred
        comp.append(dict(size=len(orb),simple_edges=len(edges),free_cube=free,loops=sum(g[y]==y for y in orb for g in ops),seed=w==seed))
    res[name]=dict(component_types=dict(Counter(str((c['size'],c['simple_edges'],c['loops'])) for c in comp)),seed_component=comp[0],edit_costs=[dict(Counter((w^g[w]).bit_count() for w in ws)) for g in ops],seed_costs=[(seed^g[seed]).bit_count() for g in ops]);
print(res);(D/'ramsey_six_boundary_moves.json').write_text(json.dumps(res,indent=2)+'\n')
