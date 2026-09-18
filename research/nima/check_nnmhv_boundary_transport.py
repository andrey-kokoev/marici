#!/usr/bin/env python3
"""Verify Lrep/Urep as sequential transported-spinor state updates."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/nima'))
from nnmhv_coherence_paths import compile_nnmhv_histories,terminal_r_state
h6=compile_nnmhv_histories(6)[0];s6=terminal_r_state(h6)
h7=compile_nnmhv_histories(7);lower_history=next(h for h in h7 if any(u.side=='lower' for u in h.boundary_updates));sl=terminal_r_state(lower_history)
# Find a terminal R with neither endpoint replacement at a larger multiplicity.
plain_history=next(h for h in compile_nnmhv_histories(9) if not h.boundary_updates);sp=terminal_r_state(plain_history)
checks={'six_point_xi_chain':s6.xi.vertices==(6,5,2) and s6.xi.matrix_edges==((6,5),(5,2)),'six_point_default_lower_spinor':s6.lower_spinor.vertices==(2,) and s6.lower_spinor.is_external,'six_point_Urep_chain':s6.upper_spinor.vertices==(6,2,5) and s6.upper_spinor.matrix_edges==((6,2),(2,5)),'right_branch_xi_is_untransported_n':sl.xi.vertices==(7,),'Lrep_uses_outer_path':sl.lower_spinor.vertices==(7,)+lower_history.outer_pair,'Lrep_leaves_upper_external':sl.upper_spinor.vertices==(lower_history.inner_pair[1],),'no_update_uses_explicit_endpoint_spinors':sp.lower_spinor.vertices==(plain_history.inner_pair[0]-1,) and sp.upper_spinor.vertices==(plain_history.inner_pair[1],)}
out={'schema':'marici.nima.nnmhv-boundary-transport.v1','source':'arXiv:0808.2475 equations generalR, Lrep, Urep','six_point':{'history':{'outer':h6.outer_pair,'inner':h6.inner_pair},'xi_vertices':s6.xi.vertices,'lower_vertices':s6.lower_spinor.vertices,'upper_vertices':s6.upper_spinor.vertices},'lower_update_example':{'n':lower_history.n,'outer':lower_history.outer_pair,'inner':lower_history.inner_pair,'xi_vertices':sl.xi.vertices,'lower_vertices':sl.lower_spinor.vertices,'upper_vertices':sl.upper_spinor.vertices},'plain_example':{'n':plain_history.n,'outer':plain_history.outer_pair,'inner':plain_history.inner_pair,'lower_vertices':sp.lower_spinor.vertices,'upper_vertices':sp.upper_spinor.vertices},'checks':checks,'passed':all(checks.values()),'scope':'Exact symbolic path implementation of endpoint spinor replacements; x-matrix chains are typed but not yet numerically evaluated.'}
p=ROOT/'research/nima/results/nnmhv-boundary-transport.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
