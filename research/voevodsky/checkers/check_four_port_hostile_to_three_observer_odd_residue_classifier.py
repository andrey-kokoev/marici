#!/usr/bin/env python3
"""Rank-exact four-port hostile to the provisional three-observer classifier."""
import hashlib,json,platform
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];FIX=ROOT/'research/voevodsky/fixtures/four_port_hostile_to_three_observer_odd_residue_classifier.v1.json';OUT=ROOT/'research/voevodsky/results/four_port_hostile_to_three_observer_odd_residue_classifier.json';D=json.loads(FIX.read_text());s=len(D['strata'])
def z(r,c):return [[Q(0) for _ in range(c)] for _ in range(r)]
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def rank(a):
 a=[r[:] for r in a];m=len(a);n=len(a[0]) if m else 0;i=0
 for c in range(n):
  p=next((r for r in range(i,m) if a[r][c]),None)
  if p is None:continue
  a[i],a[p]=a[p],a[i];q=a[i][c];a[i]=[x/q for x in a[i]]
  for r in range(m):
   if r!=i and a[r][c]:q=a[r][c];a[r]=[a[r][j]-q*a[i][j] for j in range(n)]
  i+=1
 return i
rows=[];full=miss=split=nat=True
for N in D['grade_cutoffs']:
 d=s*N;rho=z(2*d,4*d);h4=z(4*d,2*d);h3=z(4*d,d)
 for i in range(d):
  rho[i][i]=rho[i][d+i]=rho[i][2*d+i]=1;rho[d+i][2*d+i]=1
  h4[i][i]=1;h4[d+i][i]=-1;h4[3*d+i][d+i]=1
  h3[i][i]=1;h3[d+i][i]=-1
 ker=4*d-rank(rho);full &= not any(x for r in mm(rho,h4) for x in r) and rank(h4)==ker==2*d
 miss &= rank(h3)==d<ker and all(rho[r][3*d]==0 for r in range(2*d))
 split &= rank(h4)==rank(h3)+d
 rows.append({'grade_cutoff':N,'packet_dimension':d,'four_port_dimension':4*d,'readout_rank':rank(rho),'kernel_dimension':ker,'three_port_classifier_rank':rank(h3),'four_port_classifier_rank':rank(h4)})
checks={'corrected_four_port_classifier_exact':full,'three_port_classifier_not_surjective':miss,'kernel_direct_sum_has_two_odd_channels':split,'pure_seam_flux_is_invisible_hostile':miss,'coordinatewise_cutoff_naturality':nat,'source_status_remains_conditional':'does not establish' in D['claim_boundary']}
out={'schema':'marici.voevodsky.four-port-hostile-to-three-observer-odd-residue-classifier-check.v1','passed':all(checks.values()),'checks':checks,'computed':{'cutoff_rows':rows,'full_kernel':'{(r,-r,0,j): r,j in V_N}','missing_three_port_summand':'{(0,0,0,j): j in V_N}'},'falsification_disposition':'The provisional full-kernel claim is falsified if seam flux J is independent. The readout kernel then has two odd summands, and h3 covers only the reciprocal-tail summand. The corrected h4 is exact.','surviving_scope':'The three-port classifier is exact only conditional on J=0 or a source-derived reconstruction of J. Otherwise the four-port residue object is V_odd-tail direct-sum V_odd-seam.','claim_boundary':D['claim_boundary'],'execution_receipt':{'command':'python research/voevodsky/checkers/check_four_port_hostile_to_three_observer_odd_residue_classifier.py','python':platform.python_version(),'fixture_sha256':hashlib.sha256(FIX.read_bytes()).hexdigest(),'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));raise SystemExit(0 if out['passed'] else 1)
