"""Region SAT proof: no stored core colors, no imposed symmetry. Requires python-sat."""
from itertools import product,combinations
from pathlib import Path
import json
from pysat.solvers import Solver
from pysat.card import CardEnc


def audit():
    cs=[''.join(w) for w in product('01*',repeat=3) if w!=('*',)*3];corners=[c for c in cs if '*' not in c];m={s:sum(1<<i for i,b in enumerate(corners) if all(x in ('*',y) for x,y in zip(s,b))) for s in cs};V={frozenset((s,t)):n for n,(s,t) in enumerate((p for p in combinations(cs,2) if not m[p[0]]&m[p[1]]),1)}
    def edges(q):return [V[e] for p in combinations(q,2) if (e:=frozenset(p)) in V]
    tri=[[-i for i in v] for q in combinations(cs,3) if len(v:=edges(q))==3];degree=[];top=len(V)
    for s in cs:
        f=CardEnc.equals([v for e,v in V.items() if s in e],8-m[s].bit_count(),top_id=top);degree.extend(f.clauses);top=f.nv
    reps=[('*00','**1','*1*'),('**0','*01','*11')];out=[];pos=set()
    for k in range(2,8):
        for L in range(256):
            if L.bit_count()!=k:continue
            for q in combinations([s for s in cs if not m[s]&~L],k+1):pos.add(tuple(edges(q)))
        for deg in (False,True):
            with Solver(name='cadical195',bootstrap_with=tri+list(pos)+(degree if deg else [])) as sl:
                tests={}
                for s,t,u in reps:
                    a,b=edges((s,t))[0],edges((s,u))[0];tests[' '.join((s,t,u))]={str(i)+str(j):sl.solve(assumptions=[i*a if i else -a,j*b if j else -b]) for i,j in product(range(2),repeat=2)}
                out.append(dict(max_region=k,degree=deg,positive_clauses=len(pos),tests=tests));print(k,deg,tests,flush=True)
        if all(not v['00'] and not v['11'] for v in out[-1]['tests'].values()):break
    (Path(__file__).resolve().parents[1]/'results/ramsey_wedge_region_bound.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
