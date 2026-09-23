"""Berezin-extract a complete sourced four-mass component from the Y0 polynomial."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_four_mass_rank_six_Y0_regular_witness as witness
 import check_four_mass_complete_component_companion_trace as psi_checker
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
Z,D,variables=witness.Z,witness.D,witness.variables
# Exterior generators ordered p1..p4,q1..q4,eta1_1..eta1_4,eta5_1..eta5_4.
def product(A,B):
 out={}
 for ma,ca in A.items():
  for mb,cb in B.items():
   if ma&mb:continue
   swaps=sum((mb&((1<<i)-1)).bit_count() for i in range(16) if ma>>i&1)
   mask=ma|mb;out[mask]=out.get(mask,0)+(-1 if swaps%2 else 1)*ca*cb
 return {m:c for m,c in out.items() if c}
def linear(p,eta):return {(1<<(p+i))|(1<<(eta+i)):1 for i in range(4)}
px,qy,qx,py=linear(0,8),linear(4,12),linear(4,8),linear(0,12)
a=product(px,qy);b=product(qx,py)
for mask,value in b.items():a[mask]=a.get(mask,0)-value
k={m:c for m,c in a.items() if c};fourth={0:1}
for i in range(4):fourth=product(fourth,k)
assert len(fourth)==1 and (1<<16)-1 in fourth
berezin_constant=fourth[(1<<16)-1];assert berezin_constant==2880
# Independent small-N exterior calculations check the nontrivial
# (N+1)(N!)^2 factor rather than assuming a unit Berezin normalization.
def constant_for_N(n):
 def multiply(A,B):
  out={}
  for ma,ca in A.items():
   for mb,cb in B.items():
    if ma&mb:continue
    swaps=sum((mb&((1<<i)-1)).bit_count() for i in range(4*n) if ma>>i&1)
    mask=ma|mb;out[mask]=out.get(mask,0)+(-1 if swaps%2 else 1)*ca*cb
  return {m:c for m,c in out.items() if c}
 def term(p,eta):return {(1<<(p+i))|(1<<(eta+i)):1 for i in range(n)}
 first=multiply(term(0,2*n),term(n,3*n))
 second=multiply(term(n,2*n),term(0,3*n))
 for mask,value in second.items():first[mask]=first.get(mask,0)-value
 out={0:1}
 for _ in range(n):out=multiply(out,first)
 return out[(1<<(4*n))-1]
assert all(constant_for_N(n)==(-1)**n*(n+1)*s.factorial(n)**2 for n in range(1,5))
rows=[]
for row in json.loads((OUT/'nine-point-paired-two-sheet-trace.json').read_text())['rows']:
 initial=dict(zip(variables,[s.Rational(x) for x in row['weights']]+[s.Rational(row['t']),s.Rational(row['u'])]))
 C=D.subs(initial);Y=C*Z
 basis=Y.nullspace();right=Y.T*(Y*Y.T).inv()
 G=s.Matrix.hstack(*basis,*[right[:,j] for j in range(2)]);G[:,0]=G[:,0]/G.det()
 z=(Z*G)[:,0:4]
 components=[]
 for root,point in witness.fibre(C):
  Ci=D.subs(point);assert Ci*z==s.zeros(2,4)
  derivatives=[]
  for variable in variables:
   direction=D.diff(variable).subs(point)*z
   derivatives.append(s.Matrix([direction[i,j] for i in range(2) for j in range(4)]))
  Jz=s.Matrix.hstack(*derivatives).det(method='domain-ge');assert Jz!=0
  source=-s.S.One/(s.prod(point[x] for x in variables[:6])*point[variables[7]]*(point[variables[6]]-point[variables[7]]))
  delta=s.Matrix.hstack(Ci[:,0],Ci[:,4]).det()
  components.append(source/Jz*delta**4)
 extracted=s.factor(berezin_constant*sum(components))
 assert extracted!=0
 def br(i,j,k,l):return s.Matrix.vstack(z[i-1,:],z[j-1,:],z[k-1,:],z[l-1,:]).det(method='domain-ge')
 sourced,_=psi_checker.complete_component(br)
 assert sourced!=0
 rows.append({'initial_weights':row['weights'],'Berezin_extracted_component':str(extracted),
              'sourced_psi_component':str(sourced),'extracted_over_sourced_psi':str(s.factor(extracted/sourced))})
report={'schema':'marici.nima.four-mass-Y0-Berezin-component.v1','passed':True,
 'Grassmann_order':'phi1^1..4,phi2^1..4,eta1^1..4,eta5^1..4; coefficient of the top ordered monomial; no external Berezin normalization assumed',
 'det_Ch_fourth_power_top_fermion_coefficient':berezin_constant,
 'universal_small_N_check':'For N=1,2,3,4 the ordered exterior-algebra top coefficient is (-1)^N (N+1)(N!)^2, giving 2880 at N=4.',
 'witnesses':rows,'ratio_constant_across_two_targets':rows[0]['extracted_over_sourced_psi']==rows[1]['extracted_over_sourced_psi'],
 'scope':'Exact top-Grassmann-coefficient extraction and independently computed complete sourced psi component at two z datasets. Numerical orientation/normalization comparison does not establish a Y-dependent global form, source conventional Berezin measure unless separately audited, or nine-point generalized-R history.'}
(OUT/'four-mass-Y0-Berezin-component.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'Berezin_top_coefficient':berezin_constant,
 'two_ratios': [r['extracted_over_sourced_psi'] for r in rows]},indent=2))
