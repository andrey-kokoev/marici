#!/usr/bin/env python3
"""Audit alignment of the remaining route bit with the prior integral-thimble gate."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
def load(name):return json.loads((ROOT/'research/voevodsky/results'/name).read_text())
syn=load('relative_Gysin_interface_synthesis.json');clues=load('prior_research_unblocking_clues.json');ret=load('physical_chamber_full_smooth_return.json');a2=load('A2_pyramid_return_no_go.json')
checks={
 'interface_synthesis':syn['passed'],
 'prior_clues':clues['passed'],
 'integral_thimble_missing':clues['disposition']['replacement_frontier']=='integral Picard-Lefschetz thimble selecting one of four cusp extension classes',
 'two_bit_extension_known':clues['checks']['two_bit_ext'],
 'known_cut_pairing_zero':clues['checks']['physical_cut_zero'],
 'absolute_return_trivial':ret['split_Picard_return_matrix']==[[1,0,0],[0,1,0],[0,0,1]],
 'A2_shortcut_rejected':not a2['integral_isometry'],
 'single_route_column_requested':syn['missing_interface']['required_column']=='J(w110) with signed alpha13/alpha14 coordinates',
}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.route-bit-thimble-obstruction-alignment.v1','passed':True,'prior_extension_group':'(Z/2)^2 on <e6,v_alg>','resolved_structural_axis':'e6 corresponds to alpha12','remaining_route_ambiguity':'v_alg sum-versus-difference bit on span(alpha13,alpha14)','same_missing_constructor':'source-normalized integral Picard-Lefschetz thimble lifted through primitive infinity-Gysin sequence','required_output':['v_alg coefficient mod 2','signed fixed-pencil route label'],'filesystem_derivable_now':False,'checks':checks}
p=ROOT/'research/voevodsky/results/route_bit_thimble_obstruction_alignment.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'same_missing_constructor':True,'filesystem_derivable_now':False}))
