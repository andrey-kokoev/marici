"""Positive dlog representatives for all fifteen right-nested source histories."""
from pathlib import Path
import json
import sympy as s
from nine_point_source_r import Kinematics
root=Path(__file__).resolve().parents[1]
histories=[h for h in json.loads((root/'results/nine-point-source-history-contract.json').read_text())['records'] if h['branch']=='right-nested'];assert len(histories)==15
inputs=json.loads((root/'results/nine-point-missing-support-histories.json').read_text())['witnesses']
common=[(w['e'],s.Matrix([[s.Rational(x) for x in row] for row in w['quotient_twistors']])) for w in inputs]
q=s.symbols('x1:5')+s.symbols('y1:5');Z6=s.Matrix([[t**j for j in range(6)] for t in range(1,10)])
positive_point=dict(zip(q,(1,2,3,4,2,3,4,5)));records=[];tests=0
for h in histories:
 a1,b1=h['outer_pair'];a,b=h['inner_pair'];outer=(a1-1,a1,b1-1,b1);inner=(a-1,a,b-1,b)
 C=s.zeros(2,9)
 for j,i in enumerate(outer):C[0,i-1]+=q[j]
 C[0,8]=-1;C[1,8]=1
 if a==b1:
  C[1,b1-2]+=q[4]*q[2];C[1,b1-1]+=q[4]*q[3]
 else:C[1,a-2]+=q[4]
 for j,i in enumerate(inner[1:],5):C[1,i-1]+=q[j]
 minors={(i,j):s.expand(C[:,[i-1,j-1]].det()) for i in range(1,10) for j in range(i+1,10)}
 assert all(m==0 or all(v>0 for v in s.Poly(m,*q).coeffs()) for m in minors.values())
 Y=C.subs(positive_point)*Z6;chart=Y[:,:2].inv()*Y[:,2:]
 fixtures=common+[('own_positive_image',Z6[:,2:]-Z6[:,:2]*chart)];witnesses=[]
 for label,z in fixtures:
  av=z[[i-1 for i in outer],:].T.inv()*z[8,:].T
  first=av[2]*z[b1-2,:]+av[3]*z[b1-1,:] if a==b1 else z[a-2,:]
  bv=-s.Matrix.vstack(first,*(z[i-1,:] for i in inner[1:])).T.inv()*z[8,:].T
  values=list(av)+list(bv);point=dict(zip(q,values));assert C.subs(point)*z==s.zeros(2,4)
  if label=='own_positive_image':assert point==positive_point
  J=s.Matrix.hstack(*[s.Matrix(list(C.diff(v).subs(point)*z)) for v in q]).det(method='domain-ge')
  assert J!=0 and all(v!=0 for v in values)
  density=s.factor(1/(s.prod(values)*J));kin=Kinematics(z.tolist());A,f=kin.ordinary(a1,b1);B,g=kin.inner(a1,b1,a,b,'right-nested')
  wedges={pair:s.factor(A[pair[0]]*B[pair[1]]-A[pair[1]]*B[pair[0]]) for pair in minors}
  pivot=next(pair for pair,m in minors.items() if m.subs(point)!=0);scale=s.factor(wedges[pivot]/minors[pivot].subs(point))
  assert scale!=0 and all(s.factor(wedges[pair]-scale*m.subs(point))==0 for pair,m in minors.items())
  assert s.factor(f*g*scale**4-density)==0,(h,label)
  tests+=1;witnesses.append({'input':label,'positive_preimage':all(v>0 for v in values),'coordinates':list(map(str,values)),'jacobian':str(J)})
 records.append({'history':h,'cell_matrix':[[str(x) for x in row] for row in C.tolist()],'witnesses':witnesses})
report={'passed':True,'right_history_count':len(records),'boundary_updated_count':sum(bool(h['boundary_updates']) for h in histories),'exact_full_tensor_checks':tests,'symbolic_positive_minor_checks':15,'records':records,'scope':'All15 right-nested histories have subtraction-free ordered minors and localized dlog calibration at two common targets plus their own regular positive images. No all-kinematics identity proof or completeness/overlap proof;35 left-nested cells remain.'}
(root/'results/nine-point-right-history-cells.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items() if k!='records'},indent=2))
