"""Two descriptive tests on v1, not bound-conditioned v2. Compare one k-step per unordered cell, including entry into the diagonal from k=l-1. Logs are natural."""
from pathlib import Path
from fractions import Fraction as F
from statistics import median
from collections import Counter
from math import comb,log,exp,isqrt
import csv
D=Path(__file__).resolve().parents[1]/'results';Z={(int(t['l']),int(t['k'])):t for t in csv.DictReader((D/'ramsey_mixed_field_26.csv').open())};R={p:int(z['R_v1']) for p,z in Z.items()};P={(int(t['l']),int(t['k'])):float(t['fit']) for t in csv.DictReader((D/'ramsey_fit_error_ranks.csv').open())};free={};rnd={};pr=[p for p in range(2,50) if all(p%d for d in range(2,isqrt(p)+1))];rows=[]
for a in range(1,27):
 for b in range(a,27):
    if a<=3 or Z[a,b]['audit']=='exact':v=F(R[a,b])
    else:
        U=R[a-1,b]+R[a,b-1];q=F(57*U,64);e=R[a,b]-q;assert -F(1,2)<e<=F(1,2);rnd[a,b]=(U%64,e);v=F(57,64)*(free[a-1,b]+free[a,b-1])
    free[a,b]=free[b,a]=v

def d(arr,a,b):return arr[a,b]-arr[a-1,b]-arr[a,b-1]+arr[a-1,b-1]
for a in range(3,27):
 seen=set()
 for b in range(2,27):
    n=comb(a+b-4,a-2);ps={p for p in pr if n%p==0};new=sorted(ps-seen);seen|=ps
    if b<a:continue
    f=P[a,b]/P[tuple(sorted((a,b-1)))];v=d(R,a,b)/d(R,a,b-1);u=float(d(free,a,b)/d(free,a,b-1));assert u>0 and v>0
    rows.append(dict(l=a,k=b,new=','.join(map(str,new)),rounded=(a,b) in rnd,Umod64=rnd.get((a,b),('',0))[0],local_round=float(rnd.get((a,b),('',0))[1]),delta_log=log(f/v),unrounded_delta_log=log(f/u),ratio=f/v,reverse=(v-1)*(f-1)<0,flat=v==1))
with (D/'ramsey_prime_step_test.csv').open('w',newline='') as fp:
 w=csv.DictWriter(fp,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
print('round count/sign',len(rnd),Counter((e>0)-(e<0) for _,e in rnd.values()),'residue0/32',[(k,[p for p,(r,e) in rnd.items() if r==k]) for k in (0,32)],'mean',float(sum(e for _,e in rnd.values())/len(rnd)))
for label,test in [('all',lambda r:True),('rounded target',lambda r:r['rounded']),('exact both',lambda r:Z[r['l'],r['k']]['audit']==Z[r['l'],r['k']-1]['audit']=='exact')]:
 for new in [True,False]:
    g=[r for r in rows if bool(r['new'])==new and test(r)];print(label,new,len(g),'med',exp(median(t['delta_log'] for t in g)),'unrd',exp(median(t['unrounded_delta_log'] for t in g)),'pos',sum(t['delta_log']>1e-12 for t in g),'reverse',sum(t['reverse'] for t in g),'flat',sum(t['flat'] for t in g))
print('largest',sorted(rows,key=lambda r:-abs(r['delta_log']))[:3])
