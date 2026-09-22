"""Fresh numerical replay plus separate exact merge/threshold/binding checks.
The numerical replay shares the producer; it is not an independent analytic proof.
"""
from pathlib import Path
from fractions import Fraction as Q
import json,hashlib,subprocess,sys
HERE=Path(__file__).resolve().parent;R=HERE.parent/'results';NR=HERE.parents[1]/'nima'/'results'
def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def bounds(z):return Q(z['lower']),Q(z['upper'])
bp=R/'directed-C-only-Abel-branch.json';rp=R/'directed-Abel-midpoint-replay.json';before=load(bp)
for p,h in before['bindings'].items():assert sha(Path(p))==h
subprocess.run([sys.executable,str(HERE/'certify_directed_C_tail_branch.py')],check=True,stdout=subprocess.DEVNULL)
b=load(bp);r=load(rp);assert b==before
assert sha(bp)==r['branch_sha256'];assert sha(R/'three-channel-source-task-calibration-directed-Abel.json')==r['calibration_sha256']
assert b['N']==1000000 and b['critical_box_count']==3
C=bounds(b['C']);e=b['finite_pairing_evidence']
parts=[bounds(z) for z in e['bulk_before_prime_tail']+b['tail_enclosures']+[e['endpoint'],e['h']]]
raw=(sum(z[0] for z in parts),sum(z[1] for z in parts));oldC=bounds(e['C'])
# Arb may outward-round the sum, so the stored intersection must enclose
# the intersection of exact component endpoint sums.
assert C[0]<=max(raw[0],oldC[0])<=min(raw[1],oldC[1])<=C[1]
old=load(R/'projection-resolution-conjecture-attack.json');theta=load(R/'theta-mass-refinement.json');H=bounds(old['h']);L=bounds(old['L']);X=[bounds(theta['windows'][w]['X']) for w in ('A1','B1')];mu=[bounds(theta['windows'][w]['mu']) for w in ('A1','B1')]
g=tuple(2*X[0][k]*X[1][k]*(C[k]+H[k]*(mu[0][k]-L[1-k]))*(C[k]+H[k]*(mu[1][k]-L[1-k])) for k in (0,1));assert g==bounds(r['gain'])
t=Q(load(NR/'signed-functional-dpc-contract.json')['threshold']);status='CERTIFIED_FEASIBLE' if g[0]>=t else 'CERTIFIED_INFEASIBLE' if g[1]<t else 'UNRESOLVED'
assert status==r['status']==r['task_result']['status']
print('PASS: fresh numerical replay, bindings, C intersection, exact theta merge and frozen threshold:',status)
