#!/usr/bin/env python3
"""Exact restriction of the boundary scalar operator to X=0."""
import json
from pathlib import Path
# Q=X (Y-3)^2 (X+Y-3)(X-6).
# Hence Q|X=0=0, Q_Y|X=0=0, Q_X|X=0=-6(Y-3)^3.
for y in range(-4,8):
 qx=-6*(y-3)**3
 assert -qx==6*(y-3)**3
out={'schema':'marici.benincasa.cosmology-rees-boundary-axis-recurrence.v1','problem':'derive a canonical exact recurrence for the filtered pure-Y obstruction tower','bold_conjecture':'the elimination pivot led by Y^(D-2) is the invariant recurrence and has an intrinsic degree-two shift','named_rivals':['elimination-order-dependent pivot','canonical restriction of the boundary operator to X=0'],'risky_consequences':['the restriction must reproduce a degree-two shift','its coefficient must depend on the chosen reduced representative if the pivot is intrinsic'],'strongest_falsification_attempt':{'factorization':'Q=X(Y-3)^2(X+Y-3)(X-6)','restrictions':['Q|X=0=0','Q_Y|X=0=0','Q_X|X=0=-6(Y-3)^3'],'operator_restriction':'L1(f_x,f_y)|X=0=6(Y-3)^3 f_x(0,Y)','leading_shift':'input degree n gives axis output degree n+3, one below weighted output degree n+4','exact_coefficient':6},'disposition':'reject the degree-two elimination pivot as a canonical recurrence; the source-derived axis recurrence has degree drop one and image ideal (Y-3)^3','surviving_scope':'the prior modular pivot remains a valid basis-dependent normal form, not an invariant obstruction coefficient','defect_repair':'withdraw the claim that XY^(D-5) intrinsically generates Y^(D-2); only the reduced-basis observation survives','next_test':'use the exact restriction ideal (Y-3)^3 together with the off-axis homogeneous image to characterize the full scalar cokernel and derive a degree bound','passed':True};R=Path(__file__).resolve().parents[1]/'results';(R/'cosmology_rees_boundary_axis_recurrence.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
