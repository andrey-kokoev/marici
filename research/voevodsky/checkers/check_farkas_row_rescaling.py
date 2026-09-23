"""Nontrivial presentation change: positive primitive upper-row rescaling."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
# A primitive upper row rho*x<=rho*L, rho>0, and lower -x<=0.
# Its proof (a,b;c) obeys rho*b-a=1 and rho*L*b+c=T.
def valid(p,L,rho,T):
 a,b,c=map(Q,p);L,rho,T=Q(L),Q(rho),Q(T)
 return min(a,b,c)>=0 and L>0 and rho>0 and rho*b-a==1 and rho*L*b+c==T
def change(p,L,rho,sigma,T):
 if min(Q(rho),Q(sigma))<=0:raise ValueError('ROW_SCALING_MUST_BE_POSITIVE')
 assert valid(p,L,rho,T)
 a,b,c=map(Q,p);out=(a,b*Q(rho)/Q(sigma),c)
 assert valid(out,L,sigma,T);return out
def norm(p,L,rho,T):
 assert valid(p,L,rho,T)
 a,b,c=map(Q,p);out=(a+c/Q(L),b+c/(Q(L)*Q(rho)),Q(0))
 assert valid(out,L,rho,T);return out
checks=0;naive_fail=0
for L,rho,sigma,T in product((Q(1,2),Q(1),Q(2),Q(3)),repeat=4):
 if T<L:continue
 p=(Q(0),Q(1)/rho,T-L)
 left=norm(change(p,L,rho,sigma,T),L,sigma,T)
 right=change(norm(p,L,rho,T),L,rho,sigma,T)
 assert left==right==(T/L-1,T/(L*sigma),Q(0))
 if sigma!=rho and not valid(p,L,sigma,T):naive_fail+=1
 checks+=1
assert checks>20 and naive_fail>0
# Wrong 'keep multiplier unchanged' map is not a well-typed row-presentation
# change even when both primitive inequalities denote the same subset.
p=(Q(1),Q(2),Q(1));assert valid(p,1,1,3)
assert change(p,1,1,2,3)==(Q(1),Q(1),Q(1))
assert not valid(p,1,2,3)
try:change(p,1,1,-1,3)
except ValueError:negative_refused=True
else:raise AssertionError('negative row scaling was admitted')
report={'passed':True,'rescaling_squares_checked':checks,'naive_unchanged_multiplier_failures':naive_fail,'naturality':'N_sigma R_rho_sigma = R_rho_sigma N_rho strictly on packets for fixed L,T','negative_scaling_refused':negative_refused,'scope':'Positive rescaling of SAME primitive upper inequality rho*x<=rho*L with source provenance. Not a source-set change, proof-history identity, analytic role map or live authority.'}
out=Path(__file__).resolve().parents[1]/'results/farkas-row-rescaling.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
