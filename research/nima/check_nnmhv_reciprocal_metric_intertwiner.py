#!/usr/bin/env python3
"""Test diagonal metric-adjoint pairing of 2->3 and 3->2 endpoint kernels."""
import json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];src=json.loads((ROOT/'research/nima/results/nnmhv-history-kernel-operator.json').read_text())
A=src['operators']['2_to_3']['matrix_float'];B=src['operators']['3_to_2']['matrix_float'];m=len(A)
# Endpoint reversal J turns the transpose back to the same triangular orientation.
R=[[A[m-1-j][m-1-i] for j in range(m)] for i in range(m)]
diag_ratios=[B[i][i]/R[i][i] for i in range(m)]
# B=c W^{-1} R W forces every diagonal ratio to equal the same c.
diag_spread=max(diag_ratios)-min(diag_ratios);relative=diag_spread/max(abs(v) for v in diag_ratios)
# Raw transpose also has the opposite triangular support.
rawT=[[A[j][i] for j in range(m)] for i in range(m)];support_mismatch=sum((rawT[i][j]!=0)!=(B[i][j]!=0) for i in range(m) for j in range(m))
checks={'raw_transpose_has_support_mismatch':support_mismatch>0,'reversal_aligns_triangular_support':all((R[i][j]!=0)==(B[i][j]!=0) for i in range(m) for j in range(m)),'no_scalar_diagonal_metric_intertwiner':relative>1e-12}
out={'schema':'marici.nima.nnmhv-reciprocal-metric-intertwiner.v1','candidate':'K_3to2 = c W^{-1} J K_2to3^T J W with positive diagonal W','raw_transpose_support_mismatches':support_mismatch,'reversed_diagonal_ratios':diag_ratios,'relative_diagonal_ratio_spread':relative,'checks':checks,'passed':all(checks.values()),'conclusion':'Endpoint reversal repairs support orientation, but unequal diagonal ratios rule out every scalar-times-diagonal metric W. Any reciprocal pairing must be non-diagonal or use additional wall/tail channels.'}
p=ROOT/'research/nima/results/nnmhv-reciprocal-metric-intertwiner.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
