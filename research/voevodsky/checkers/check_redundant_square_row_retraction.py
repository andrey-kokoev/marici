"""Redundant x+y<=2 row yields split retraction, not inverse proof path."""
from fractions import Fraction as Q
from pathlib import Path
import json
old=(((-1,0),0),((1,0),1),((0,-1),0),((0,1),1))
new=old+(((1,1),2),)
def image(rows,m):return tuple(sum(Q(rows[i][0][j])*m[i] for i in range(len(m))) for j in (0,1)),sum(Q(rows[i][1])*m[i] for i in range(len(m)))
def include(m):return tuple(m)+(Q(0),)
def retract_linear(n):
 a,x,b,y,z=map(Q,n)
 return (a,x+z,b,y+z)
def retract(n):
 if min(map(Q,n))<0:raise ValueError('NEGATIVE_MULTIPLIER')
 return retract_linear(n)
def section(m):assert len(m)==4;return include(m)
P=(Q(1),Q(2),Q(0),Q(0));Qp=(Q(0),Q(1),Q(1),Q(1));K=tuple(Qp[i]-P[i] for i in range(4))
for m in (P,Qp):assert image(new,include(m))==image(old,m) and retract(include(m))==m
assert image(new,include(K))==image(old,K)==((0,0),0)
added=(Q(0),Q(0),Q(0),Q(0),Q(1));mapped=retract(added)
assert image(new,added)==image(old,mapped)==((1,1),2)
assert include(mapped)!=(added) and mapped==(0,1,0,1)
# A signed zero-normal, zero-bound relation connects added row to old highs.
relation=tuple(added[i]-include(mapped)[i] for i in range(5))
assert relation==(0,-1,0,-1,1) and image(new,relation)==((0,0),0)
assert retract_linear(relation)==(0,0,0,0)
assert image(new,added)!=image(new,include((0,0,0,0)))
report={'passed':True,'new_redundant_row':'x+y<=2','forward_inclusion_and_retraction_preserve_normal_bound':True,'retraction_after_inclusion_identity':True,'inclusion_after_retraction_not_identity':True,'signed_zero_bound_kernel':list(map(str,relation)),'old_comparison_path_forward_preserved':True,'scope':'Exact fixed square redundant-row presentation. Retraction is a nonnegative proof-data map, not inverse on proof histories, real source issuer migration, or analytic role functor.'}
out=Path(__file__).resolve().parents[1]/'results/redundant-square-row-retraction.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
