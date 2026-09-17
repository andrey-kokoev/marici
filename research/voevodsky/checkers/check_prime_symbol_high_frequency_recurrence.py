#!/usr/bin/env python3
"""Finite witness to high-frequency phase recurrence in a prime translation symbol."""
import json,math
from pathlib import Path
primes=[2,3,5];u=189162.6
errors=[abs(math.remainder(u*math.log(p),2*math.pi)) for p in primes]
weights=[math.log(p)/math.sqrt(p) for p in primes]
symbol=sum(2*w*math.cos(u*math.log(p)) for p,w in zip(primes,weights));mass=sum(2*w for w in weights)
out={'schema':'marici.voevodsky.prime-symbol-high-frequency-recurrence.v1','frequency':u,'primes':primes,'maximum_phase_error':max(errors),'symbol_to_absolute_mass_ratio':symbol/mass,'checks':{'frequency_above_100000':u>1e5,'all_generator_phases_within_0p012':max(errors)<.012,'symbol_exceeds_0p9999_absolute_mass':symbol/mass>.9999},'analytic_reason':'Compact-torus recurrence gives arbitrarily large simultaneous returns for every fixed finite prime packet.','passed':max(errors)<.012 and symbol/mass>.9999,'rh_proved':False}
p=Path(__file__).parents[1]/'results'/'prime_symbol_high_frequency_recurrence.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']
