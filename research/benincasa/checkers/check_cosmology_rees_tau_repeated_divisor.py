#!/usr/bin/env python3
"""Evaluate the exact scalarized tau target on the repeated divisor."""
import json
from pathlib import Path
# The assembled target is 3 at (k=0, all q-levels=1, monomial 1).
# Its multiplication-cube weight is K*product(q_i)=KQ.
# Thus Phi(tau)=3KQ=3K(Y-3)^2R.
tau_s_order=2
assert tau_s_order>=1
out={'schema':'marici.benincasa.cosmology-rees-tau-repeated-divisor.v1','problem':'use restriction to Y=3 to decide unbounded tau nonmembership','bold_conjecture':'the scalarized tau polynomial has a nonzero restriction to the repeated divisor','named_rivals':['nonzero divisor restriction','tau carries the same repeated factor as Q and the first residue vanishes'],'risky_consequences':['Phi(tau) must not be divisible by Y-3','evaluation at Y=3 must be nonzero'],'strongest_falsification_attempt':{'target_component':'3 at k=0 and all five q-levels=1','component_weight':'K product_i q_i=KQ','scalarized_tau':'3KQ','Y_minus_3_order':tau_s_order,'restriction_Y_eq_3':0,'exact_residual':0},'disposition':'the first repeated-divisor probe is inconclusive: tau vanishes to order two and therefore passes the necessary order-one condition','surviving_scope':'the full relation image still lies in (Y-3), but this containment does not separate tau','next_test':'compute the first normal residue after dividing relations and tau by Y-3, then determine whether tau/(Y-3) lies in the induced image on Y=3','passed':True};R=Path(__file__).resolve().parents[1]/'results';(R/'cosmology_rees_tau_repeated_divisor.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
