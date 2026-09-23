"""Typed source-bound refinement transport and its lax normalizer square."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
def valid(p,L,T):
 a,b,c=map(Q,p);L,T=Q(L),Q(T)
 return L>0 and min(a,b,c)>=0 and b-a==1 and L*b+c==T
def normal(p,L,T):
 assert valid(p,L,T)
 a,b,c=map(Q,p);shift=c/Q(L)
 q=(a+shift,b+shift,Q(0));assert valid(q,L,T);return q
def change(p,L,K,T):
 assert valid(p,L,T) and Q(K)>0
 a,b,c=map(Q,p);q=(a,b,c+(Q(L)-Q(K))*b)
 if not valid(q,K,T):raise ValueError('SOURCE_WIDENING_LOSES_PROOF')
 return q
checks=0;strict_fail=0
for L,K,T in product((Q(1,2),Q(1),Q(2),Q(3)),repeat=3):
 if K>L or T<L:continue
 p=(Q(0),Q(1),Q(T)-Q(L))
 direct=normal(change(p,L,K,T),K,T)
 staged=normal(change(normal(p,L,T),L,K,T),K,T)
 assert direct==staged==(T/K-1,T/K,Q(0))
 if change(normal(p,L,T),L,K,T)!=direct:strict_fail+=1
 checks+=1
assert checks>10 and strict_fail>0
p=(Q(1),Q(2),Q(1))
assert valid(p,1,3)
assert change(p,1,Q(1,2),3)==(Q(1),Q(2),Q(2))
assert normal(change(p,1,Q(1,2),3),Q(1,2),3)==(Q(5),Q(6),Q(0))
try:change((Q(0),Q(1),Q(0)),1,2,1)
except ValueError:widening_refused=True
else:raise AssertionError('invalid widened-source certificate')
assert not valid((Q(2),Q(3),Q(0)),2,3) # stale old source normal form
report={'passed':True,'refinement_squares_checked':checks,'strict_failures':strict_fail,'lax_refinement':'N_K change_LK = N_K change_LK N_L for 0<K<=L and valid proofs','widening_counterexample':'x<=1 on [0,1] does not prove x<=1 on [0,2]','widening_refused':widening_refused,'scope':'One-dimensional positive source upper bound, same target x<=T; retaining both primitive row bounds mandatory. No proof-path cell, analytic correspondence, or authority.'}
out=Path(__file__).resolve().parents[1]/'results/source-bound-change.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
