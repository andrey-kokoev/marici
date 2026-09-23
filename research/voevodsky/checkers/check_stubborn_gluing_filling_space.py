"""Stubborn pairwise obstruction as an owning analytical filling-space gap."""
from pathlib import Path
from fractions import Fraction as Q
import subprocess
import sys
import json
import hashlib
ROOT=Path(__file__).resolve().parents[3]
G=ROOT/'research/grothendieck';OUT=ROOT/'research/voevodsky/results'
p=G/'results/ternary-tail-budget-dpc.json'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,x):p.write_text(json.dumps(x,indent=2)+'\n')
cp=OUT/'stubborn-gluing-filling-space-contract.json'
save(cp,{'packet_sha256':sha(p),
 'issue':'Exact pair restrictions and coherent overlaps can have no common source filling.',
 'source':'Owning three-bin moment relaxation, with atom and prefix budgets.',
 'boundary':'Three bin-pair restrictions with equal shared mass coordinates.',
 'filling':'One admitted mass triple satisfying all source budgets.',
 'candidate_repair':'Nonnegative slack witness for the total budget, joined before projection.',
 'prediction':'Pairwise-compatible boundaries have a global filling exactly when their forced total has nonnegative budget slack.',
 'scope':'This exact monotone three-bin constraint system; not arbitrary higher-order sources or prime-realizability.'})
subprocess.run([sys.executable,str(G/'checkers/verify_ternary_tail_budget_dpc.py')],check=True,capture_output=True,text=True)
d=json.loads(p.read_text());C=list(map(Q,d['atom_capacity_upper']));B=list(map(Q,d['prefix_budget_upper']))
lo=[Q(w['lower']) for w in d['weights']];hi=[Q(w['upper']) for w in d['weights']]
assert 0<=B[0]<=B[1]<=B[2]
def admitted(z):return all(0<=z[i]<=C[i] for i in range(3)) and all(sum(z[:i+1])<=B[i] for i in range(3))
def pair_admitted(z,omit):return admitted(tuple(Q(0) if i==omit else z[i] for i in range(3)))
z=(B[1]/2,B[1]/2,B[2]-B[1]/2)
assert all(pair_admitted(z,k) for k in range(3))
assert not admitted(z)
slack=B[2]-sum(z)
assert slack==-B[1]/2<0
# Exact criterion: all non-total source inequalities occur in some pair lift;
# adjoining total slack restores the one missing inequality.
# Check coefficient coverage explicitly (inequalities a.x<=rhs, x>=0).
source_rows=[((1,0,0),C[0]),((0,1,0),C[1]),((0,0,1),C[2]),
             ((1,0,0),B[0]),((1,1,0),B[1]),((1,1,1),B[2])]
pair_rows=[]
for omit in range(3):
 for coeff,rhs in source_rows:
  pair_rows.append((tuple(0 if i==omit else v for i,v in enumerate(coeff)),rhs))
assert all(row in pair_rows for row in source_rows[:-1])
# Pair projections are entailed by source nonnegativity: deleting positive
# coefficients only decreases left side. Thus pair constraints + total = source.
assert all(v>=0 for coeff,_ in source_rows for v in coeff)
# Reverse-oriented residual: solve the SAME equation for any coordinate.
reverse_checks=0
for i in range(3):
 residual=B[2]-sum(z[j] for j in range(3) if j!=i)
 assert residual-z[i]==slack
 reverse_checks+=1
# The slack certificate also expresses a cross-cut lift: s=x1+x2, r=B3-s.
s=z[0]+z[1]; remaining=B[2]-s
assert z[2]-remaining==-slack
# Bind objective relevance to owning exact packet quantities.
gap=Q(d['robust_gap_lower'])
assert gap>0
report={'passed':True,'contract_sha256':sha(cp),
 'local_fillings_exist':True,'global_filling_exists_for_candidate':False,
 'forced_mass_triple':[str(x) for x in z],
 'missing_global_witness':'lambda>=0 with x1+x2+x3+lambda=B3',
 'forced_lambda':str(slack),
 'exact_obstruction':'lambda=-B2/2<0',
 'boundary_completion_theorem':'Pairwise-compatible nonnegative masses admit a source filling iff total slack is nonnegative. This follows by exact source-row coverage plus the missing total-budget row.',
 'all_coordinate_orientation_checks':reverse_checks,
 'owning_objective_gap_lower':str(gap),
 'interpretation':'The filling space is empty above the locally compatible candidate. The obstruction is an omitted source constraint, not a disagreement between overlap maps. Adding the shared slack relation characterizes its exact image.',
 'scope':'The slack is a uniquely determined real witness when it exists; retaining its equation is additional higher-arity source information, not a new source acquisition or a proof that pair marginals imply the budget.'}
save(OUT/'stubborn-gluing-filling-space.json',report)
print(json.dumps({k:v for k,v in report.items() if k not in ('forced_mass_triple','owning_objective_gap_lower','forced_lambda')},indent=2))
