#!/usr/bin/env python3
"""Audit whether the known relative-residue cocycle can project to tau_p."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
B=ROOT/'research/benincasa/results';N=ROOT/'research/nima/results'
cech=json.loads((B/'cosmology_principal_wall_partial_fraction_cech_gate.json').read_text())
relative=json.loads((N/'cosmology_p_normal_relative_residue_cocycle.json').read_text())
M=cech['edge_to_vertex_matrix']; tau=cech['p_partial_fraction_pair_vector']; residue=relative['logarithmic_residue_vector']
def mv(x): return [sum(M[i][j]*x[j] for j in range(3)) for i in range(3)]
delta=[tau[i]-residue[i] for i in range(3)]
assert tau==[1,-1,-1] and residue==[1,-1,1]
assert delta==[0,0,-2]
assert mv(residue)==[0,0,0]
assert mv(tau)==[0,2,-2]
assert mv(delta)==[0,2,-2]
out={'schema':'marici.benincasa.cosmology-relative-residue-tau-p-chain-lift-audit.v1','problem':'can the source-derived relative residue cocycle be the residue projection of a total-complex lift of the affine tau_p cell?','bold_conjecture':'the known residue cocycle supplies the missing chain lift for tau_p','rivals':['the residue cocycle and tau_p have the same pair projection','they differ by a closed pair cell','they differ by a nonclosed pair cell requiring an additional source term'],'risky_consequences':'a chain lift identifying them must have equal pair projection, or a source-derived correction with zero vertex boundary','strongest_falsification_attempt':{'tau_p_pair_vector':tau,'relative_residue_pair_vector':residue,'projection_difference_tau_minus_residue':delta,'relative_residue_vertex_boundary':mv(residue),'tau_p_vertex_boundary':mv(tau),'difference_vertex_boundary':mv(delta)},'exact_residual':'tau_p minus the relative residue cocycle is (0,0,-2), whose vertex boundary is (0,2,-2); the discrepancy is not a closed pair cell','conjecture_disposition':'falsified for direct residue projection','surviving_scope':'the source-derived relative residue cocycle is closed at residue level but cannot directly be the pair projection of a tau_p total-complex lift','first_missing_typed_object':'a source-derived higher or lower total-complex component whose projected boundary cancels (0,2,-2) while retaining the tau_p affine coefficients','acceptance_test':'construct the component and verify the full total differential, its square, and projection to tau_p exactly','passed':True}
(B/'cosmology_relative_residue_tau_p_chain_lift_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
