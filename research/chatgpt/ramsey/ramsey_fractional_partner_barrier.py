"""Fractional matching/cover LP for partner misses. Rationalize only nonzero weights; verify both primal and dual inequalities with exact arithmetic; normalize both rational certificates."""
from fractions import Fraction as Q
from math import lcm
from collections import Counter
from scipy.optimize import linprog
import numpy as np
from ramsey_first_link_obstructions import run,bits,D,json

def audit():
    prev={(r['parent'],r['first']):r for r in json.loads((D/'ramsey_partner_bipartitions.json').read_text())};out=[]
    def visit(r,A,M,link,T):
        known=prev[r['parent'],A];V=list(link);S=[M[i] for i in V];tag='two_rows' if known['two_rows'] else 'odd' if known['odd_cycle'] else 'bipartite';rows=T[6]+[t for t in T[5] if not t&A]
        if known['two_rows']:
            x={t:Q(1) for t in known['two_rows']};i=next(i for i in V if link[i]);y={M[i]:Q(1),M[next(bits(link[i]))]:Q(1)}
        else:
            cols={sum(1<<j for j,s in enumerate(S) if not s&t):t for t in rows};keep=[]
            for c in sorted(cols,key=int.bit_count,reverse=True):
                if c and all(c&h!=c for h in keep):keep.append(c)
            mat=np.array([[(c>>i)&1 for c in keep] for i in range(len(S))]);lp=linprog(np.ones(len(keep)),A_ub=-mat,b_ub=-np.ones(len(S)),method='highs');assert lp.success
            rat=lambda f:Q(float(f)).limit_denominator(100000);x={cols[c]:rat(f) for c,f in zip(keep,lp.x) if f>1e-8};y={s:rat(-f) for s,f in zip(S,lp.ineqlin.marginals) if f< -1e-8}
        sx=min(sum(f for t,f in x.items() if not t&s) for s in S);sy=max(sum(f for s,f in y.items() if not s&t) for t in rows);x={t:f/sx for t,f in x.items()};y={s:f/sy for s,f in y.items()};val=sum(x.values());assert val<3 or sum(y.values())>=3;out.append(dict(parent=r['parent'],deleted=r['deleted'],first=A,tag=tag,upper=str(val),lower=str(sum(y.values())),cover={t:str(f) for t,f in x.items()},packing={s:str(f) for s,f in y.items()}))
    run(on_triangle_free=visit);return out
if __name__=='__main__':
    z=audit();print(Counter((r['tag'],Q(r['upper'])<3) for r in z));print(Counter(r['lower'] for r in z).most_common(15));(D/'ramsey_fractional_partner_barrier.json').write_text(json.dumps(z)+'\n')
