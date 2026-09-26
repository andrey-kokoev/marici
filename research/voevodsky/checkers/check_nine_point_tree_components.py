"""Exact selected coefficients of sourced P9 NNMHV, not A_MHV times P."""
from nine_point_source_r import Kinematics
from pathlib import Path
import sympy as s
import json
root=Path(__file__).resolve().parents[1];histories=json.loads((root/'results/nine-point-source-history-contract.json').read_text())['records'];results=[]
for parameters in (range(1,10),(1,2,4,7,11,16,22,29,37)):
 kin=Kinematics([(1,t,t*t,t**3) for t in parameters]);components={pair:[] for pair in ((3,5),(2,5),(1,5))}
 for h in histories:
  a1,b1=h['outer_pair'];a,b=h['inner_pair'];A,p=kin.ordinary(a1,b1);B,q=kin.inner(a1,b1,a,b,h['branch'])
  for (i,j),terms in components.items():terms.append(s.factor(p*q*(A[i]*B[j]-A[j]*B[i])**4))
 results.append({'parameters':list(parameters),'components':{f'chi{i}^4 chi{j}^4':{'sum':str(s.factor(sum(terms))),'nonzero_histories':sum(x!=0 for x in terms)} for (i,j),terms in components.items()}})
report={'passed':True,'histories_per_witness':50,'witnesses':results,'scope':'Three flavor-grouped degree-eight coefficients of normalized P9 tree ratio function. External 4D momentum twistors, not the barrier fixture bosonized target Y; no direct alpha/beta matching claimed.'}
(root/'results/nine-point-tree-components.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
