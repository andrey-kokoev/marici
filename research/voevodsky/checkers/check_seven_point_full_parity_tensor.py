"""Exact full parity tensor comparison using its positive-definite Gram norm.

For rational v_r in Q^35, T=sum_r w_r v_r^{tensor 4} has
||T||^2=sum_rs w_r w_s (v_r dot v_s)^4.
Zero norm is equivalent to every ordered tensor coefficient vanishing.
"""
from pathlib import Path
import contextlib,io,itertools,json,hashlib
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_seven_point_parity as prior
from nine_point_source_r import Kinematics
root=Path(__file__).resolve().parents[1]
choices=list(itertools.combinations(range(1,8),4))

def vectors(kin,degree,dual=False):
 result=[]
 for M,w in prior.amplitude_terms(kin,degree):
  values=[]
  for subset in choices:
   columns=[i-1 for i in range(1,8) if i not in subset] if dual else [i-1 for i in subset]
   sign=(-1)**(sum(i-1 for i in subset)-6) if dual else 1
   values.append(s.factor(sign*M[:,columns].det()))
  pivot=next(x for x in values if x)
  result.append((s.factor(w*pivot**4),s.Matrix([s.factor(x/pivot) for x in values])))
 return result

def contraction(left,right):
 return s.factor(sum(w*u*(v.dot(z))**4 for w,v in left for u,z in right))

results=[]
for index,rows in enumerate(prior.fixtures):
 kin=Kinematics(rows);dual=prior.parity_kinematics(kin)
 direct=vectors(kin,2);parity=vectors(dual,1,True)
 aa=contraction(direct,direct);bb=contraction(parity,parity);ab=contraction(direct,parity)
 norm=s.factor(aa+bb-2*ab)
 assert aa>0 and bb>0 and norm==0
 # Negative control: omit one NMHV term. The resulting norm must detect it.
 truncated=parity[1:]
 bad=s.factor(aa+contraction(truncated,truncated)-2*contraction(direct,truncated))
 expected=s.factor(parity[0][0]**2*parity[0][1].dot(parity[0][1])**4)
 assert bad==expected and bad>0
 results.append({'input_index':index,'twistors':rows,'single_flavor_dimension':35,'ordered_four_flavor_coordinates':35**4,'direct_squared_norm':str(aa),'parity_squared_norm':str(bb),'cross_inner_product':str(ab),'difference_squared_norm':str(norm),'omitted_term_negative_control_squared_norm':str(bad),'direct_terms':[{'weight':str(w),'vector':list(map(str,v))} for w,v in direct],'Fourier_transformed_parity_terms':[{'weight':str(w),'vector':list(map(str,v))} for w,v in parity]})
files=[Path(__file__),Path(prior.__file__),Path(prior.__file__).with_name('nine_point_source_r.py')]
report={'passed':True,'witness_count':len(results),'full_tensor_coordinates_per_witness':35**4,'method':'Exact rational positive-definite Euclidean Gram contraction, NOT a probabilistic projection or modular zero test','source_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in files},'witnesses':results,'scope':'Complete degree(4,4,4,4) eta tensor identity at each of two specified rational kinematics, with fixed flavor-grouped Fourier convention. Does not establish an all-kinematics rational identity.'}
(root/'results/seven-point-full-parity-tensor.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in ('witnesses','source_sha256')},indent=2))
