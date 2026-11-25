"""Build a fractional support packing directly from a deleted triple's common neighbors. No input support lists, pivot labels, colors or saved cyclic orders."""
from ramsey312_google_two_step import *
from itertools import combinations
from scipy.optimize import linprog
from fractions import Fraction
import math

def solve(h,C,tens,elev):
 # Maximal independent supports containing C via Bron-Kerbosch on the complement.
 p=h&~C
 for i in bits(C):p&=~adj[i]
 s=[]
 def bk(x,p,e):
    if not p|e:
        if all(x&t for t in elev):s.append(x)
        return
    u=max(bits(p|e),key=lambda j:(p&~(adj[j]|1<<j)).bit_count());cand=p&(adj[u]|1<<u)
    for j in bits(cand):
        b=1<<j;allow=~(adj[j]|b);bk(x|b,p&allow,e&allow);p^=b;e|=b
 bk(C,p,0);s.sort();cols={v:sum(1<<j for j,x in enumerate(s) if x>>v&1) for v in bits(h)};full=(1<<len(s))-1;foot=set()
 for t in tens:
    p=full
    for v in bits(t):p&=~cols[v]
    if p:foot.add(p)
 rows=[]
 for p in sorted(foot,key=lambda p:(-p.bit_count(),p)):
    if not any(p&r==p for r in rows):rows.append(p)
 if not s:return dict(value='0',packing=[],facets=0)
 A=[[int(p>>j&1) for j in range(len(s))] for p in rows];res=linprog([-1]*len(s),A_ub=A,b_ub=[1]*len(A),method='highs');assert res.success
 w=[Fraction(float(x)).limit_denominator(10000) for x in res.x];dual=[Fraction(float(-x)).limit_denominator(10000) for x in res.ineqlin.marginals];assert min(w)>=0 and min(dual)>=0 and all(sum(w[j] for j in bits(p))<=1 for p in rows) and all(sum(y for y,p in zip(dual,rows) if p>>j&1)>=1 for j in range(len(s))) and sum(w)==sum(dual)
 return dict(value=str(sum(w)),facets=len(s),packing=[[s[j],str(x)] for j,x in enumerate(w) if x],rows=len(rows))

def main():
 T=list(sets(F,10));E=list(sets(F,11));out=[]
 for r in json.loads((D/'ramsey312_failed_cover_colorings.json').read_text()):
    d=r['d'];h=F^sum(1<<i for i in d);ts=[t for t in T if not t&~h];es=[t for t in E if not t&~h];trip=[(a,adj[a[0]]&adj[a[1]]&adj[a[2]]&h) for a in combinations(d,3)];m=max(c.bit_count() for a,c in trip)
    for a,c in trip:
        if c.bit_count()!=m or not c:continue
        z=solve(h,c,ts,es);print(d,a,c.bit_count(),z['facets'],z['value'],len(z['packing']),sorted(set(w for x,w in z['packing'])),flush=True);out.append(dict(d=d,triple=a,center=c,**z))
 (D/'ramsey312_center_packing.json').write_text(json.dumps(out))
if __name__=='__main__':main()
