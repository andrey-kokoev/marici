"""Infer cyclic coordinate charts from address incidence alone. No exterior links, preselected steps, output graphs or cube truth tables as input. Canonicalize the cyclic coordinate freedom by all units mod 35."""
from itertools import combinations,permutations
from collections import Counter,defaultdict
from math import gcd
from pathlib import Path
import json
D=Path(__file__).parent
# External addresses in lexicographic order of their original IDs; entries contain only label signatures. The array indices themselves are opaque IDs.
S=(1,16,68,40,130,51,72,132,85,32,2,136,105,150,17,64,4,170,33,18,204,65,20,34,8,128)
probes=[(0,2),(0,3),(0,19)] # original ID pairs (2,4),(2,5),(2,26)

def run():
    units=[u for u in range(35) if gcd(35,u)==1];canonical=lambda steps:min(tuple(sorted(min(u*x%35,-u*x%35) for x in steps)) for u in units);possible=Counter();charts=[];ds=[]
    for steps in combinations(range(1,18),4):
        if canonical(steps)!=steps:continue
        possible['step_orbits']+=1;L=sorted(set(steps)|{35-i for i in steps});Lset=set(L);ext=set(range(1,35))-Lset
        # Root neighborhood must be independent, equivalently the whole Cayley graph triangle-free.
        if any((b-a)%35 in Lset for a,b in combinations(L,2)):continue
        possible['triangle_free']+=1;raw={x:sum(1<<i for i,y in enumerate(L) if (x-y)%35 in Lset) for x in ext};inv={s:x for x,s in raw.items()}
        if len(inv)!=26 or sorted(t.bit_count() for t in inv)!=sorted(s.bit_count() for s in S):continue
        possible['size_profile']+=1
        for p in permutations(range(8)):
            table=[0]*256
            # test pairs first, fail fast
            def mapmask(m):return sum(1<<p[i] for i in range(8) if m>>i&1)
            if any(mapmask(s) not in inv for s in S if s.bit_count()==2):continue
            U=list(map(mapmask,S))
            if any(t not in inv for t in U):continue
            coords=tuple(inv[t] for t in U);possible['fits']+=1
            if any(tuple(u*x%35 for x in coords)<coords for u in units if {u*x%35 for x in L}==Lset):continue
            code=sum(int((coords[i]-coords[j])%35 in Lset)<<k for k,(i,j) in enumerate(probes));charts.append((code,coords,steps));ds.append(steps)
    charts.sort();assert [c for c,_,_ in charts]==list(range(8));E=[e for e in combinations(range(26),2) if not S[e[0]]&S[e[1]]];features=Counter();truth=[]
    for i,j in E:
        corners=[c for c,X,steps in charts if min((X[i]-X[j])%35,(X[j]-X[i])%35) in steps];truth.append(corners);key=(len(corners),tuple(sorted((a^b).bit_count() for a,b in combinations(corners,2))));features[key]+=1
    from verify_ramsey_catalogue_free_chain import verify
    for c,X,steps in charts:
        H=[sum(1<<((x+d)%35) for i in steps for d in (i,-i)) for x in range(35)];verify(H,9)
    out=dict(counts=dict(possible),step_sets=sorted(set(ds)),charts=charts,feature_counts={str(k):n for k,n in features.items()},probe_edges=probes);print(out['counts'],out['step_sets'],out['feature_counts']);return out
if __name__=='__main__':(D/'ramsey_address_to_cube.json').write_text(json.dumps(run())+'\n')
