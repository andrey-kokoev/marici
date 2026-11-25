"""Exact one- and two-port continuation sets on all 51-vertex single deletions of Google's 52-witness. Requires python-sat."""
import sys,json,itertools
from pathlib import Path
from collections import Counter
from pysat.solvers import Solver
D=Path(__file__).resolve().parents[1]/'results';sys.path.insert(0,str(D.parents[1]/'grothendieck'))
from r312_google_extension import adj,n,sets
F=(1<<n)-1
def bits(m):
 while m:b=m&-m;yield b.bit_length()-1;m-=b

def main():
 elev=list(sets(F,11));out=[]
 for h in range(n):
    H=F^(1<<h);large=[s for s in elev if not s>>h&1];lo=sum(1<<v for v in bits(H) if (adj[v]&H).bit_count()<11);candidates=[]
    # Vertices already red-degree 11 cannot gain another red neighbor (12 neighbors would be blue-independent in red graph).
    with Solver(name='g4') as sl:
        for v in bits(lo):
            for u in bits(adj[v]&lo&((1<<v)-1)):sl.add_clause([-1-u,-1-v])
        for s in large:sl.add_clause([v+1 for v in bits(s&lo)])
        while sl.solve():
            m=sum(1<<(i-1) for i in sl.get_model() if i>0)&lo;candidates.append(m);sl.add_clause([-(v+1) if m>>v&1 else v+1 for v in bits(lo)])
    assert adj[h] in candidates;assert all(all(m&s for s in large) and not any(m&adj[v] for v in bits(m)) for m in candidates)
    steps=[];tests=0
    for a,b in itertools.combinations_with_replacement(candidates,2):
        tests+=1
        if not a&b:steps.append([a,b,'red'])
        if next(sets(H&~(a|b),10),None) is None:steps.append([a,b,'blue'])
    out.append(dict(deleted=h,core_elevens=len(large),supports=sorted(candidates),pairs=tests,extensions=steps));print(h,len(candidates),tests,len(steps),flush=True)
 (D/'ramsey312_google_two_step.json').write_text(json.dumps(out));print('sizes',Counter(len(r['supports']) for r in out),'totals',sum(len(r['supports']) for r in out),sum(r['pairs'] for r in out),sum(len(r['extensions']) for r in out))
if __name__=='__main__':main()
