"""Compose directed N=4 moments, constants, prime terms, and coarse tails into c=1 Gram cells."""
from fractions import Fraction as F
import json
import preconditioned_spline_weil as w
src=json.load(open('research/grothendieck/results/interval-undilated-septic-moments.json'))
def frac(s): return F(s)
mom={(r['profile'],int(r['n'])):(frac(r['interval'][0]),frac(r['interval'][1])) for r in src['rows']}
BASE_C=[F(1),F(-5),F(33,4),F(-5),F(1)];BASE_M=[2,1,0,-1,-2]
def lag(k):
 d={}
 for c,m in zip(BASE_C,BASE_M):
  for t in (k,-k):d[m+t]=d.get(m+t,F(0))+c/2
 ms=sorted(d,reverse=True);return [d[m] for m in ms],ms
profiles={'baseline':(BASE_C,BASE_M),'cross':lag(1),'lag2':lag(2)}
a=w.log_q(F(4));gp=w.add(w.gamma_interval(),(w.log_q(w.pi_interval()[0])[0],w.log_q(w.pi_interval()[1])[1]))
E=F('0.06101538');cells={}
for name,(cs,ms) in profiles.items():
 w.COEFF=list(cs);w.SHIFT_INDEX=list(ms)
 f0=w.shifted_k(w.Z,a);finite=w.Z
 source_name='lag2_cross' if name=='lag2' else name
 for n in range(4):finite=w.add(finite,w.sub(w.scale(F(1,n+1),f0),mom[(source_name,n)]))
 prefix=w.add(w.sub(finite,w.mul(gp,f0)),w.prime_term(a))
 cells[name]=(prefix[0]-E,prefix[1]+E)
def add(x,y):return (x[0]+y[0],x[1]+y[1])
def neg(x):return (-x[1],-x[0])
def mul(x,y):
 v=[a*b for a in x for b in y];return(min(v),max(v))
def sub(x,y):return add(x,neg(y))
def sc(k,x):return mul((F(k),F(k)),x)
d,c1,c2=cells['baseline'],cells['cross'],cells['lag2'];m2=sub(mul(d,d),mul(c1,c1));x2=mul(c1,c1)
det=sub(add(sub(mul(mul(d,d),d),sc(2,mul(d,x2))),sc(2,mul(x2,c2))),mul(d,mul(c2,c2)))
assert d[0]>0 and m2[0]>0 and det[0]>0
fl=lambda x:[float(x[0]),float(x[1])]
print(json.dumps({'schema':'marici.nima.c-one-n4-directed-gram.v1','status':'passed','cells':{k:fl(v) for k,v in cells.items()},'leading_minor_2':fl(m2),'determinant_3':fl(det),'positive_definite_rank_three':True,'tail_error_each':float(E),'claim_boundary':'declared executable c=1 explicit-formula assembly; external theorem sign/involution identification remains separate'},sort_keys=True))
