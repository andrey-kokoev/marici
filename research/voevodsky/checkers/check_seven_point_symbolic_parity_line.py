"""Full tensor parity identity over Q(t), restricted to a stated twistor curve."""
from pathlib import Path
import contextlib,io,itertools,json
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):import check_seven_point_parity as prior
from nine_point_source_r import Kinematics
root=Path(__file__).resolve().parents[1];t=s.symbols('t');parameters=[1,2,3,4,5,6,t]
kin=Kinematics([(1,x,x*x,x**3) for x in parameters]);dual=prior.parity_kinematics(kin)
choices=list(itertools.combinations(range(1,8),4));vectors=[];weights=[]
for parity,K,k in ((False,kin,2),(True,dual,1)):
 for M,f in prior.amplitude_terms(K,k):
  M=M.applyfunc(s.factor);vector=[]
  for subset in choices:
   columns=[i-1 for i in range(1,8) if i not in subset] if parity else [i-1 for i in subset]
   sign=(-1)**(sum(i-1 for i in subset)-6) if parity else 1
   vector.append(s.factor(sign*M[:,columns].det(method='domain-ge')))
  pivot=next(v for v in vector if v!=0)
  vectors.append(s.Matrix([s.factor(v/pivot) for v in vector]));weights.append(s.factor(f*pivot**4*(-1 if parity else 1)))
V=s.Matrix.hstack(*vectors);rows=[0,1,4]
# Find a regular3-column basis using t=7 solely for pivot selection.
_,columns=V.subs(t,7).rref();assert len(columns)==3
basis=V[:,list(columns)];pivot_det=s.factor(basis[rows,:].det());assert pivot_det!=0
coordinates=(basis[rows,:].inv()*V[rows,:]).applyfunc(s.factor)
embedding=(basis*coordinates-V).applyfunc(s.factor);assert embedding==s.zeros(35,12)
checks=[]
for indices in itertools.combinations_with_replacement(range(3),4):
 difference=s.factor(sum(weights[j]*s.prod(coordinates[i,j] for i in indices) for j in range(12)))
 assert difference==0,indices
 checks.append({'indices':indices,'difference':str(difference)})
report={'passed':True,'field':'Q(t)','twistors':[[str(v) for v in row] for row in [(1,x,x*x,x**3) for x in parameters]],'span_rank':3,'basis_columns':columns,'pivot_rows':rows,'basis_pivot_determinant':str(pivot_det),'full_embedding_entries_checked':35*12,'symmetric_quartic_identities':checks,'signed_weights':list(map(str,weights)),'coordinates':[[str(v) for v in row] for row in coordinates.tolist()],'scope':'Complete Grassmann tensor identity as rational functions on this one-parameter moment-curve family, wherever original denominators are regular. Not a generic seven-point all-kinematics identity; t=7 used only to select a basis, all final equalities proved over Q(t).'}
(root/'results/seven-point-symbolic-parity-line.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:report[k] for k in ('passed','field','span_rank','full_embedding_entries_checked','scope')},indent=2))
