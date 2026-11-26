"""Find a saturated split with enough fractional but insufficient integer capacity."""
import itertools, json, math, random
from fractions import Fraction
from pathlib import Path
import networkx as nx
import numpy as np
from scipy.optimize import linprog,milp,Bounds,LinearConstraint

def test(g):
    n=len(g);H=nx.complement(g);fac=sorted(sum(1<<i for i in c) for c in nx.find_cliques(H));rows=[s for s in range(1,1<<n) if any(s&f==s for f in fac)];need=np.array([s.bit_count() for s in rows]);M=np.array([[bool(s&f) for f in fac] for s in rows],dtype=float);c=np.ones(len(fac));r=linprog(c,A_ub=-M,b_ub=-need);a=max(int(max(need))+1,math.ceil(r.fun-1e-7));
    z=milp(c,integrality=c,bounds=Bounds(0,np.inf),constraints=LinearConstraint(M,need,np.inf));
    if z.fun<=a+1e-6:return
    weights=[Fraction(v).limit_denominator(100000) for v in r.x];assert sum(weights)<=a and all(sum(w for w,f in zip(weights,fac) if f&s)>=s.bit_count() for s in rows)
    return dict(n=n,edges=sorted(g.edges()),a=a,fac=fac,weights=list(map(str,weights)),integer=round(z.fun))
if __name__=='__main__':
    for g in nx.graph_atlas_g():
        if not len(g) or not nx.is_connected(g) or any(nx.triangles(g).values()):continue
        res=test(g)
        if res:break
    else:
        rng=random.Random(4344)
        for j in range(5000):
            n=8+j//500;g=nx.empty_graph(n);es=list(itertools.combinations(range(n),2));rng.shuffle(es)
            for i,k in es:
                if rng.random()<.55 and not(set(g[i])&set(g[k])):g.add_edge(i,k)
            res=test(g)
            if res:break
        else:raise SystemExit('no gap found')
    print(res,flush=True);(Path(__file__).resolve().parents[1]/'results'/'ramsey_split_fractional_gap.json').write_text(json.dumps(res,indent=1)+'\n')
