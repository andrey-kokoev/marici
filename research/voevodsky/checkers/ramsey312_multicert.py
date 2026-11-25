"""Compress an ordinary coloring using separate minimal red and maximal blue frontiers. Find short witness lists for intersecting footprints, and test the stronger majority (fractional) certificate."""
from ramsey312_google_two_step import *
from scipy.optimize import linprog
from fractions import Fraction
from functools import reduce
from operator import or_

def frontier(s,up):
 f=[]
 for x in sorted(s,key=lambda x:((-1 if up else 1)*x.bit_count(),x)):
    if not any((x&y)==(x if up else y) for y in f):f.append(x)
 return f

def compress(f,rows):
 n=len(f);opts={}
 for witness,p in rows:
    if p:opts.setdefault(p,witness)
 mx=[]
 for p in sorted(opts,key=lambda p:(-p.bit_count(),p)):
    if not any(p&r==p for r in mx):mx.append(p)
 # cover all unordered pairs incl self; score via bitset population across remaining upper triangular rows
 remain=[(1<<(j+1))-1 for j in range(n)];sel=[];L={p:list(bits(p)) for p in mx}
 while any(remain):
    p=max(mx,key=lambda p:sum((remain[j]&p).bit_count() for j in L[p]));assert any(remain[j]&p for j in L[p]);sel.append(opts[p]);
    for j in L[p]:remain[j]&=~p
 # Minimize total weight hitting each support with weight >=1. Total <2 suffices for pairwise intersection.
 mat=[[-(p>>i&1) for p in mx] for i in range(n)];res=linprog([1]*len(mx),A_ub=mat,b_ub=[-1]*n,method='highs');assert res.success;ww=[Fraction(float(x)).limit_denominator(1000000) for x in res.x];dual=[Fraction(float(-x)).limit_denominator(1000000) for x in res.ineqlin.marginals];exact=all(sum(ww[j] for j,p in enumerate(mx) if p>>i&1)>=1 for i in range(n)) and all(sum(dual[i] for i in bits(p))<=1 for p in mx) and sum(ww)==sum(dual) and min(ww+dual)>=0
 return dict(witnesses=sel,maximal_patterns=len(mx),weight=str(sum(ww)) if exact else float(res.fun),exact=exact,majority=[[opts[p],str(w)] for p,w in zip(mx,ww) if w] if exact and sum(ww)<2 else None)

def main():
 r=json.loads((D/'ramsey312_no_budget_coloring.json').read_text());h=F^r['d'];ts=list(sets(h,10));out=[]
 for k in range(6):
    s=[x for x,c in zip(r['supports'],r['color']) if c==k];lo=frontier(s,False);hi=frontier(s,True);col=lambda f:{i:sum(1<<j for j,x in enumerate(f) if x>>i&1) for i in bits(h)};lc=col(lo);hc=col(hi);full=(1<<len(hi))-1
    red=compress(lo,[(1<<i,p) for i,p in lc.items()]);blue=compress(hi,[(t,full&~reduce(or_,(hc[i] for i in bits(t)))) for t in ts]);print(k,len(s),len(lo),len(hi),[(len(q['witnesses']),q['weight'],q['maximal_patterns']) for q in (red,blue)],flush=True);out.append(dict(k=k,n=len(s),lo=len(lo),hi=len(hi),red=red,blue=blue))
 (D/'ramsey312_multicert.json').write_text(json.dumps(out))
if __name__=='__main__':main()
