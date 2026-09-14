#!/usr/bin/env python3
"""Audit whether the mixed logarithmic column currently has a physical Betti realization."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[3]
one=json.loads((R/'research/benincasa/one-wall-universal-cleared-certificate.json').read_text())
gate=json.loads((R/'research/benincasa/relative-stokes-pairing-gate.json').read_text())
census=json.loads((R/'research/voevodsky/results/noncorner_logarithmic_valg_channel.json').read_text())
checks={
 'candidate_is_Theta101':census['candidate_v_alg_observable'].startswith('Theta101'),
 'Theta101_has_global_meromorphic_primitive':one['certificate']['verified_remaining_terms']==0,
 'Theta101_classified_in_algebraic_kernel':one['classification']['home']=='existing one-wall relative boundary into algebraic kernel',
 'correct_pairing_is_Leray_tube':gate['conclusion']['pairing_home']=='logarithmic residue/Leray-tube duality',
 'naive_contraction_does_not_descend':gate['naive_contraction_falsifier']['contraction_descends_to_relative_class'] is False,
 'moving_wall_pullback_invalid':gate['scope_correction']['direct_exceptional_pullback_is_valid'] is False,
 'GM_pairing_still_missing':'compute the residue-compatible Gauss-Manin connection' in gate['remaining'],
}
assert all(checks.values()),checks
out={
 'schema':'marici.voevodsky.mixed-log-physical-Betti-realization-audit.v1',
 'requested_candidate':'Theta101 (Theta110 by exchange)',
 'resolution':'--',
 'reason':'The algebraic v0 coordinate is represented by a one-wall form with an exact meromorphic primitive and is explicitly housed in the algebraic kernel. A physical scalar cannot be obtained by coordinate contraction: that contraction fails gauge descent. The valid realization must instead use residue/Leray-tube duality for the moving walls, but its residue-compatible, orientation-twisted Gauss-Manin connection has not been computed.',
 'do_not_claim':'Theta101 itself is a nonzero physical period merely because its marked-extension coordinate on v0 is one.',
 'available_data':{
   'primitive':'eta from one-wall-universal-cleared-certificate.json',
   'duality':'integral_T(gamma) Omega = 2*pi*i integral_gamma Res_W(Omega)',
   'central_primitives':gate['central_fiber_complement_primitives'],
 },
 'missing_interface':'moving-wall residue-compatible Gauss-Manin connection plus source-oriented relative cycle',
 'next_executable_action':'Construct the moving-wall residue totalization and connection first; only then pair its horizontal class with the source Leray tube.',
 'correction_to_VA2_interpretation':'VA2 established primitive algebraic rank-two tomography only. It did not establish a physical logarithmic observable.',
 'checks':checks,'passed':True}
dest=R/'research/voevodsky/results/mixed_log_physical_Betti_realization_audit.json';dest.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'resolution':out['resolution'],'missing':out['missing_interface']}))
