"""Retrospective: why did 26 early-sign survivors lack a seven-label filling?"""
from itertools import combinations
from collections import Counter
from ramsey38_early_sign_trial import P,R,inputs,json,prev
from ramsey38_root15_link_rotation import link_domains,canon
from ramsey38_polygon_endpoint_rule import compatible

def domains(bd,req):
    fs=req|{t|{0} for t in bd};V=set.union(set(),*fs)
    return {v:link_domains(frozenset(f-{v} for f in fs if v in f)) for v in V}

def solve(d):
    if not d:return True
    v=min(d,key=lambda w:len(d[w]))
    for r in d[v]:
        nxt={w:[s for s in opts if w not in r or s[v]==canon(r[w][::-1])] for w,opts in d.items() if w!=v}
        if all(nxt.values()) and solve(nxt):return True
    return False

def smallest(d):
    for n in range(1,len(d)+1):
        for q in combinations(sorted(d),n):
            if not solve({v:d[v] for v in q}):return q

def run():
    pred=json.loads(P.read_text());comparison=json.loads(R.read_text());assert comparison['prediction_sha']==prev.sha(P.read_bytes());stats=Counter();exceptions=[]
    for e,cert in zip(pred['cases'],comparison['certificates']):
        fills={(t['row'],tuple(t['bd']),t['tip']) for t in cert};b,_,x,rs,v=inputs(e);labs=sorted(b[e['u']]);S=rs[x];rs[x]|=v;decode=lambda m:frozenset(a for j,a in enumerate(labs) if m>>j&1)
        for case in e['predictions']:
            for sw,c in case['tips'].items():
                if c!='pass':continue
                w=int(sw);bd=frozenset(map(decode,case['bd']));req=set(map(decode,rs.values()))|{decode(S)|{w}};actual=(case['row'],tuple(case['bd']),w) in fills
                passed=compatible(bd,req);assert passed or not actual
                core=None
                if not passed:
                    ds=domains(bd,req);core=smallest(ds);assert core
                kind='pass' if passed else 'conflict-'+str(len(core));stats[kind,actual]+=1
                if not actual:
                    z=dict(record=e['record'],root=e['u'],row=case['row'],bd=case['bd'],tip=w,core=core)
                    if core and len(core)==2:
                        v0,v1=core;z['orders']=sorted({r[v1] for r in ds[v0]});z['reversed_orders']=sorted({canon(r[v0][::-1]) for r in ds[v1]});assert not set(z['orders'])&set(z['reversed_orders'])
                    if passed:
                        from ramsey38_signed_swap_transport import replay
                        from ramsey38_novel_root8_diagonal import link_profile,sub
                        all_ts=list(replay(dict(enumerate(req)),bd));assert len(all_ts)==1
                        ts=all_ts[0];z['non_disk_links']=[]
                        for vertex in labs:
                            triangles={t-{vertex} for t in ts if vertex in t};edges=set.union(*(sub(t,2) for t in triangles));chi=len(set.union(set(),*triangles))-len(edges)+len(triangles)
                            if chi!=1:
                                assert chi==0 and link_profile(triangles)==(1,False) and any(vertex in f for f in bd);z['non_disk_links'].append(vertex)
                        assert len(z['non_disk_links'])==2
                    exceptions.append(z)
    print(stats);print('survivors:',[z for z in exceptions if not z['core']]);print('conflict example',next((z for z in exceptions if z['core']),None))
    prev.save(prev.out/'ramsey38_early_sign_join_and_links.json',dict(frozen_sha=comparison['prediction_sha'],counts={f'{k}/{b}':v for (k,b),v in stats.items()},unfilled=exceptions))
if __name__=='__main__':run()
