"""Can three distinct old rows still attach together? Allow legal red links between disjoint rows."""
from itertools import combinations,pairwise
from functools import lru_cache
from collections import Counter
from ramsey_inherited_swap_selector import run,D
import json


def oracle(k,sq,edges):
    core=edges|{(i,i+1) for i in range(1,k)}; V=set(range(1,k+1)); independent=lambda q:not any(e in core for e in combinations(q,2))
    @lru_cache(None)
    def cap(v):
        vs=sorted(v)
        return next(n for n in range(len(vs),-1,-1) if any(independent(q) for q in combinations(vs,n)))
    @lru_cache(None)
    def risky(rows):
        # Blue seven through all listed ports; applies if their mutual links are blue.
        old=[r for r in sq if all(set(r)&set(s) for s in rows)]
        return any(len(rows)+n+cap(frozenset(V-set().union(*rows,*sub)))>=7 for n in range(len(old)+1) for sub in combinations(old,n))
    @lru_cache(None)
    def option(a,b):return set(a).isdisjoint(b) and all(set(r)&(set(a)|set(b)) for r in sq)
    def legal(rows):
        if any(not independent(r) or risky((r,)) for r in rows):return False
        pairs=list(combinations(rows,2));required=[p for p in pairs if risky(p)]
        if any(not option(*p) for p in required) or len(required)==3:return False
        # If all three blue would fail, one permissible red link suffices unless
        # a link is already required. Two red links never form a port triangle.
        return bool(required) or not risky(rows) or any(option(*p) for p in pairs)
    def diagnose(rows):
        pairs=list(combinations(rows,2));required=[p for p in pairs if risky(p)]
        if len(required)==3 and all(option(*p) for p in pairs):return 'three_required_red_links'
        assert not required and risky(rows) and not any(option(*p) for p in pairs)
        if all(set(a)&set(b) for a,b in pairs):return 'fixed_seven_overlapping_supports'
        return 'fixed_seven_blocked_by_square_port'
    return legal,diagnose


def main():
    counts=Counter();example=None;mechanisms=Counter();witnesses={}
    def inspect(sq,path,swaps,children):
        nonlocal example
        old={tuple(sorted(e)) for e in pairwise(path)};ends={path[0],path[-1]};c=old|{(i,10) for i in ends};fixed,=set.intersection(*map(set,sq));row=sorted({fixed}|ends)
        if not swaps or all(b-a>1 for a,b in pairwise(row)) or not any(c==e and swaps<=v for e,v in children):return
        a,_=oracle(9,sq,old);b,diagnose=oracle(10,sq,c);rows=[s for s in combinations(range(1,10),3) if s not in sq and min(s[1]-s[0],s[2]-s[1])>=2 and a((s,))];loss=False;triple_only=False
        for triple in combinations(rows,3):
            if not a(triple):continue
            counts['legal_old_triples']+=1
            if b(triple):continue
            loss=True;counts['lost_triples']+=1
            if all(b(p) for p in combinations(triple,2)):
                counts['lost_with_all_pairs_legal']+=1;triple_only=True
                tag=diagnose(triple);mechanisms[tag]+=1;witnesses.setdefault(tag,dict(square=sq,path=path,rows=triple))
                if example is None:example=dict(square=sq,path=path,rows=triple)
        counts['predecessors']+=1;counts['predecessors_with_loss']+=loss;counts['predecessors_with_triple_only_loss']+=triple_only
    run(inspect);assert counts['predecessors']==23;assert sum(mechanisms.values())==232;res=dict(counts=counts,example=example,mechanisms=mechanisms,witnesses=witnesses);print(res);(D/'ramsey_inherited_three_ports.json').write_text(json.dumps(res,indent=2)+'\n')
if __name__=='__main__':main()
