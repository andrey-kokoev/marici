"""Two-coordinate witnessed cut presentation of the owning ternary tail carrier.

Each adjacent cut relation retains the bin mass x as witness. The source is
its certified moment relaxation, not exact prime-realizable measures.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
import subprocess
import sys
import json
import hashlib
ROOT = Path(__file__).resolve().parents[3]
G = ROOT / 'research/grothendieck'
OUT = ROOT / 'research/voevodsky/results'
p = G / 'results/ternary-tail-budget-dpc.json'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p, x): p.write_text(json.dumps(x, indent=2) + '\n')
cp = OUT / 'analytic-cut-compatibility-contract.json'
save(cp, {'source_packet_sha256':sha(p),
 'source':'Owning three-bin rational moment relaxation with caps ci, prefix budgets Bi and fixed lower coefficients li.',
 'boundary':'Two exact real/rational coordinates (s,t): cumulative mass and lower-functional value; (s0,t0)=(0,0).',
 'local_relation':'Ri((s,t),(v,w);x) iff 0<=x<=ci, v=s+x, w=t+li*x, v<=Bi.',
 'prediction':'Source triples correspond bijectively to joined witnessed adjacent relations; every regrouping has the same witness triples and objective, and reversal exchanges relation arguments.',
 'bound':'Two scalar coordinates per cut and one bin-mass witness per segment, independent of numerical precision. Finite-dimensional, not finite-state or claimed minimal.',
 'scope':'Static compatibility equations. No interpretation as reverse physical execution.'})
subprocess.run([sys.executable,str(G/'checkers/verify_ternary_tail_budget_dpc.py')],check=True,capture_output=True,text=True)
d=json.loads(p.read_text()); caps=list(map(Q,d['atom_capacity_upper'])); budgets=list(map(Q,d['prefix_budget_upper'])); weights=[Q(v['lower']) for v in d['weights']]
def admitted(xs):
 return all(0<=x<=c for x,c in zip(xs,caps)) and all(sum(xs[:i+1])<=budgets[i] for i in range(3))
def R(i,a,b,x):
 return 0<=x<=caps[i] and b[0]==a[0]+x and b[1]==a[1]+weights[i]*x and b[0]<=budgets[i]
def boundaries(xs):
 z=[(Q(0),Q(0))]
 for i,x in enumerate(xs):z.append((z[-1][0]+x,z[-1][1]+weights[i]*x))
 return z
# Polynomial identity certificates for ALL real triples: represent affine forms
# as four rational coefficients (constant,x1,x2,x3), independent of sampling.
zero=(Q(0),)*4
mass=[zero]; value=[zero]
for i in range(3):
 e=tuple(Q(int(j==i+1)) for j in range(4))
 mass.append(tuple(a+b for a,b in zip(mass[-1],e)))
 value.append(tuple(a+weights[i]*b for a,b in zip(value[-1],e)))
 assert tuple(b-a for a,b in zip(mass[i],mass[i+1]))==e
 assert tuple(b-a for a,b in zip(value[i],value[i+1]))==tuple(weights[i]*v for v in e)
for a in range(4):
 for b in range(a,4):
  for c in range(b,4):
   for forms in (mass,value):
    assert tuple(forms[b][j]-forms[a][j]+forms[c][j]-forms[b][j] for j in range(4))==tuple(forms[c][j]-forms[a][j] for j in range(4))
# Exact regressions with boundary and interior values, including the frozen
# pairwise-impossible completion. Continuum proof is by identities above.
choices=[sorted({Q(0),c/2,c,budgets[i]/2,budgets[i]}) for i,c in enumerate(caps)]
candidates=set(product(*choices))
bad=(budgets[1]/2,budgets[1]/2,budgets[2]-budgets[1]/2)
candidates.add(bad)
checks=valid=0
for xs in candidates:
 z=boundaries(xs)
 joint=all(R(i,z[i],z[i+1],xs[i]) for i in range(3))
 assert joint==admitted(xs)
 valid+=joint
 # A proposed joined path reconstructs each witness from boundary mass difference.
 assert tuple(z[i+1][0]-z[i][0] for i in range(3))==xs
 assert z[3][1]==sum(w*x for w,x in zip(weights,xs))
 # Same relation under swapped orientation, retaining its original index.
 rev=list(reversed(z))
 assert joint==all(R(2-j,rev[j+1],rev[j],xs[2-j]) for j in range(3))
 checks+=1
assert not admitted(bad)
z=boundaries(bad)
assert R(0,z[0],z[1],bad[0]) and R(1,z[1],z[2],bad[1])
assert not R(2,z[2],z[3],bad[2])
# Pairwise admission confirmed directly by actual full carrier zero lifts.
assert all(admitted(tuple(Q(0) if i==missing else x for i,x in enumerate(bad))) for missing in range(3))
assert sha(p)==json.loads(cp.read_text())['source_packet_sha256']
report={'passed':True,'contract_sha256':sha(cp),'scalar_coordinates_per_cut':2,
 'exact_regression_triples':checks,'admitted_regression_triples':valid,
 'affine_mass_forms':[[str(v) for v in row] for row in mass],
 'affine_objective_forms':[[str(v) for v in row] for row in value],
 'pairwise_obstruction_rejected_by_third_segment':True,
 'continuum_certificate':'Adjacent equalities telescope to source cumulative sums and objective. Each local inequality is exactly one atom cap or prefix budget. Conversely any admitted source triple defines unique marked boundaries. This is a witness-preserving bijection, valid over the reals.',
 'composition':'Regrouping is reassociation of conjunction and existential quantification over shared boundaries; retaining segment witnesses preserves exactly the same source triples.',
 'orientation':'Transpose each indexed relation and reverse their order; the same equalities and source witnesses remain.',
 'scope':'Two-field sufficient presentation for the fixed rational lower functional on the actual three-bin relaxation. No minimality claim, fixed-hat exact moment optimization, prime-realizability, or finite-state bound.'}
save(OUT/'analytic-cut-compatibility.json',report)
print(json.dumps({k:v for k,v in report.items() if not k.endswith('_forms')},indent=2))
