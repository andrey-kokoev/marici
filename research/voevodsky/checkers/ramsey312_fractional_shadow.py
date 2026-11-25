"""Look for a fractional obstruction before partition search. Minimize total capacity using the saturated shadow catalog; exact rational check on active dual support."""
from ramsey312_google_two_step import *
from fractions import Fraction
from scipy.optimize import linprog
from functools import reduce
from operator import and_

def solve(d,ss,el,target=6):
 h=F^d;s=sorted(set(ss)|{adj[i]&h for i in bits(d)});n=len(s);full=(1<<n)-1;col=[sum(1<<j for j,x in enumerate(s) if x>>v&1) for v in range(52)];rows={}
 for e in el:
    g=e&d
    if not g:continue
    t=e^g;b=h&reduce(and_,(adj[i] for i in bits(g)));miss=full
    for i in bits(t):miss&=~col[i]
    for i in bits(b):
        mask=miss&col[i];rows.setdefault(g,{}).setdefault(mask,(1<<i,t))
 rs=[]
 for g,rr in rows.items():
    mx=[]
    for p in sorted(rr,key=int.bit_count,reverse=True):
        if not any(p&~v==0 for v in mx):mx.append(p);rs.append((g,*rr[p],p))
 res=linprog([g.bit_count() for g,b,t,p in rs],A_ub=[[-(p>>i&1) for g,b,t,p in rs] for i in range(n)],b_ub=[-1]*n,method='highs');assert res.success;w=[Fraction(float(x)).limit_denominator(100000) for x in res.x];y=[Fraction(float(-x)).limit_denominator(100000) for x in res.ineqlin.marginals];assert min(y)>=0 and all(sum(y[j] for j in bits(p))<=g.bit_count() for g,b,t,p in rs);cert=[(g,b,t,a) for (g,b,t,p),a in zip(rs,w) if a]
 if sum(y)>target:cert=[] # Only the exact dual lower bound is needed.
 else:cert=[(g,b,t,float(a)) for (g,b,t,p),a in zip(rs,res.x) if a>1e-9] # floating primal only for discovery; replay separately if no violation found.
 return sum(y),[(x,str(a)) for x,a in zip(s,y) if a],cert

def main():
 import sys
 el=list(sets(F,11));out=[]
 for suffix,f in zip(['','19'],sys.argv[1:]):
    r=json.loads((D/f'ramsey312_no_budget{suffix}.json').read_text());d,*full=map(int,open(f).read().split());assert d==r['d'];ss=r['challenge'];turn=0
    while True:
        turn+=1;v,y,cert=solve(d,ss,el);print(d,turn,len(ss),v,'dual',len(y),'classes',len(cert),flush=True)
        if v>6:break
        missed=[x for x in full if sum(a for g,b,t,a in cert if x&b and not x&t)<1-1e-7];
        if not missed:break
        ss=ss+missed[::max(1,len(missed)//40)][:41]
    out.append(dict(d=d,value=str(v),dual=y,classes=[(g,b,t,str(a)) for g,b,t,a in cert],rounds=turn))
 (D/'ramsey312_fractional_shadow.json').write_text(json.dumps(out))
if __name__=='__main__':main()
