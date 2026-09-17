#!/usr/bin/env python3
"""Record the exact contract needed for refinement to descend through observer radicals."""
import json
from pathlib import Path
out={
 'schema':'marici.nima.qRB-radical-descent-contract.v1',
 'condition':'R_XY(Rad_X) subseteq Rad_Y',
 'equivalent_test':'for every admitted observer omega_Y, omega_Y composed with R_XY is an admitted observer at X',
 'finite_status':'verified as a direct linear-algebra implication when the observer family is explicitly stacked',
 'infinite_status':'open',
 'not_inferred_from':['carrier positivity','trace-class cross-readout','projective endpoint continuity'],
 'next_input':'an explicit source-labelled pullback action on Gaussian translates and endpoint functionals',
 'rh_proved':False}
p=Path(__file__).with_name('results')/'qRB-radical-descent-contract.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
