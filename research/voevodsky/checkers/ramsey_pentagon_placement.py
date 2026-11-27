from itertools import combinations,product
from collections import Counter,defaultdict
from pathlib import Path
from hashlib import sha256
import json
from ramsey_table_cube_differences import analyze
from ramsey_pentagon_selector import charts,ind,coexists


def run():
    ix=defaultdict(list);flip=lambda s:tuple(11-i for i in reversed(s))
    for p in analyze(10)['pieces']:
        a=tuple(p['start']);C=list(product(*[(v,v+1) for v in a]));fresh={tuple(v) for v in p['new']}
        for s,t in combinations(C,2):
            if sum(abs(i-j) for i,j in zip(s,t))!=1:continue
            for half,f in [('upper',lambda s:s),('mirror',flip)]:
                ix[tuple(sorted((f(s),f(t))))].append((half,a,tuple(sorted(f(z) for z in (s,t) if z in fresh))))
    scores=Counter();coverage=Counter();seen=defaultdict(dict);example=None
    for sq,qs,cycles in charts():
        U=set().union(*sq);mov=U-set.intersection(*map(set,sq));probes={tuple(sorted((*e,z))):e for e in qs for z in mov if ind({*e,z})}
        for s,t in combinations(sorted(probes),2):
            if sum(abs(i-j) for i,j in zip(s,t))!=1:continue
            occ=ix[s,t]
            for cycle in cycles:
                if {probes[s],probes[t]}&cycle:continue
                coverage[bool(occ)]+=1
                if not occ:continue
                verdict=coexists(sq,(s,t),cycle)
                for half,a,fresh in occ:
                    scores[len(fresh),verdict]+=1;key=(s,t,half,a,fresh);models=seen[key];models.setdefault(verdict,dict(square=sq,cycle=sorted(cycle)))
                    if example is None and len(fresh)==2 and len(models)==2:example=dict(rows=(s,t),half=half,placement_start=a,models=dict(models))
    out=dict(scope='individual-pass trials; scores count marked placement occurrences, coverage counts each square/row-pair/cycle once',coverage={str(k):v for k,v in coverage.items()},fresh_and_joint={str(k):v for k,v in scores.items()},marked_edges_tested=len(seen),marked_edges_with_both_verdicts=sum(len(v)==2 for v in seen.values()),example=example,protocol_sha=sha256((D/'ramsey_pentagon_placement_protocol.md').read_bytes()).hexdigest());print(out);(D/'ramsey_pentagon_placement.json').write_text(json.dumps(out,indent=2)+'\n')
D=Path(__file__).resolve().parents[1]/'results'
if __name__=='__main__':run()
