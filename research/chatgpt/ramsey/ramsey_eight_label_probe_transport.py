"""Rooted 35-chart actual address automorphisms. Prefix masks never ranked by target values. Separate orbit ordering from invariant-color hypothesis."""
from ramsey_eight_label_blind_stars import *
from itertools import permutations
from collections import defaultdict

def group():
    inv={x:v for v,x in sig.items()};assert len(inv)==26;out=[]
    for p in permutations(L):
        d={v:sum(1<<b for a,b in zip(L,p) if mask>>a&1) for v,mask in sig.items()}
        if set(d.values())==set(inv):out.append({v:inv[x] for v,x in d.items()})
    return out

def main():
    G=group();orbs=[];seen=set()
    for e in E:
        if e not in seen:
            O=sorted({tuple(sorted(g[x] for x in e)) for g in G});orbs.append(O);seen.update(O)
    print('automorphisms',len(G),'orbits',len(orbs),'sizes',Counter(map(len,orbs)),flush=True);orders={'lex':E,'orbit_order':[x for o in orbs for x in o]};out={}
    for name,order in orders.items():
        s.push();last=0;rows=[]
        for n in (3,6,12,24,48,96):
            for e in order[last:n]:s.add(X[e]==ref[e]);
            last=n;fixed,_=fixed_links();rows.append((n,len(fixed)-n));print(name,rows[-1],flush=True)
        out[name]=rows;s.pop()
    # Modular multipliers are only a subgroup if the signature table has extra symmetries.
    from math import gcd
    M=[u for u in range(1,35) if gcd(35,u)==1 and set((u*i)%35 for i in L)==set(L)];print('multipliers',M,flush=True);s.push()
    for e in E:
        for u in M:s.add(X[e]==X[tuple(sorted(u*x%35 for x in e))])
    models=[]
    while (ans:=s.check())==z3.sat:
        m=s.model();w=sum(1<<i for i,e in enumerate(E) if z3.is_true(m.eval(X[e])));models.append(w);s.add(z3.Or(*[X[e]!=bool(w>>i&1) for i,e in enumerate(E)]))
    assert ans==z3.unsat;s.pop();w=sum(1<<i for i,e in enumerate(E) if ref[e]);assert w in models
    subsets=[{q for q in models if ((q^w)>>i)&1} for i in range(len(E))];reps=[i for i,x in enumerate(subsets) if x not in subsets[:i] and x];U=set(models)-{w};cover=next(t for n in range(len(reps)+1) for t in combinations(reps,n) if set().union(*(subsets[i] for i in t))==U);out.update(group_size=len(G),orbit_count=len(orbs),multipliers=M,invariant_models=len(models),target_minimum_probe=[(E[i],ref[E[i]]) for i in cover]);from ramsey_port_deletion_chain import independent
    valid=[]
    for q in models:
        B=[r if v not in W else r&label for v,r in enumerate(A)]
        for i,(a,b) in enumerate(E):
            if q>>i&1:B[a]|=1<<b;B[b]|=1<<a
        if not independent(B,(1<<35)-1,9):valid.append(q)
    out.update(invariant_ramsey=len(valid),only_target=valid==[w]);other=next(q for q in valid if q!=w);out['ramsey_link_differences']=(w^other).bit_count();out['chart_maps_between']=sum(all(bool(other>>E.index(tuple(sorted(g[x] for x in e)))&1)==ref[e] for e in E) for g in G);out['first_distinguishing_link']=E[next(i for i in range(len(E)) if (w^other)>>i&1)];s.push()
    for o in orbs:s.add(*[X[e]==X[o[0]] for e in o[1:]])
    out['full_group_invariance']=str(s.check());s.pop();first=orders['orbit_order'][:3];s.push();s.add(*[X[e]==ref[e] for e in first]);fixed,_=fixed_links();s.pop();out['first_three']=[(e,ref[e]) for e in first];out['first_forced']=[(e,ref[e]) for e in sorted(fixed-set(first))];print(out,flush=True);(D/'ramsey_eight_label_probe_transport.json').write_text(json.dumps(out)+'\n')
if __name__=='__main__':main()
