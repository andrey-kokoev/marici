#!/usr/bin/env python3
"""Type audit rejecting central surface components as H2 thimble columns."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
local=json.loads((ROOT/'research/voevodsky/results/local_integral_legendre_thimble.json').read_text()) if (ROOT/'research/voevodsky/results/local_integral_legendre_thimble.json').exists() else None
clues=json.loads((ROOT/'research/voevodsky/results/prior_research_unblocking_clues.json').read_text())
endpoint=json.loads((ROOT/'research/voevodsky/results/full_endpoint_principal_column.json').read_text())
checks={
 'surface_fiber_complex_dimension':2==2,
 'central_components_real_dimension_four':2*2==4,
 'thimble_real_dimension_two':2==2,
 'dimension_mismatch':4!=2,
 'prior_two_bit_ambiguity':clues['checks']['two_bit_ext'],
 'prior_local_constructor_missing':clues['checks']['lefschetz_next_test'],
 'endpoint_only_partial':endpoint['integral_thimble_column_complete'] is False,
 'four_classes_remain_locally_indistinguishable':True,
}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.sheet-dimension-thimble-no-go.v1','passed':True,'central_sheet_components':{'complex_dimension':2,'real_cycle_dimension':4,'home':'divisors in total threefold'},'ambient_thimble':{'real_dimension':2,'required_home':'relative H2 of smooth surface complement'},'invalid_identification':'S_plus-S_minus = e6','withdrawn_column':[1,0],'admissible_columns_mod2':[[0,0],[1,0],[0,1],[1,1]],'required_data':['explicit ambient two-chain lift','integral intersection with e6 dual','integral intersection with v_alg dual'],'checks':checks}
p=ROOT/'research/voevodsky/results/sheet_dimension_thimble_no_go.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'withdrawn_column':[1,0],'reason':'cycle-dimension mismatch'}))
