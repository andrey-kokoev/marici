"""Can one red port link repair an all-blue square obstruction? Same eligible trials as previous test."""
from itertools import combinations
from collections import Counter
from pathlib import Path
import json


def run(k):
    sites=set(range(1,k+1));rows=[frozenset(t) for t in combinations(sorted(sites),3) if min(t[1]-t[0],t[2]-t[1])>=2];R=set(rows);squares=set()
    for p in rows:
        moves=[frozenset((i,i+1)) for i in range(1,k) if len(p&{i,i+1})==1 and (p^{i,i+1}) in R]
        for a,b in combinations(moves,2):
            if not a&b and p^a^b in R:squares.add(tuple(sorted((p,p^a,p^b,p^a^b),key=sorted)))
    def blue(q):
        avail=sorted(sites-set().union(*q));take=[]
        for v in avail:
            if not take or v>take[-1]+1:take.append(v)
        return len(take)+len(q)>=7
    def bad(ss):return [p for n in range(len(ss)+1) for p in combinations(range(len(ss)),n) if blue([ss[i] for i in p])]
    count=Counter();examples={}
    for square in sorted(squares,key=lambda s:list(map(sorted,s))):
        singles=[s for s in rows if s not in square and not bad((*square,s))]
        for s,t in combinations(singles,2):
            ss=(*square,s,t);clauses=list(map(set,bad(ss)));count['eligible']+=1
            if not clauses:continue
            assert clauses==[set(range(6))], 'a blue seven can omit a port'
            edges=[e for e in combinations(range(6),2) if not ss[e[0]]&ss[e[1]]];minimal=[]
            for n in range(len(edges)+1):
                for es in combinations(edges,n):
                    F=set(es)
                    if any(z<=F for z in minimal):continue
                    if all(any(set(e)<=p for e in F) for p in clauses):minimal.append(F)
            # All eligible port edges can simultaneously be red: 3 disjoint triples need 9 sites.
            assert k<9
            forced=set.intersection(*minimal) if minimal else set();one=[z for z in minimal if len(z)==1];label='impossible' if not minimal else 'one_forced' if one and forced else 'one_optional' if one else 'multiple_required';count[label]+=1
            if label not in examples:examples[label]=dict(rows=list(map(sorted,ss)),uncovered=sorted(sites-set().union(*ss)),eligible_edges=edges,minimal=[sorted(z) for z in minimal],forced=sorted(forced),one_based_port_indices=False)
            count['forced_some']+=bool(forced)
            count['any_disjoint_pair_suffices']+=bool(edges) and len(one)==len(edges)
            count['disjoint_but_not_single_repair']+=len(edges)-len(one)
    return dict(width=k,counts=count,examples=examples)
if __name__=='__main__':
    out=[run(k) for k in (7,8)];print(out);path=Path(__file__).resolve().parents[1]/'results/ramsey_square_port_repairs.json';path.write_text(json.dumps(out,indent=2)+'\n')
