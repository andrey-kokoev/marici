"""Exact anonymous continuation types. Two states are equal iff they have the same multiset of successor types (including move multiplicities); named moves are not equated. Compare with counts of paths at each length. Count commutation squares from initial states separately per ring."""
from collections import Counter,defaultdict
from pathlib import Path
import json
D=Path(__file__).resolve().parents[1]/'results';data=json.loads((D/'ramsey_38_correction_continuation.json').read_text());codes={};profiles=[];out=[];allstates=set();control=None
for o in data:
    Z=o['Z'];W=o['W'];pairs=[(1<<Z.index(f['move'][0]),1<<W.index(f['move'][1])) for f in o['first']];states={};pmap=defaultdict(set);examples={}
    def solve(a,b):
        if (a,b) in states:return states[a,b]
        hist=Counter(solve(a^z,b^w) for z,w in pairs if a&z and b&w);sig=tuple(sorted(hist.items()))
        if sig not in codes:
            codes[sig]=len(codes);p=[1]+[0]*max((len(profiles[t]) for t in hist),default=0)
            for t,n in hist.items():
                for j,v in enumerate(profiles[t]):p[j+1]+=n*v
            profiles.append(tuple(p))
        t=codes[sig];states[a,b]=t;profile=profiles[t];pmap[profile].add(t);examples[profile,t]=(a,b);return t
    root=solve((1<<len(Z))-1,(1<<len(W))-1);assert profiles[root][2]%2==0;collisions=[(p,ts) for p,ts in pmap.items() if len(ts)>1];
    if collisions and control is None:
        p,ts=min(collisions,key=lambda pt:len(pt[0]));control=dict(record=len(out),path_counts=p,states=[examples[p,t] for t in sorted(ts)[:2]])
    allstates.update(states.values());out.append(dict(poles=o['poles'],ring=o['ring'],reachable=len(states),anonymous_types=len(set(states.values())),length_profiles=len(pmap),distinct_types_with_same_length_counts=bool(collisions),commuting_first_pairs=profiles[root][2]//2,root_type=root))
result=dict(scope='anonymous move multiplicity and recursive choices, no reuse on either side',rings=out,common_type_count=len(allstates),example_profile_collision=control);(D/'ramsey_38_correction_quotient.json').write_text(json.dumps(result,indent=2)+'\n');print(out[0],len(allstates),sum(x['distinct_types_with_same_length_counts'] for x in out),control);print({k:(min(x[k] for x in out),max(x[k] for x in out)) for k in ['reachable','anonymous_types','commuting_first_pairs']})
