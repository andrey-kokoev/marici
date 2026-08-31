#!/usr/bin/env python3
"""Exact lattice conditions on any source enlargement capable of a primitive tau_p lift."""
import json, math
from pathlib import Path
R=Path(__file__).resolve().parents[1]/'results'
existing_principal_generator=2
exceptional_column=(0,1)
required=(1,1)
# Adding one column (a,b) can reach Xi coefficient 1 iff gcd(2,a)=1.
tests=[]
for a in range(-6,7):
    tests.append({'a':a,'primitive_Xi_reachable':math.gcd(existing_principal_generator,abs(a))==1,'a_is_odd':a%2!=0})
assert all(t['primitive_Xi_reachable']==t['a_is_odd'] for t in tests)
out={'schema':'marici.benincasa.cosmology-minimal-primitive-source-enlargement.v1','existing_principal_lattice':'2Z','existing_exceptional_column':list(exceptional_column),'required_column':list(required),'necessary_new_data':{'odd_Xi_log_coefficient':True,'ordered_cech_obstruction_correction':[0,-2,2],'explicit_g23_g31_routing':True,'integral_chain_map_and_d_squared_zero':True},'single_generator_lattice_criterion':'for new column (a,b), gcd(2,a)=1; equivalently a is odd','sufficiency':False,'reason_not_sufficient':'The lattice criterion does not construct a sourced generator, its boundary, or the weighted comparison map.','bounded_exact_tests':tests,'passed':True};(R/'cosmology_minimal_primitive_source_enlargement.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
