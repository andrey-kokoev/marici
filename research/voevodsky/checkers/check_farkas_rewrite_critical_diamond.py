"""Exact partial-rewrite critical diamond; endpoint join is not a 3-cell."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
def valid(p,T,bound=Q(1)):
 a,b,c=map(Q,p);return min(a,b,c)>=0 and b-a==1 and b*Q(bound)+c==Q(T)
def step(p,lam,T,root='S[-x<=0,x<=1]'):
 if root!='S[-x<=0,x<=1]':raise PermissionError('FOREIGN_ROOT')
 a,b,c=map(Q,p);lam=Q(lam);assert valid(p,T) and 0<=lam<=c
 q=(a+lam,b+lam,c-lam);assert valid(q,T);return q
checks=0;nonidentical=0
for total,lam,mu in product((Q(1),Q(3,2),Q(2),Q(3)),(Q(0),Q(1,2),Q(1)),(Q(0),Q(1,2),Q(1))):
 if lam+mu>total:continue
 p=(Q(0),Q(1),total);T=1+total
 left_mid=step(p,lam,T);right_mid=step(p,mu,T)
 left=step(left_mid,mu,T);right=step(right_mid,lam,T)
 assert left==right==step(p,lam+mu,T)
 if lam!=mu and lam and mu:nonidentical+=1
 # Finishing each route by the remaining surplus reaches canonical proof.
 assert step(left,left[2],T)==(total,1+total,Q(0))
 checks+=1
assert checks>10 and nonidentical>0
p=(Q(0),Q(1),Q(2));T=Q(3)
assert step(step(p,Q(1,2),T),Q(3,2),T)==step(step(p,Q(3,2),T),Q(1,2),T)==(Q(2),Q(3),Q(0))
assert step(p,Q(1,2),T)!=step(p,Q(3,2),T)
try:step(p,3,T)
except AssertionError:overdraw_refused=True
else:raise AssertionError('overspent surplus')
try:step(p,1,T,root='foreign')
except PermissionError:foreign_refused=True
else:raise AssertionError('foreign root')
# With primitive bound 2, (lambda,lambda,-lambda) changes bound by +lambda:
# the same directed rewrite cannot be transported unchanged.
assert not valid((Q(1),Q(2),Q(1)),T,bound=Q(2))
report={'passed':True,'partial_diamonds_checked':checks,'different_nontrivial_intermediates':nonidentical,'join':'two partial syzygy steps commute on final proof (a+lambda+mu,b+lambda+mu,c-lambda-mu)','overspent_surplus_refused':overdraw_refused,'foreign_root_refused':foreign_refused,'higher_path_equality':'unsupported: distinct rewrite traces; no declared interchange 3-cell','scope':'Fixed primitive interval, nonnegative partial rewrites with lambda+mu<=c; neither actual-history authority nor analytic comparison.'}
out=Path(__file__).resolve().parents[1]/'results/farkas-rewrite-critical-diamond.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
