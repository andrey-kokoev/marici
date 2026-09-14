#!/usr/bin/env python3
import json
from pathlib import Path
N=12;ROOT=Path(__file__).resolve().parents[3];P=ROOT/'research/aspect/contracts/optical-ring-carrier-chain-map.v1.json';c=json.loads(P.read_text())
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def ident(n):return [[int(i==j) for j in range(n)] for i in range(n)]
# Boundary columns e_j -> v_(j+1)-v_j.
d=[[0]*N for _ in range(N)]
for j in range(N):d[j][j]=-1;d[(j+1)%N][j]=1
F0=ident(N);F1=ident(N)
# h maps reduced generator v_j-v_0 to tree path e_0+...+e_(j-1).
h=[[0]*(N-1) for _ in range(N-1)]
for j in range(1,N):
 for k in range(j):h[k][j-1]=1
# Reduced basis B columns v_j-v_0, tree boundary D_T.
B=[[0]*(N-1) for _ in range(N)]
for j in range(1,N):B[0][j-1]=-1;B[j][j-1]=1
DT=[row[:N-1] for row in d]
cycle=[1]*N
checks={
 'source_named':c['source_package'].endswith('optical-pair-stiffness-flux-cell.v1.json'),
 'twelve_sites':N==12,
 'chain_map':mm(d,F1)==mm(F0,d),
 'tree_h_is_right_inverse':mm(DT,h)==B,
 'contraction_descends':mm(F1[:N-1],h)==h,
 'cycle_closed':all(sum(d[i][j]*cycle[j] for j in range(N))==0 for i in range(N)),
 'cycle_retained':c['carrier_contraction']['full_cycle_contraction'] is False and 'Wilson' in c['carrier_contraction']['obstruction'],
 'periodic_boundary_declared':'periodic' in c['source_chain']['boundary'],
 'physical_boundary_preserved':c['physical_readout']['calibration_authority'] is None,
 'synthetic_only':'no apparatus calibration' in c['claim_boundary']}
out={'schema':'marici.aspect.optical-ring-carrier-chain-map-check.v1','passed':all(checks.values()),'checks':checks,'chain_residual':'zero','contraction_descent':'yes_on_spanning_tree_reduced_complex','full_cycle_descent':'blocked_by_retained_H1_Wilson_generator','rh_implication':False}
R=ROOT/'research/aspect/results/optical_ring_carrier_chain_map.json';R.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
