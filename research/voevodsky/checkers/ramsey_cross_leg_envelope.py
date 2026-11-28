"""Exhaust the crossed-link family (not merely one witness per successful cut/row signature). Test wrong-leg blue-eight veto on each predecessor before consulting the target removal list."""
from ramsey_centered_family_envelope import enumerate_all,G,induced,D,CAT,decode,iso,wl,deg,json,combinations,Counter,defaultdict,gzip
from ramsey_retention_slice import has,check
from itertools import product

def audit():
    V=json.loads((D.parent/'ramsey_cube_unlock_free_row.json').read_text())['core_labels'];a=induced(G,V);rows=json.loads((D.parent/'ramsey_cube_cut_location.json').read_text())['cases'];recs=[];samples={};keys=defaultdict(list);hist=Counter();F=(1<<26)-1
    def typ(g):
        key=wl(g)
        for t in keys[key]:
            if iso(g,samples[t]) is not None:return t
        t=len(samples);samples[t]=g;keys[key].append(t);return t
    for r in rows:
        if r['locations']!=[1,2]:continue
        s=set(r['row']);cuts=list(map(tuple,r['cuts']));e,=[e for e in cuts if set(e)<=s];f,=[f for f in cuts if len(set(f)&s)==1];u,=set(f)-s;i,=set(f)&s;es,models=enumerate_all(a,r);minimal=[m for m in models if all(m^(1<<k) not in models for k in range(len(es)) if m>>k&1)]
        for m,g in models.items():
            removed={es[j] for j in range(len(es)) if m>>j&1};center=g[e[0]]&g[e[1]]&F;cross=g[i]&g[u]&F;middle=[j for j in range(26) if cross>>j&1];post=g[:26];post=[v&F for v in post];
            for v,w in cuts:post[v]|=1<<w;post[w]|=1<<v
            tests=[]
            for j in middle:
                legs=[]
                for endpoint in (u,i):
                    h=post[:];h[j]^=1<<endpoint;h[endpoint]^=1<<j
                    # Any surviving blue eight after these two additions and one removal kills that removal for good.
                    veto=has([~v for v in h],F,8);leg=tuple(sorted((j,endpoint)));taken=leg in removed;assert not(taken and veto);legs.append((taken,veto))
                assert any(t for t,v in legs);tests.append(dict(middle=j,outside_removed=legs[0][0],inside_removed=legs[1][0],outside_veto=legs[0][1],inside_veto=legs[1][1]));hist[legs[0],legs[1]]+=1
            h=post[:];
            for v,w in removed:h[v]^=1<<w;h[w]^=1<<v
            assert h==a;recs.append(dict(type=typ(g),cuts=cuts,row=r['row'],outside=u,old_degree=g[u].bit_count(),target_degree=a[u].bit_count(),center_extra=center.bit_count(),cross_paths=tests,optional_removals=len(removed)-min(v.bit_count() for v in minimal if v&m==v),removals=sorted(removed)))
    es={sum(map(int.bit_count,g))//2 for g in samples.values()};ds={deg(g) for g in samples.values()};w=bytes([(i-63).bit_count() if 63<=i<=126 else 0 for i in range(256)]);pending=set(samples);records={}
    for idx,l in enumerate(gzip.open(CAT/'r38_27.g6.gz','rb')):
        b=l.strip();
        if sum(b[1:].translate(w)) not in es:continue
        g=decode(b.decode());
        if deg(g) not in ds:continue
        for t in keys.get(wl(g),[]):
            if t in pending and iso(samples[t],g) is not None:records[t]=idx;pending.remove(t)
        if not pending:break
    assert not pending
    for r in recs:r['record']=records[r.pop('type')]
    envelopes=defaultdict(list)
    for r in recs:
        f,=[e for e in r['cuts'] if r['outside'] in e];i,=set(f)-{r['outside']};j=r['cross_paths'][0]['middle'];envelopes[tuple(r['row']),tuple(map(tuple,r['cuts'])),i,j].append(r)
    cert=[]
    for (row,cuts,i,j),rs in envelopes.items():
        h=a[:]
        for r in rs:
            for u,v in r['removals']:h[u]|=1<<v;h[v]|=1<<u
        free=[v for v in range(26) if v not in (i,j) and not(h[i]|h[j])>>v&1];qq=[c for c in combinations(free,6) if all(not h[u]>>v&1 for u,v in combinations(c,2))];assert qq;cert.append(dict(row=row,cuts=cuts,wrong_leg=[i,j],shared_six=qq[0],shared_six_count=len(qq),cases=len(rs)))
    assert len(cert)==12
    counts=Counter((r['center_extra'],len(r['cross_paths'])) for r in recs);print('realizations',len(recs),'types',len(records),'minima',{r['record'] for r in recs if not r['optional_removals']},'path multiplicity',counts,'leg counts',hist);(D.parent/'ramsey_cross_leg_envelope.json').write_text(json.dumps(dict(shared_certificates=cert,path_histogram={str(k):v for k,v in counts.items()},leg_histogram={str(k):v for k,v in hist.items()},cases=recs),indent=1)+'\n')
if __name__=='__main__':audit()
