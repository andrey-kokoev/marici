"""Exact Laurent-jet sufficiency and loss-of-information controls."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
paths=[Path(__file__),HERE/'triangle-cartesian-pole.md',HERE/'triangle-measure-transport.md']
def hashes():return {p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
def mul(p,q):
 out={}
 for i,a in p.items():
  for j,b in q.items():out[i+j]=out.get(i+j,F(0))+a*b
 return {i:a for i,a in out.items() if a}
before=hashes();count=0
for r1 in map(F,(1,2)):
 for r2 in map(F,(-1,0,3)):
  for A in map(F,(1,3)):
   for B in map(F,(0,1,7)):
    R={1:r1,2:r2};G={-1:A,0:B,1:F(5)};P=mul(R,G)
    P0=P.get(0,F(0));P1=P.get(1,F(0))
    assert P0==r1*A and P1==r1*B+r2*A
    assert P0/r1==A and P1/r1-r2*P0/(r1*r1)==B
    for sigma in map(F,(-2,0,1)):
     shifted=mul({0:F(1),1:sigma},G);PS=mul(R,shifted)
     assert shifted.get(0,F(0))==B+sigma*A
     assert PS.get(0,F(0))==P0
     assert PS.get(1,F(0))==P1+r1*sigma*A
     count+=1
P_a=mul({1:F(2),2:F(3)},{-1:F(5),0:F(7)})
P_b=mul({1:F(2),2:F(3)},{-1:F(5),0:F(11)})
assert P_a[0]==P_b[0]==10 and P_a[1]==29 and P_b[1]==37
assert before==hashes()
report={'passed':True,'source_unchanged':True,'source_sha256':before,'jet_controls':count,
 'counterexample':{'same_P0':10,'different_finite_parts':[7,11],'distinguishing_P1':[29,37]},
 'recovery':'A=P0/r1; B=P1/r1-r2*P0/r1^2',
 'actual_ratio_expansion':'r1=H/3; r2=-2log(2)*H/3',
 'actual_finite_part_if_supplied':'B=(3/H)*(P1+2log(2)*P0)',
 'scope':'Formal simple-pole germs. Does not assert two different germs are admitted physical realizations of the same fixed source, nor choose finite part as the physical observable.'}
(HERE/'triangle-readout-jet.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
