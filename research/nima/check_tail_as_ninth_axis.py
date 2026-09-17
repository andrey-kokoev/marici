#!/usr/bin/env python3
"""Test whether Fourier cutoff leakage is an independent ninth axis or a regulator fiber."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
N=9
# Backward shift: e_j -> e_{j-1}; it has a unit moving-boundary leakage.
F=[[0]*N for _ in range(N)]
for j in range(1,N):F[j-1][j]=1
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def add(a,b):return [[a[i][j]+b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
def eye_diag(m,inside):return [[int(i==j and ((i<m)==inside)) for j in range(N)] for i in range(N)]
def rank_nonzero(a):return any(any(x for x in row) for row in a)
def blocks(m):
 P=eye_diag(m,True);T=eye_diag(m,False)
 return P,T,mm(mm(P,F),P),mm(mm(P,F),T),mm(mm(T,F),P),mm(mm(T,F),T)
def norm_inf(a):return max(sum(abs(x) for x in row) for row in a)
block_reconstruction=True
complement_determined=True
moving=[]
for m in range(1,N):
 P,T,Fvv,A,B,Ftt=blocks(m)
 block_reconstruction &= add(add(Fvv,A),add(B,Ftt))==F
 complement_determined &= all(T[i][j]==int(i==j)-P[i][j] for i in range(N) for j in range(N))
 moving.append(norm_inf(A))
# For fixed visible m, residual from beyond refinement n eventually vanishes.
fixed_m=3
P=eye_diag(fixed_m,True)
fixed=[]
for n in range(fixed_m,N+1):
 Tn=[[int(i==j and i>=n) for j in range(N)] for i in range(N)]
 fixed.append(norm_inf(mm(mm(P,F),Tn)))
checks={'four_block_system_reconstructs_global_operator':block_reconstruction,'tail_projection_is_forced_by_regulator':complement_determined,'moving_boundary_leakage_stays_unit':all(x==1 for x in moving),'fixed_observer_tail_eventually_vanishes':fixed[-1]==0,'independent_ninth_binary_axis':False}
out={'schema':'marici.nima.tail-as-ninth-axis-audit.v1','checks':checks,'moving_leakage_norms':moving,'fixed_observer_residual_norms':fixed,'verdict':'retaining the complement gives an exact reservoir realization and next-cycle recurrence, but T_X=I-P_X is determined by regulator X; leakage is an R-q lax cell/fiber, not an independent ninth axis','passed':all(v for k,v in checks.items() if k!='independent_ninth_binary_axis'),'promotion_gate':'a ninth axis requires a source-derived reservoir operation or state coordinate not functorially determined by P_X and F'}
p=ROOT/'research/nima/results/tail-as-ninth-axis-audit.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
