"""Apply the universal Ward basis, rather than an empirical amplitude span."""
from pathlib import Path
import itertools,json
import sympy as s
from nine_point_source_r import Kinematics,EPS
root=Path(__file__).resolve().parents[1]
source=json.loads((root/'results/seven-point-full-parity-tensor.json').read_text())
choices=list(itertools.combinations(range(7),4));pivots=[0,1,4];reports=[]
for witness in source['witnesses']:
 kin=Kinematics(witness['twistors']);L=s.Matrix.hstack(*(kin.lam[i] for i in range(1,8)));L=L[:,:2].inv()*L
 tilde=[]
 for i in range(1,8):
  D=kin.X[i]-kin.X[i%7+1];bra=kin.lam[i].T*EPS;j=next(j for j in range(2) if bra[j]);tilde.append(D[:,j]/bra[j])
 R=s.Matrix.hstack(*tilde);R=R[:,5:7].inv()*R;assert L*R.T==s.zeros(2)
 U=s.zeros(3,7)
 for i in range(3):U[i,i+2]=1;U[i,5]=-R[0,i+2];U[i,6]=-R[1,i+2]
 B=s.Matrix.hstack(*(s.Matrix([L.col_join(U[[i,j],:])[:,list(subset)].det() for subset in choices]) for i,j in itertools.combinations(range(3),2)))
 assert B[pivots,:]==s.eye(3)
 terms=witness['direct_terms']+witness['Fourier_transformed_parity_terms']
 V=s.Matrix.hstack(*(s.Matrix(list(map(s.Rational,t['vector']))) for t in terms));coordinates=V[pivots,:]
 assert B*coordinates==V
 weights=[s.Rational(t['weight'])*(1 if j<6 else -1) for j,t in enumerate(terms)]
 for indices in itertools.combinations_with_replacement(range(3),4):
  assert sum(weights[j]*s.prod(coordinates[i,j] for i in indices) for j in range(12))==0
 reports.append({'input_index':witness['input_index'],'full_embedding_entries':420,'reduced_quartic_identities':15})
report={'passed':True,'witnesses':reports,'scope':'At saved exact inputs, all12 amplitude vectors satisfy the universal kinematics-only Ward embedding, and parity follows from15 pivot quartics. No amplitude-dependent basis selection. Universal generic Ward basis proved separately; generic amplitude Ward membership and15 bosonic identities still require proof.'}
(root/'results/seven-point-ward-reduced-parity.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
