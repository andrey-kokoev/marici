"""Which pentagon information suffices to name an additional exchanged pair? Compare 137 completions sharing a specified four-incidence core. Additional tests are actual moving incidence orbits, not just a common count."""
from ramsey_strip_four_shared_core import targets,cores,orbits,acts,transform,D,r,Counter,defaultdict
U={u for u in orbits if orbits[u]==2};des={}
for u in U:
 p=next(p for p,a,b in acts if p!=tuple(range(6)) and transform(u,a,b)==u);hub,=[i for i in range(6) if p[i]==i];group=frozenset(pp for pp,aa,bb in acts if transform(u,aa,bb)==u);des[u]=(hub,group)
for mode in ['core','hub','cyclic subgroup']:
 tally=Counter();bycore=Counter()
 for c in targets:
    buckets=defaultdict(list)
    for u in U:
        if c<=u:buckets[None if mode=='core' else des[u][mode!='hub']].append(u)
    for us in buckets.values():
        common=set.intersection(*(set(cores[u]-c) for u in us));extras=sorted((i,j) for i,j in common if i<r[i]);tally[len(us),len(extras)]+=1
 print(mode,tally)
# Constructive rule: propagate the four decisions by rotation, then test their swap mates.
lookup={p:(a,b) for p,a,b in acts};hits=Counter();samples={};hard=Counter()
for c in targets:
 for G in {des[u][1] for u in U if c<=u}:
    forced=set.union(*(set(transform(c,*lookup[p])) for p in G));paired={(i,j) for i,j in forced-c if i<r[i] and (r[i],r[15+j]-15) in forced};hits[len(forced),len(paired)]+=1
    if not paired:
        from ramsey_strip_witness_orbits import M
        available=set(range(15))-{j for i,j in forced};rest={i:[j for j in available if D[i] in M[j]] for i in set(range(15))-{i for i,j in forced}};assert len(rest)==5 and all(len(js)==1 for js in rest.values());completed=forced|{(i,js[0]) for i,js in rest.items()};assert any(i<r[i] and (r[i],r[15+j]-15) in completed for i,j in completed-c)
        all_ext=[(n,u) for u,n in orbits.items() if forced<=u];hard[tuple(sorted(Counter(n for n,u in all_ext).items()))]+=1
    samples.setdefault(bool(paired),(sorted(c),sorted(paired),len(forced)))
print('rotation closure (forced decisions,extra pairs)',hits,'hard completions by type',hard,'examples',samples)
