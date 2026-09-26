"""Seven-point gluon amplitudes: NNMHV recursion versus parity NMHV."""
from pathlib import Path
import itertools,json,random
import sympy as s
from nine_point_source_r import Kinematics,EPS

def histories(n):
 for a in range(2,n):
  for b in range(a+2,n):
   for c in range(a+1,b+1):
    for d in range(c+2,b+1):yield a,b,c,d,'left-nested'
   for c in range(b,n):
    for d in range(c+2,n):yield a,b,c,d,'right-nested'

def angle(kin,i,j):return s.det(s.Matrix.hstack(kin.lam[i],kin.lam[j]))
def eta_row(kin,row):
 # chi_i = <theta_i lambda_i>, theta_i=sum_{j<i} lambda_j eta_j.
 return s.Matrix([[sum(row[i]*angle(kin,j,i) for i in range(j+1,kin.n+1)) for j in range(1,kin.n+1)]])
def amplitude_terms(kin,k):
 base=s.Matrix.hstack(*(kin.lam[i] for i in range(1,kin.n+1)))
 pt=s.prod(angle(kin,i,i%kin.n+1) for i in range(1,kin.n+1))
 if k==1:
  for a in range(2,kin.n):
   for b in range(a+2,kin.n):
    R,f=kin.ordinary(a,b);yield base.col_join(eta_row(kin,R)),f/pt
 else:
  for a,b,c,d,branch in histories(kin.n):
   R,f=kin.ordinary(a,b);S,g=kin.inner(a,b,c,d,branch)
   yield base.col_join(eta_row(kin,R)).col_join(eta_row(kin,S)),f*g/pt

def parity_kinematics(kin):
 tilde={}
 for i in range(1,kin.n+1):
  difference=(kin.X[i]-kin.X[i%kin.n+1]).applyfunc(s.factor);bra=kin.lam[i].T*EPS
  j=next(j for j in range(2) if bra[j]!=0);tilde[i]=difference[:,j]/bra[j]
  assert (difference-tilde[i]*bra).applyfunc(s.factor)==s.zeros(2)
 assert sum((kin.lam[i]*tilde[i].T for i in tilde),s.zeros(2)).applyfunc(s.factor)==s.zeros(2)
 X=s.zeros(2);rows=[]
 for i in range(1,kin.n+1):
  mu=X*tilde[i];rows.append(list(tilde[i])+list(mu))
  X=(X-kin.lam[i]*tilde[i].T*EPS).applyfunc(s.factor)
 assert X==s.zeros(2)
 return Kinematics(rows)

rng=random.Random(707)
fixtures=[[(1,t,t*t,t**3) for t in range(1,8)],[tuple(rng.randint(-20,20) for _ in range(4)) for i in range(7)]]
reports=[];mixed_checks=0
assert len(list(histories(7)))==6
for rows in fixtures:
 kin=Kinematics(rows);dual=parity_kinematics(kin)
 direct=list(amplitude_terms(kin,2));parity=list(amplitude_terms(dual,1));assert len(direct)==len(parity)==6
 components=[]
 for negative in itertools.combinations(range(1,8),4):
  complement=[i for i in range(1,8) if i not in negative]
  left=s.factor(sum(f*M[:,[i-1 for i in negative]].det()**4 for M,f in direct))
  right=s.factor(sum(f*M[:,[i-1 for i in complement]].det()**4 for M,f in parity))
  assert s.factor(left-right)==0,(negative,left,right)
  components.append({'negative_helicity_labels':negative,'amplitude':str(left)})
 # Fourier/Hodge complement signs matter for mixed supermultiplet states.
 choices=list(itertools.combinations(range(1,8),4));mixed=[]
 for trial in range(64):
  subsets=[rng.choice(choices) for _ in range(4)]
  complements=[[i for i in range(1,8) if i not in subset] for subset in subsets]
  sign=(-1)**sum(sum(i-1 for i in subset)-6 for subset in subsets)
  left=s.factor(sum(f*s.prod(M[:,[i-1 for i in subset]].det() for subset in subsets) for M,f in direct))
  right=s.factor(sign*sum(f*s.prod(M[:,[i-1 for i in subset]].det() for subset in complements) for M,f in parity))
  assert s.factor(left-right)==0,('mixed',subsets,sign,left,right)
  mixed_checks+=1;mixed.append({'flavor_label_subsets':subsets,'Fourier_sign':sign,'coefficient':str(left)})
 reports.append({'twistors':rows,'components':components,'mixed_components':mixed})
report={'passed':True,'NNMHV_histories':6,'NMHV_histories':6,'gluon_parity_checks':70,'mixed_Fourier_checks':mixed_checks,'witnesses':reports,'scope':'All35 four-negative-helicity gluon components at two rational kinematics. Momentum delta removed; MHV Parke-Taylor prefactors retained. Parity computed via swapped spinors and complementary helicities. Also64 mixed flavor subsets per input with explicit Hodge-complement Fourier signs. Not exhaustive supermultiplet comparison or a symbolic all-kinematics proof.'}
path=Path(__file__).resolve().parents[1]/'results/seven-point-parity.json';path.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items() if k!='witnesses'},indent=2))
