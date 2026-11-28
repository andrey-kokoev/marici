"""Catalogue-labeled certificate for the first two-crossing example that requires an inside-leg cut."""
from ramsey_centered_family_envelope import G,induced,D,CAT,decode,iso,json,combinations,gzip
from itertools import islice
from ramsey_retention_slice import check

def audit():
    cases=json.loads((D.parent/'ramsey_double_cross_paths.json').read_text())['cases'];r=next(c for c in cases if len(c['paths'])==3);idx=r['record'];v0=json.loads((D.parent/'ramsey_cube_unlock_free_row.json').read_text())['core_labels'];a=induced(G,v0)+[sum(1<<i for i in r['row'])]
    for i,j in r['pair']+r['removed']:a[i]^=1<<j;a[j]^=1<<i
    for i in r['row']:a[i]|=1<<26
    with gzip.open(CAT/'r38_27.g6.gz','rt') as file:b=decode(next(islice(file,idx,None)).strip())
    p=iso(a,b);assert p is not None;z=p[-1];V=((1<<27)-1)^(1<<z);h=[v&V for v in b];h[z]=0;adds=[(p[i],p[j]) for i,j in r['pair']];
    for i,j in adds:h[i]|=1<<j;h[j]|=1<<i
    veto=set(map(tuple,r['single_veto']));path=[]
    for i,m,u in r['paths']:
        bad,good=sorted([tuple(sorted((i,m))),tuple(sorted((m,u)))],key=lambda e:e not in veto);assert bad in veto and good not in veto;l,k=map(p.__getitem__,bad);qs=(v for v in range(27) if v not in (z,l,k) and not(h[l]|h[k])>>v&1);six=next(c for c in combinations(qs,6) if all(not h[i]>>j&1 for i,j in combinations(c,2)));path.append(dict(inside=p[i],middle=p[m],outside=p[u],required_cut=[p[j] for j in good],protected_edge=[l,k],six=six))
    for i,j in r['removed']:u,v=p[i],p[j];h[u]^=1<<v;h[v]^=1<<u
    assert check(h,V,3,8) and induced(h,p[:-1])==induced(G,v0);out=dict(record=idx,deleted=z,add=adds,paths=path);print(out);(D.parent/'ramsey_cross_inside_exception.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
