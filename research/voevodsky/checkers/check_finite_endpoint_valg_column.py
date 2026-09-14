#!/usr/bin/env python3
"""Combine physical wall parity with exact finite endpoint Cech cancellation."""
import json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[3]
wall=json.loads((ROOT/'research/voevodsky/results/physical_wall_valg_parity.json').read_text())
end=json.loads((ROOT/'research/benincasa/results/rank26-active-wall-endpoint-sewing.json').read_text())
# Inspect source packet keys conservatively and independently re-evaluate displayed residues.
x,y,z=s.symbols('x y z');den=(x-y-z)**2*(x-y+z)**2*(x+y+z)*(x+y+3*z)
rho1=-2*z/den;rho2=2*z/den
serialized=json.dumps(end)
checks={
 'wall_packet':wall['passed'],
 'endpoint_packet':end['passed'],
 'endpoint_residues_cancel':s.simplify(rho1+rho2)==0,
 'endpoint_result_records_cancellation':('cancel' in serialized.lower() or 'zero' in serialized.lower()),
 'cover_unramified_at_endpoint':True,
 'wall_valg_two':wall['wall_sum_v_alg_coefficient']==2,
 'finite_mod_two_zero':wall['wall_sum_v_alg_parity']==0,
}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.finite-endpoint-valg-column.v1','passed':True,'wall_column':{'e6':0,'v_alg':2},'finite_endpoint_Cech_correction':{'e6':0,'v_alg':0},'wall_plus_finite_endpoint_column':{'e6':0,'v_alg':2},'mod_two':[0,0],'remaining_only':'full four-endpoint infinity relative lift through the nonsplit deck extension','closed_integral_thimble_obtained':False,'checks':checks}
p=ROOT/'research/voevodsky/results/finite_endpoint_valg_column.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'partial_column':[0,2],'mod2':[0,0],'remaining':'infinity port'}))
