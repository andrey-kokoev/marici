"""Look at order 14: exactly three new addresses needed. Compare complete tables."""
from ramsey_36_try_deck import data,unpack
from itertools import combinations,permutations,product
from functools import lru_cache
from random import Random

def table(g):
    ind=[0]
    for i,ns in enumerate(g.get_adjlist()):
        a=sum(1<<j for j in ns);ind += [s|1<<i for s in ind if not s&a]
    f=[s for s in ind if s.bit_count()==5];opts=[p for p in ind if all(p&s for s in f)]
    if not 1<=len(opts)<=6:return
    four=[s for s in ind if s.bit_count()==4];m=[sum(1<<j for j,s in enumerate(four) if not p&s) for p in opts];t=[[int(not(p&q))+2*int(not(m[i]&m[j])) for j,q in enumerate(opts)] for i,p in enumerate(opts)]
    groups={}
    for i,row in enumerate(t):groups.setdefault((row[i],tuple(sorted(row))),[]).append(i)
    return min(tuple(t[i][j] for i in o for j in o) for blocks in product(*(permutations(groups[k]) for k in sorted(groups))) for o in [sum(blocks,())])

def main():
    hosts=[unpack(s) for s in data(17).splitlines()];targets={}
    for i,h in enumerate(hosts):
        for rm in combinations(range(17),3):
            g=h.copy();g.delete_vertices(rm);k=table(g)
            if k:targets.setdefault(k,(i+1,rm))
    print('eligible table types retained',len(targets),flush=True)
    records=data(14).splitlines();Random(36).shuffle(records)
    for j,s in enumerate(records):
        g=unpack(s);k=table(g)
        if k in targets and not any(h.subisomorphic_lad(g,induced=True) for h in hosts):
            print('counterexample',s,targets[k],k,'tested',j+1,flush=True);return
    print('no collision in tested table sizes')
if __name__=='__main__': main()
