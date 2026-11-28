"""Adaptive permanent two-row readout; final repairs must extend installed link colors."""
from itertools import combinations
from collections import defaultdict
import json
from ramsey_two_repairs_opposite import run
from ramsey_pentagon_selector import charts,path
from ramsey_quartet_live_probe import independent_sets
from ramsey_inherited_swap_selector import evaluate,D


def audit():
    ref=defaultdict(dict)
    for sq,c,g in run():
        opts=[p for p in combinations(g,2) if set(p[0]).isdisjoint(p[1]) and all(set(r)&set(p[0]+p[1]) for r in sq)];m,=[(p,q) for p,q in combinations(opts,2) if set(p).isdisjoint(q)];ref[sq,c][g]=m
    selected={tuple(map(tuple,r['square'])) for r in json.loads((D/'ramsey_square_first_move.json').read_text())['records'] if not r['promise'] and r['outcome']=='no first-row plan'};records=[]
    for sq,_,cs in charts():
        if sq not in selected:continue
        gs=[ref[sq,tuple(sorted(c))] for c in cs];rows=sorted(set(s for group in gs for g in group for s in g));ok=[{r for r, in evaluate(10,sq,c,[(r,) for r in rows])} for c in cs];ids=tuple(range(len(cs)))
        def leaf(ii,installed,red):
            if not any(gs[i] for i in ii):return None if installed else {'none':True}
            for g in sorted(set.intersection(*(set(gs[i]) for i in ii))):
                if set(installed)<=set(g) and (len(installed)<2 or ((tuple(sorted(installed)) in gs[ii[0]][g])==red)):
                    return dict(quartet=g,repairs=gs[ii[0]][g])
        def solve(ii,installed,left,reject_only=False):
            stop=leaf(ii,installed,False)
            if stop:return stop
            if not left:return None
            for r in rows:
                if r in installed:continue
                for red in ([False,True] if installed else [False]):
                    yes=[]
                    for i in ii:
                        if r not in ok[i]:continue
                        if installed:
                            s,=installed;G=path|cs[i]|{(k,11+j) for j,t in enumerate(sq+(s,r)) for k in t}|{(11+j,15+d) for j,t in enumerate(sq) for d,p in enumerate((s,r)) if set(t).isdisjoint(p)}
                            if red:
                                if set(s)&set(r) or any(set(t).isdisjoint(s+r) for t in sq):continue
                                G.add((15,16))
                            if independent_sets(16,G,7):continue
                        yes.append(i)
                    no=[i for i in ii if i not in yes]
                    if not yes or not no:continue
                    y=leaf(yes,installed+(r,),red) or (solve(yes,(r,),left-1) if not installed and not reject_only else None);n=solve(no,installed,left-1,reject_only)
                    if y and n:return dict(probe=r,link_to_first=('red' if red else 'blue') if installed else None,yes=y,no=n)
        simple=solve(ids,(),2,True);policy=simple or solve(ids,(),2);assert policy;records.append(dict(square=sq,reject_only=bool(simple),policy=policy))
    print([bool(r['policy']) for r in records]);print(records[0]);(D/'ramsey_square_two_moves.json').write_text(json.dumps(records,indent=2)+'\n')
if __name__=='__main__':audit()
