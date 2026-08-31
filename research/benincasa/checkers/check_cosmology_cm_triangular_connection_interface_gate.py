#!/usr/bin/env python3
"""Test whether the reconstructed CM cyclic connection exposes a q0-to-e6 triangular block."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
rec=json.loads((R/'cm-cyclic-connection-reconstruction.json').read_text());cur=json.loads((R/'cm-cyclic-connection-curvature.json').read_text());hor=json.loads((R/'cm-cyclic-transverse-horizontality.json').read_text())
assert rec['status']==cur['status']==hor['status']=='pass'
coeff=rec['coefficients_by_direction'];assert len(coeff)==3 and all(len(v)==15 for v in coeff)
assert 'does not define a flat quotient connection' in cur['conclusion']
assert 'does not certify a marked-relative subconnection' in hor['scope_warning']
out={'schema':'marici.benincasa.cosmology-cm-triangular-connection-interface-gate.v1','available':{'three_direction_rational_scalar_reconstruction':True,'denominator':rec['denominator'],'validation_residuals_vanish':rec['checks']['all_validation_residuals_vanish'],'quadratic_quotient_horizontality':True},'missing':{'seven_dimensional_CM_basis_labels':True,'seven_by_seven_connection_matrices':True,'marked_q0_basis_vector':True,'e6_subspace_embedding':True,'q0_to_e6_off_diagonal_block':True,'source_normalized_triangular_gauge':True},'coefficient_shape':[len(coeff),len(coeff[0])],'promotion_allowed':False,'reason':'the 3 by 15 scalar reconstruction is not a matrix connection on the seven-dimensional CM cohomology and has no typed marked-relative basis','additional_obstruction':cur['conclusion'],'next_constructor':'serialize a source-labelled seven-element CM cohomology basis and reconstruct all three 7x7 Gauss-Manin matrices before asking for a triangular shear','passed':True};(R/'cosmology_cm_triangular_connection_interface_gate.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
