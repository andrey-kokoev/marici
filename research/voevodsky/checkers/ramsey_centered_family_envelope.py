"""Is a new family even possible under the centered two-link rule? Complete each feasible signature, *including* nonminimal additions; identify minimal predecessors and all descendants up to graph isomorphism."""
from ramsey_cube_retention_floor import G,induced,D,CAT,decode,iso,wl,deg,json,combinations,Counter
from ramsey_retention_slice import check
from collections import defaultdict
import gzip

def enumerate_all(a,r):
    cuts=set(map(tuple,r['cuts']));s=sum(1<<v for v in r['row']);b=a[:]
    for i,j in cuts:b[i]^=1<<j;b[j]^=1<<i
    I=[0]
    for j,v in enumerate(b):I.extend([t|1<<j for t in I if not t&v])
    qs=[q for q in I if q.bit_count()==8 or q.bit_count()==7 and not q&s];base=b[:]+[s]
    for j in range(26):base[j]|=(s>>j&1)<<26
    es=[(i,j) for i,j in combinations(range(26),2) if (i,j) not in cuts and not base[i]&((1<<j)|base[j]) and max(base[i].bit_count(),base[j].bit_count())<7];dem=sorted({sum(1<<k for k,(i,j) in enumerate(es) if q>>i&q>>j&1) for q in qs},key=int.bit_count);ds=[]
    for d in dem:
        if not any(d&v==v for v in ds):ds.append(d)
    allmodels={}
    def rec(g,used,avail,remaining):
        if not remaining:
            assert check(g,(1<<27)-1,3,8);assert used not in allmodels;allmodels[used]=g
            opts=avail
        else:opts=min((d&avail for d in remaining),key=int.bit_count)
        while opts:
            bit=opts&-opts;opts-=bit;avail^=bit;k=bit.bit_length()-1;i,j=es[k];h=g[:];h[i]|=1<<j;h[j]|=1<<i
            nextmask=sum(1<<t for t,(u,v) in enumerate(es) if avail>>t&1 and max(h[u].bit_count(),h[v].bit_count())<7 and not h[u]&h[v]);rec(h,used|bit,nextmask,[d for d in remaining if not d&bit])
    rec(base,0,(1<<len(es))-1,ds);known=sum(1<<es.index(tuple(e)) for e in r['reverse_add']);assert known in allmodels
    return es,allmodels

def audit():
    V=json.loads((D.parent/'ramsey_cube_unlock_free_row.json').read_text())['core_labels'];a=induced(G,V);rows=json.loads((D.parent/'ramsey_cube_cut_location.json').read_text())['cases'];samples={};bykey=defaultdict(list);models=[];types=[]
    def typ(g):
        sig=wl(g)
        for t in bykey[sig]:
            if iso(g,samples[t]) is not None:return t
        t=len(samples);samples[t]=g;bykey[sig].append(t);types.append({});return t
    for r in rows:
        if r['locations']!=[2,2]:continue
        es,graphs=enumerate_all(a,r);minimal=[m for m in graphs if all(m^(1<<j) not in graphs for j in range(len(es)) if m>>j&1)];assert all(any(v&m==v for v in minimal) for m in graphs);records=[]
        for m,g in graphs.items():
            ancestors=[v for v in minimal if v&m==v];mid=[(g[i]&g[j]).bit_count()-1 for i,j in r['cuts']];records.append(dict(type=typ(g),adds=[es[j] for j in range(len(es)) if m>>j&1],min_ancestors=sorted({typ(graphs[v]) for v in ancestors}),excess=min((m^v).bit_count() for v in ancestors),extra_paths=sorted(mid)))
        models.append(dict(cuts=r['cuts'],row=r['row'],models=records));print('signature',len(graphs),len(minimal),flush=True)
    E={sum(map(int.bit_count,g))//2 for g in samples.values()};degs={deg(g) for g in samples.values()};w=bytes([(j-63).bit_count() if 63<=j<=126 else 0 for j in range(256)]);pending=set(samples)
    for idx,l in enumerate(gzip.open(CAT/'r38_27.g6.gz','rb')):
        b=l.strip();ec=sum(b[1:].translate(w));
        if ec not in E:continue
        g=decode(b.decode());
        if deg(g) not in degs:continue
        for t in bykey.get(wl(g),[]):
            if t in pending and iso(samples[t],g) is not None:types[t]=dict(record=idx,edges=ec);pending.remove(t)
        if not pending:break
    assert not pending;stats=Counter();mins=set();
    for r in models:
        for m in r['models']:
            stats[m['excess']]+=1
            if not m['excess']:mins.add(types[m['type']]['record'])
    print('types',len(types),'minima',mins,'excess',stats);out=dict(types=types,minimum_records=sorted(mins),excess_hist=stats,signatures=models);(D.parent/'ramsey_centered_family_envelope.json').write_text(json.dumps(out,indent=1)+'\n')
if __name__=='__main__':audit()
