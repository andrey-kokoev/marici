"""Quantify exact continuation equivalence AFTER fixing w's support; vary all legal labeled supports of z. v-w,v-z,w-z blue. Cross-check against previous exhaustive counts."""
from itertools import combinations,product
from collections import Counter
from pathlib import Path
import json
D=Path(__file__).resolve().parents[1]/'results'
def run(old):
 E=old['edges'];I=[s for s in range(256) if all(s&(1<<(a-1)|1<<(b-1))!=(1<<(a-1)|1<<(b-1)) for a,b in E)];corners=[sum(1<<(i-1) for i in t) for t in product((1,2),(4,5),(7,8))];family=[0,1,3,7];rows=[];totals=[0]*8
 for T in I:
    # Build a hitting-set request from each blue clique among the exterior vertices. Requests containing smaller requests are redundant.
    bases=[{x for x in I if x.bit_count()==4 and not x&S} for S in corners]
    profiles=[];sigs=[]
    for i,S in enumerate(corners):
        # Without z the v,w pair already has four-core obstruction. With z present, v,z and w,z require fours, v,w,z requires triples.
        impossible=any(not x&T for x in bases[i]);req=bases[i]|{x for x in I if x.bit_count()==4 and not x&T}|{x for x in I if x.bit_count()==3 and not x&(S|T)}
        minimal=() if impossible else tuple(sorted(x for x in req if not any(y!=x and y&x==y for y in req)))
        profiles.append(None if impossible else minimal);sig=frozenset() if impossible else frozenset(U for U in I if all(U&x for x in minimal));sigs.append(sig);totals[i]+=len(sig)
    rel=lambda L:tuple(next(j for j,v in enumerate(L) if v==x) for x in L)
    a=[sigs[i] for i in family];b=[profiles[i] for i in family];rows.append(dict(T=T,partition=rel(a),sets=len(set(a)),live=sum(bool(s) for s in a),common=len(set.intersection(*(set(s) for s in a))),all_live_equal=len(set(a))==1 and bool(a[0]),minimal_requests_exact=rel(b)==rel(a),all8_profiles_exact=rel(profiles)==rel(sigs),requests=[profiles[i] for i in family],counts=list(map(len,a))))
 return dict(distribution=dict(Counter(r['sets'] for r in rows)),live_equal=sum(r['all_live_equal'] for r in rows),profile_matches=sum(r['minimal_requests_exact'] for r in rows),all8_matches=sum(r['all8_profiles_exact'] for r in rows),totals=totals,rows=rows)
if __name__=='__main__':
 old=json.loads((D/'ramsey_cube_exterior_test.json').read_text());ref=json.loads((D/'ramsey_cube_two_exterior.json').read_text());out={}
 for name,v in old.items():
    r=out[name]=run(v);prior=ref['chord' if name=='path_plus_36' else name][0]['groups'];assert r['totals']==[g['count'] for g in prior];print(name,{k:v for k,v in r.items() if k!='rows'});print('example',next(((x['T'],x['requests'][0],x['counts']) for x in r['rows'] if x['all_live_equal']),None))
 (D/'ramsey_cube_conditional_folds.json').write_text(json.dumps(out))
