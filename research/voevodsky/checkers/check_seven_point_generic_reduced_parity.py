"""Construct all generic Ward-reduced terms; quartics are a separate checker."""
from pathlib import Path
import contextlib,io,json,time,hashlib
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):import check_seven_point_parity as prior
from nine_point_source_r import Kinematics,EPS
root=Path(__file__).resolve().parents[1];out=root/'results/seven-point-generic-reduced-parity.json'
a,b,c,d,e,f=s.symbols('a b c d e f');symbols=(a,b,c,d,e,f)
external=[(1,t,t*t,t**3) for t in range(1,6)]+[(1,a,b,c),(1,d,e,f)]
start=time.monotonic();report={'passed':False,'field':'Q(a,b,c,d,e,f)','twistors':[[str(x) for x in row] for row in external],'stage':'initializing','terms':[],'identities':[]}
def save(stage):
 report['stage']=stage;report['elapsed_seconds']=round(time.monotonic()-start,3);out.write_text(json.dumps(report,indent=2)+'\n');print(stage,flush=True)
save('building direct kinematics')
kin=Kinematics(external)
kin.X={i:X.applyfunc(s.factor) for i,X in kin.X.items()}
save('building parity kinematics')
dual=prior.parity_kinematics(kin);dual.X={i:X.applyfunc(s.factor) for i,X in dual.X.items()}
L=s.Matrix.hstack(*(kin.lam[i] for i in range(1,8)));R=s.Matrix.hstack(*(dual.lam[i] for i in range(1,8)))
assert (L*R.T).applyfunc(s.factor)==s.zeros(2)
subsets=((1,2,3,4),(1,2,3,5),(1,2,4,5));weights=[];vectors=[]
for parity,K,k in ((False,kin,2),(True,dual,1)):
 for index,(M,weight) in enumerate(prior.amplitude_terms(K,k)):
  M=M.applyfunc(s.factor)
  # Direct rows lie in ker R and include L. Dual rows lie in ker L
  # and include R; Hodge dual therefore satisfies both original Ward laws.
  ward=M*(L.T if parity else R.T)
  assert ward.applyfunc(s.factor)==s.zeros(M.rows,2)
  v=[]
  for subset in subsets:
   columns=[i-1 for i in range(1,8) if i not in subset] if parity else [i-1 for i in subset]
   sign=(-1)**(sum(i-1 for i in subset)-6) if parity else 1
   v.append(s.factor(sign*M[:,columns].det(method='domain-ge')))
  pivot=next(x for x in v if x!=0);v=[s.factor(x/pivot) for x in v];w=s.factor(weight*pivot**4*(-1 if parity else 1))
  vectors.append(v);weights.append(w)
  report['terms'].append({'side':'parity' if parity else 'direct','index':index,'signed_weight':str(w),'pivot_vector':list(map(str,v)),'Ward_residual_zero':True})
  save('completed '+('parity' if parity else 'direct')+' term '+str(index))
assert len(report['terms'])==12
files=[Path(__file__),Path(prior.__file__),Path(prior.__file__).with_name('nine_point_source_r.py')]
report['source_sha256']={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
report['passed']=True
report['scope']='Construction only: six direct and six parity terms over the generic six-modulus chart, with termwise Ward constraints. All15 quartic parity identities must be verified separately by check_seven_point_generic_quartics.py.'
save('construction complete')
