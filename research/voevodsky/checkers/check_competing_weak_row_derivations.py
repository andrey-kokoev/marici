"""Weak x+y<=3 has distinct old-row derivations with different surplus."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
old=(((-1,0),0),((1,0),1),((0,-1),0),((0,1),1));weak=((1,1),3)
def image(m,c=Q(0)):
 return tuple(sum(Q(old[i][0][j])*m[i] for i in range(4)) for j in (0,1)),sum(Q(old[i][1])*m[i] for i in range(4))+c
A=((Q(0),Q(1),Q(0),Q(1)),Q(1))
B=((Q(1),Q(2),Q(0),Q(1)),Q(0))
C=((Q(0),Q(1),Q(1),Q(2)),Q(0))
assert image(*A)==image(*B)==image(*C)==weak
cycle=tuple(B[0][i]-A[0][i] for i in range(4))
assert cycle==(1,1,0,0) and image(cycle,0)==((0,0),Q(1))
checks=0
for z,prior_c in product((Q(0),Q(1,2),Q(1),Q(2)),(Q(0),Q(1,2))):
 prior=(Q(0),Q(0),Q(0),Q(0))
 a=(tuple(prior[i]+z*A[0][i] for i in range(4)),prior_c+z*A[1])
 b=(tuple(prior[i]+z*B[0][i] for i in range(4)),prior_c+z*B[1])
 assert image(*a)==image(*b)==((z,z),3*z+prior_c)
 assert tuple(b[0][i]-a[0][i] for i in range(4))==tuple(z*x for x in cycle)
 assert a[1]-b[1]==z
 checks+=1
assert checks==8
# Nonnegative source cycle improves surplus but is not inverse path history.
report={'passed':True,'weak_row':'x+y<=3','derivations':{'A':{'multipliers':['0','1','0','1'],'surplus':'1'},'B':{'multipliers':['1','2','0','1'],'surplus':'0'},'C':{'multipliers':['0','1','1','2'],'surplus':'0'}},'scaled_comparison_cases':checks,'A_to_B':'add z*(1,1,0,0) and subtract z surplus','scope':'Fixed unit-square old rows. Different source-rooted proof packets and margins; no canonical selector, admitted higher comparison cell, actual-history identity or analytic role map.'}
out=Path(__file__).resolve().parents[1]/'results/competing-weak-row-derivations.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
