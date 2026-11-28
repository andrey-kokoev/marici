"""Test a conditional construction: close the old path, then subdivide one edge."""
from itertools import pairwise
from collections import Counter
import json
from ramsey_inherited_swap_selector import D, run


def splices(path):
    ring = {tuple(sorted(e)) for e in pairwise((*path, path[0]))}
    return {(a,b): (ring-{(a,b)}) | {(a,10),(b,10)} for a,b in sorted(ring)}


def audit():
    cases = json.loads((D/'ramsey_inherited_single_rows.json').read_text())['failed_cases']
    conflicts = {(tuple(map(tuple,c['square'])),tuple(c['old_path'])): c for c in cases if not c['common']}
    hist = Counter(); witnesses = []
    def inspect(sq,path,marks,children):
        tied = [c for c,v in children if marks<=v]
        if len(tied)<2:return
        keep = [(e,c) for e,c in splices(path).items() if c in tied]
        hist[len(keep)] += 1
        if (sq,path) not in conflicts:return
        case = conflicts[sq,path]; losses = {frozenset(map(tuple,d['edges'])):d['lost_rows'] for d in case['candidates']}
        witnesses.append(dict(square=sq,old_path=path,options=[dict(cut=e,lost=losses[frozenset(c)]) for e,c in keep]))
    run(inspect)
    assert sum(hist.values())==28 and len(witnesses)==2
    result=dict(tied_cases_by_splice_count=hist,witnesses=witnesses);print(result)
    (D/'ramsey_inherited_endpoint_splice.json').write_text(json.dumps(result,indent=2)+'\n')

if __name__=='__main__':audit()
