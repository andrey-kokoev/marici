"""Read each exit division as its partner involution on the four corners; compare their actual products with the action that permutes divisions."""
from itertools import permutations
from ramsey_folded_entry_handoff import T,P,X,D,json

def run():
    maps={}
    for d in T[14]:
        f={}
        for k in d:
            a,b=X[k];f[a]=b;f[b]=a
        maps[P.index(d)]=tuple(f[i] for i in range(1,5))
    comp=lambda p,q:tuple(p[i-1] for i in q);labels={f:d for d,f in maps.items()};products={};actions={}
    for a,b in permutations(maps,2):
        c=labels[comp(maps[a],maps[b])];assert c not in (a,b) and comp(maps[b],maps[a])==maps[c];products[f'{a},{b}']=c
    for p in permutations(range(1,5)):
        inv=tuple(p.index(i)+1 for i in range(1,5));im=tuple(labels[comp(p,comp(f,inv))] for f in maps.values());actions.setdefault(im,[]).append(p)
    kernel=actions[tuple(maps)];assert len(actions)==6 and all(len(v)==4 and sum(p[0]==1 for p in v)==1 for v in actions.values());return dict(maps=maps,products=products,kernel=kernel,orders=list(maps),actions=[dict(images=k,lifts=v) for k,v in actions.items()])
if __name__=='__main__':
    out=run();print(out['maps'],out['products'],out['kernel']);(D/'ramsey_division_triality.json').write_text(json.dumps(out)+'\n')
