"""Can the square and the full list of inherited legal swap pairs identify the old ring?"""
from collections import defaultdict,Counter
from itertools import combinations,pairwise
import json
from ramsey_inherited_endpoint_splice import splices
from ramsey_inherited_swap_selector import run,D,evaluate


def ring(path):
    return frozenset(tuple(sorted(e)) for e in pairwise((*path,path[0])))


def main():
    groups=defaultdict(list)
    def collect(sq,path,marks,children):
        viable=[c for c,v in children if marks<=v]
        if len(viable)<2:return
        choices={frozenset(c) for c in splices(path).values() if c in viable}
        groups[sq,frozenset(marks)].append((path,choices))
    run(collect)
    counts=Counter(); examples=[]
    for (sq,marks),cases in groups.items():
        counts['observation_groups']+=1
        if len({ring(p) for p,_ in cases})<2:continue
        counts['ambiguous_ring_groups']+=1
        for (p,a),(q,b) in combinations(cases,2):
            if not a or not b or a&b:continue
            counts['incompatible_pairs']+=1
            queries=[(s,) for s in combinations(range(1,10),3) if s not in sq and min(s[1]-s[0],s[2]-s[1])>=2]
            profiles=[evaluate(9,sq,{tuple(sorted(e)) for e in pairwise(t)},queries) for t in (p,q)]
            difference=sorted(s for (s,) in profiles[0]^profiles[1]);counts['separated_by_single_row']+=bool(difference)
            examples.append(dict(square=sq,marks=sorted(marks),paths=[p,q],single_row_only_on_each=[sorted(s for (s,) in profile-profiles[1-i]) for i,profile in enumerate(profiles)],choices=[[sorted(c) for c in sorted(opts,key=sorted)] for opts in (a,b)]))
    assert sum(map(len,groups.values()))==28
    examples.sort(key=lambda e:-len(e['marks']))
    result=dict(counts=counts,examples=examples);print(counts);print(examples[:1]);(D/'ramsey_inherited_order_visibility.json').write_text(json.dumps(result,indent=2)+'\n')
if __name__=='__main__':main()
