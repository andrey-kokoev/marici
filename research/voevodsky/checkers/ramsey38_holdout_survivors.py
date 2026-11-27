"""Classify every saved-count survivor; check shelling even for topological negatives."""
from ramsey38_cached_holdout import H,R,prev,inputs,json,cached
from ramsey38_twist10_edge_certificate import failures
from ramsey38_novel_root8_diagonal import link_profile,sub
from ramsey38_support_ball_completion import shelling
from ramsey38_compare_support_fillings import boundary
from collections import Counter

def run():
    data=json.loads(H.read_text());old=json.loads(R.read_text());assert old['sample_sha']==prev.sha(H.read_bytes());it=iter(old['cases']);tot=Counter();by=Counter();out=[]
    for e in data['cases']:
        b,_,x,rs,v=inputs(e);S=rs[x];rs[x]|=v;labs=sorted(b[e['u']]);dec=lambda m:frozenset(w for i,w in enumerate(labs) if m>>i&1)
        for d in e['sample']:
            ref=next(it);assert all(ref[k]==d[k] for k in d) and ref['record']==e['record'];bd=set(map(dec,d['bd']));req=set(map(dec,rs.values()))|{dec(S)|{d['tip']}};leaves=cached(labs,bd,req)['leaves'];assert len(leaves)==ref['survivors'];results=[]
            for leaf in leaves:
                ts=set(map(frozenset,leaf));assert boundary(ts)==bd and all(any(r<=t for t in ts) for r in req);bad=failures(ts,bd);profiles={};order=shelling(ts)
                if not bad:
                    for w in labs:
                        fs={t-{w} for t in ts if w in t};chi=len(set.union(set(),*fs))-len(set.union(*(sub(t,2) for t in fs)))+len(fs);n,ori=link_profile(fs);assert any(w in f for f in bd)
                        if (n,ori,chi)!=(1,True,1):profiles[w]=(n,ori,chi)
                kind='edge' if bad else 'link' if profiles else 'ball' if order else 'no-shelling';assert not order or kind=='ball';tot[kind]+=1;results.append(dict(kind=kind,cells=leaf,edges=[dict(edge=k,**v) for k,v in bad.items()],non_disk=profiles,shelling=[sorted(t) for t in order]))
            by['has_ball' if any(r['kind']=='ball' for r in results) else 'nonempty_no_ball' if results else 'empty']+=1;out.append(dict(record=e['record'],root=e['u'],**d,results=results))
    assert next(it,None) is None and sum(tot.values())==old['survivors'];print(tot,by)
    for i in sorted({d['record'] for d in out}):print(i,Counter(r['kind'] for d in out if d['record']==i for r in d['results']))
    print('bad links',Counter(tuple(tuple(x) for x in sorted(r['non_disk'].values())) for d in out for r in d['results'] if r['kind']=='link'));prev.save(prev.out/'ramsey38_holdout_survivors.json',dict(sample_sha=old['sample_sha'],totals=dict(tot),cases_by_result=dict(by),cases=out))
if __name__=='__main__':run()
