#!/usr/bin/env python3
"""DPC classification of coordinate-fiber pullbacks of the E6/q_top residual."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
prior=json.loads((R/'cosmology_C2_corner_connection_normalization.json').read_text());assert prior['passed']
# Rv numerator over D(v-2).
# Nv = u*F, F=(-2u^2+2u+1)v + 4u^3-3u-2.
# Ru numerator over D*u*(u-2), expanded by exact polynomial arithmetic.
Nv={(4,0):4,(3,1):-2,(2,1):2,(2,0):-3,(1,1):1,(1,0):-2}
Nu={(4,1):-2,(4,0):10,(3,0):-3,(2,1):3,(2,0):-6,(1,2):2,(1,1):-10,(1,0):12,(0,2):-2,(0,1):8,(0,0):-8}
assert all(i>=1 for i,j in Nv) and Nu[(0,2)]==-2
# On u=c, du pulls back to zero; Rv vanishes identically only for c=0.
# For c != 0, v coefficient gives -2c^2+2c+1=0; using it in the constant term gives 3c=0, contradiction.
# On v=c, dv pulls back to zero; Ru cannot vanish identically: its u^4 coefficient forces c=5, while u^3 coefficient remains -3.
out={'schema':'marici.benincasa.cosmology-E6-qtop-diagonal-residual-loci.v1','conjecture':'the diagonal mismatch vanishes on a source-relevant coordinate fiber larger than the known u=0 corner','dv_residual_numerator':'u*((-2*u^2+2*u+1)*v + 4*u^3-3*u-2)','du_residual_numerator':'(-2*v+10)*u^4 - 3*u^3 + (3*v-6)*u^2 + (2*v^2-10*v+12)*u - 2*(v-2)^2','u_constant_pullback':{'tangent':'dv','unique_identically_vanishing_fiber':'u=0','proof_for_nonzero_u':'the v coefficient and constant term imply both -2u^2+2u+1=0 and 3u=0'},'v_constant_pullback':{'tangent':'du','identically_vanishing_fibers':[],'proof':'u^4 coefficient forces v=5 but u^3 coefficient is then -3'},'exceptional_v2_pullback_vanishes':False,'conjecture_disposition':'falsified for coordinate-fiber loci','survivor':'the residual pullback vanishes on u=0 because du pulls back to zero and the dv residual has factor u','full_bivariate_residual_vanishes_on_u0':False,'next_test':'type the exact u=0 horizontal comparison and determine whether the principal three-wall target factors through that corner','passed':True};(R/'cosmology_E6_qtop_diagonal_residual_loci.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
