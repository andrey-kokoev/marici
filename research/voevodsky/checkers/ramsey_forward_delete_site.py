"""Freeze the automorphism classes of record 262402 before scoring any deletion. Verify an explicit forward route for each successful site/pair."""
from ramsey_forward_link_filter import score,CAT,D,decode,G,induced,islice,combinations,gzip,json

def autom(a):
    n=len(a);signature=lambda m:tuple(sorted(a[j].bit_count() for j in range(n) if m>>j&1));sig=list(map(signature,a));ds=[sum(1<<j for j in range(n) if s==sig[j]) for s in sig];out=[];f=[-1]*n
    def visit(left,ds):
        if not left:out.append(tuple(f));return
        i=min(left,key=lambda i:ds[i].bit_count());rem=left-{i};opts=ds[i]
        while opts:
            bit=opts&-opts;opts-=bit;j=bit.bit_length()-1;d=ds[:]
            for h in rem:
                d[h]&=(a[j] if a[i]>>h&1 else ~a[j])&~bit
                if not d[h]:break
            else:f[i]=j;visit(rem,d)
    visit(set(range(n)),ds);assert all(len(set(f))==n and all((a[i]>>j&1)==(a[f[i]]>>f[j]&1) for i,j in combinations(range(n),2)) for f in out);return out

def audit():
    idx=262402
    with gzip.open(CAT/'r38_27.g6.gz','rt') as f:a=decode(next(islice(f,idx,None)).strip())
    group=autom(a);orbits=sorted({tuple(sorted({f[i] for f in group})) for i in range(27)});assert sum(map(len,orbits))==27;old_edges=sum(map(int.bit_count,a))//2;V=json.loads((D.parent/'ramsey_cube_unlock_free_row.json').read_text())['core_labels'];target=induced(G,V);cases=[];ok=[]
    independent=[0]
    for i,v in enumerate(a):independent.extend([s|1<<i for s in independent if not s&v]);
    for z in range(27):
        if old_edges-a[z].bit_count()+2-9!=76:continue
        es=[(1<<i)|(1<<j) for i,j in combinations(range(27),2) if not a[i]>>j&1 and a[i]&a[j]==1<<z];qs=[s for s in independent if not s>>z&1 and s.bit_count()==7];coverage=[sum(q&e==e or q&h==h for q in qs) for e,h in combinations(es,2) if not e&h];fs={};pairs,ct,nodes=score(a,z,fs);ex=[]
        for pair,f in fs.items():
            g=induced(a,f);rm=[];add=[]
            for i,j in combinations(range(26),2):
                if (g[i]^target[i])>>j&1:(rm if g[i]>>j&1 else add).append(tuple(sorted((f[i],f[j]))))
            assert len(rm)==9 and tuple(sorted(add))==pair and set(f)==set(range(27))-{z};b=a[:]
            for u,v in rm+add:b[u]^=1<<v;b[v]^=1<<u
            assert induced(b,f)==target;ex.append(dict(added=pair,removed=rm,retained=f))
        if pairs:ok.append(z)
        cases.append(dict(z=z,eligible_pairs=len(coverage),best_coverage=max(coverage,default=None),routes=ex,embeddings=ct['embeddings']))
    orbit0=next(o for o in orbits if 0 in o);assert all(set(o)<=set(ok) or not set(o)&set(ok) for o in orbits);out=dict(record=idx,old_edges=old_edges,group_order=len(group),site_orbits=orbits,eligible=len(cases),successful_sites=ok,only_orbit_0=set(ok)==set(orbit0),cases=cases);print({k:v for k,v in out.items() if k!='cases'});(D.parent/'ramsey_forward_delete_site.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
