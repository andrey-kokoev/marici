from nine_point_source_r import Kinematics
import sympy as s
from pathlib import Path
import json
checks=0;scales=[]
for shift,parameters in enumerate((range(1,10),(1,2,4,7,11,16,22,29,37))):
 kin=Kinematics([(1,t,t*t,t**3) for t in parameters])
 for a in range(2,9):
  for b in range(a+2,9):
   A,p=kin.ordinary(a,b);B,q=kin.five_bracket(a,b)
   pivot=next(i for i in B if B[i]);scale=s.factor(A[pivot]/B[pivot])
   assert scale!=0 and all(s.factor(A[i]-scale*B[i])==0 for i in A)
   assert s.factor(p*scale**4-q)==0,(shift,a,b,s.factor(p*scale**4/q))
   checks+=1;scales.append(str(scale))
report={'passed':True,'ordinary_R_cases':checks,'witnesses':2,'check':'Entire fermion row proportional and prefactor*scale^4 equals cyclic five-bracket normalization','scope':'Exact ordinary R normalization only; generalized boundary substitutions not yet certified.'}
p=Path(__file__).resolve().parents[1]/'results/nine-point-ordinary-r-normalization.json';p.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
