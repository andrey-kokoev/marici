#!/usr/bin/env python3
"""Certified Arb enclosure of the first nontrivial zeta zero."""
import json,sys
from pathlib import Path
try:
 import flint
 from flint import acb
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'))
 import flint
 from flint import acb
flint.ctx.prec=256
z=acb.zeta_zero(1)
out={
 'schema':'marici.voevodsky.first-zeta-zero-arb-enclosure.v1',
 'precision_bits':flint.ctx.prec,
 'zero_ball':str(z),
 'real_ball':str(z.real),
 'ordinate_ball':str(z.imag),
 'contains_critical_line':bool(z.real.contains(acb('0.5').real)),
 'arb_certified_zero_index':1,
 'passed':bool(z.real.contains(acb('0.5').real)),
 'rh_proved':False,
}
p=Path(__file__).parents[1]/'results'/'first_zeta_zero_arb_enclosure.json'
p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
assert out['passed']
