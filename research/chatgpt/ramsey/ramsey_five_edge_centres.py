"""Test path reversal, middle flags and endpoint phase in the two uniform five-edge representatives. Number the active decagon starting at a partition and taking the FIRST row out, second back."""
from itertools import permutations
from ramsey_ten_cycle_shift_census import enum,flags,D,json

def test():
    ms=list(enum());out=[]
    for r in json.loads((D/'ramsey_ten_cycle_shift_census.json').read_text()):
        if r['lengths']!=[5]*5:continue
        s,t=[ms[i] for i in r['representative']];a={j:i for i,j in s};b=dict(t);j=min(y for _,y in s^t);w=[]
        for _ in range(5):w.extend([j,a[j]]);j=b[a[j]]
        adj={x:set() for x in range(30)}
        for x,y in flags-(s|t):adj[x].add(y);adj[y].add(x)
        paths=[];phase=[];f={}
        for j in w[::2]:
            p=[j];prev=None
            while adj[p[-1]]-{prev}:prev,z=p[-1],next(iter(adj[p[-1]]-{prev}));p.append(z)
            assert len(p)==6;paths.append(p);phase.append((w.index(p[-1])-w.index(j))%10);f.update(zip(p,p[::-1]))
        duals=[]
        for perm in permutations(range(5)):
            g={x:y for k,p in enumerate(paths) for x,y in zip(p,paths[perm[k]][::-1])};im=lambda u:{tuple(sorted((g[x],g[y]))) for x,y in u}
            if im(flags)==flags:duals.append(dict(path_map=perm,involution=all(g[g[x]]==x for x in g),exchanges=im(s)==t,preserves=im(s)==s))
        image=lambda u:{tuple(sorted((f[x],f[y]))) for x,y in u};out.append(dict(rep=r['representative'],endpoint_offsets=phase,duals=duals,paths=paths,flags_preserved=len(flags&image(flags)),common_preserved=len((s&t)&image(s&t)),row_exchanged=image(s)==t,row_preserved=image(s)==s))
    return out
if __name__=='__main__':
    out=test();print(out);(D/'ramsey_five_edge_centres.json').write_text(json.dumps(out)+'\n')
