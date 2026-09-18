#!/usr/bin/env python3
"""Möbius/zeta reduction of the triangular NNMHV history kernel."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];src=json.loads((ROOT/'research/nima/results/nnmhv-history-kernel-operator.json').read_text());K=src['operators']['2_to_3']['matrix_float'];m=len(K)
# Rectangular zeta transform after zero extension outside b2<=b1.
F=[[sum(K[r][c] for r in range(i+1) for c in range(j+1)) for j in range(m)] for i in range(m)]
def at(A,i,j):return 0.0 if i<0 or j<0 else A[i][j]
M=[[at(F,i,j)-at(F,i-1,j)-at(F,i,j-1)+at(F,i-1,j-1) for j in range(m)] for i in range(m)]
maxerr=max(abs(M[i][j]-K[i][j]) for i in range(m) for j in range(m));shells=[F[i][i]-(F[i-1][i-1] if i else 0.0) for i in range(m)];row_shells=[sum(K[i][j] for j in range(i+1)) for i in range(m)];total=sum(sum(row) for row in K)
checks={'mixed_difference_recovers_kernel':maxerr<1e-18,'diagonal_shell_equals_new_history_row':max(abs(a-b) for a,b in zip(shells,row_shells))<1e-18,'full_sum_is_diagonal_telescoping_flux':abs(sum(shells)-total)<1e-18,'terminal_zeta_value_is_scalar_sum':abs(F[-1][-1]-total)<1e-18}
out={'schema':'marici.nima.nnmhv-interval-poset-mobius.v1','n':src['n'],'zeta_terminal':F[-1][-1],'scalar_sum':total,'diagonal_shell_increments':shells,'mobius_reconstruction_max_error':maxerr,'checks':checks,'passed':all(checks.values()),'interpretation':'Resolution is the zeta transform; mixed finite difference is Möbius inversion; augmentation telescopes through diagonal shells to the terminal cumulative value.'}
p=ROOT/'research/nima/results/nnmhv-interval-poset-mobius.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
