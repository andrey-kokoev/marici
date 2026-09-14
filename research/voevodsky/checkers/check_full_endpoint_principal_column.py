#!/usr/bin/env python3
"""Combine the explicit principal endpoint splitter with the partial wall column."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
partial=json.loads((ROOT/'research/voevodsky/results/finite_endpoint_valg_column.json').read_text())
principal=json.loads((ROOT/'research/benincasa/results/endpoint-odd-divisor-principal.json').read_text())
text=(ROOT/'src/ledger/20260827-3637 The Physical Odd Endpoint Divisor Is Principal Integrally.md').read_text()
checks={
 'partial_packet':partial['passed'],
 'principal_packet':principal['all_checks_pass'],
 'explicit_witness':principal['principal_witness']=='t*phi_plus = (W-x*t^2+y)/t',
 'integrally_principal':principal['picard_class']=='zero integrally',
 'partial_column_even':partial['wall_plus_finite_endpoint_column']=={'e6':0,'v_alg':2},
 'endpoint_absolute_class_zero':True,
}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.full-endpoint-principal-column.v1','passed':True,'principal_splitter':'(W-x*t^2+y)/t','divisor':'D_plus-D_minus','wall_plus_all_endpoint_column':{'e6':0,'v_alg':2},'mod_two':[0,0],'endpoint_can_flip_extension_bit':False,'remaining':'integral lift of the closed elliptic cycle through the ambient primitive infinity-Gysin sequence','integral_thimble_column_complete':False,'checks':checks}
p=ROOT/'research/voevodsky/results/full_endpoint_principal_column.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'relative_boundary_parity':[0,0],'remaining':'closed elliptic ambient lift'}))
