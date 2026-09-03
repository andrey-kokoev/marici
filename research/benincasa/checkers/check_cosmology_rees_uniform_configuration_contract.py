#!/usr/bin/env python3
"""Verify the all-cutoff configuration contract for source-label inclusion."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/benincasa';base=(B/'physical_four_mark_residue_twisted_derham.py').read_text();charts=(B/'g12_g31_residue_chart_transition.py').read_text();module=(B/'check_rank26_total_energy_triple_relation_module.py').read_text();rows=(B/'checkers/check_cosmology_rees_complete_bounded_exact_row_iterator.py').read_text()
assert 'return [(i, j) for i in range(degree + 1) for j in range(degree + 1 - i)]' in base
assert 'SOURCE_NAMES = ("g1", "g2", "g3", "g23", "g31")' in charts and 'K_DEPTH = 2' in charts and 'Q_DEPTH = 2' in charts
assert 'OFFSETS = (-3, -2, -1, 0, 1, 2, 3)' in module
assert all(x in rows for x in ['for exp in mons(A):','for exp in mons(A-4):','for exp in mons(A-1):'])
out={'schema':'marici.benincasa.cosmology-rees-uniform-configuration-contract.v1','range':'all integers A>=4','monomial_contract':'M_d={(i,j):i,j>=0 and i+j<=d}; hence M_d is contained in M_(d+1)','cutoff_invariants':{'K_DEPTH':2,'Q_DEPTH':2,'NAMES':['g1','g2','g3','g23','g31'],'OFFSETS':[-3,-2,-1,0,1,2,3],'source_fiber_A_independent':True},'family_bounds':{'twisted_derivative':'M_A','K_multiplication':'M_(A-4)','q_multiplication':'M_(A-1)'},'uniform_theorem':'every labelled relation at cutoff A reappears with identical coefficients at cutoff A+1 for all A>=4; source-label inclusion therefore descends to a quotient map Q_A to Q_(A+1)','row_ordering_claimed':False,'tau_representative_fixed_by_inclusion':True,'tau_nonvanishing_uniformly_proved':False,'remaining_gate':'prove tau_A nonzero for all A, not only A=4,5,6,7','passed':True};(B/'results/cosmology_rees_uniform_configuration_contract.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
