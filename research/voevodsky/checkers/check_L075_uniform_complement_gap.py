#!/usr/bin/env python3
"""Instantiate the tau=.9 normalized complement theorem at L=.75."""
import json
from pathlib import Path
d=json.loads((Path(__file__).parents[1]/'results'/'normalized_prime_codefect_L075_scout.json').read_text());tau=.9;rank=d['retained_codefect_modes_above_point9'];upper=d['complement_codefect_upper'];out={'schema':'marici.voevodsky.L075-uniform-complement-gap.v1','tau':tau,'finite_dangerous_rank':rank,'computed_complement_codefect_upper':upper,'theorem_complement_upper':tau,'computed_normalized_gap':1-upper,'uniform_theorem_gap':1-tau,'passed':rank==7 and upper<=tau,'rh_proved':False};p=Path(__file__).parents[1]/'results'/'L075_uniform_complement_gap.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']
