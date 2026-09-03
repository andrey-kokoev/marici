#!/usr/bin/env python3
"""Compute the integral K2 correction on the materialized horn overlap."""
import json
from pathlib import Path
P=Path(__file__).resolve();ROOT=P.parents[3];B=ROOT/'research'/'benincasa';R=B/'results'
t=json.loads((B/'g12-g31-residue-chart-transition.json').read_text());assert t['transition']['orientation_sign']==-1
# Milnor bilinearity for u'=u/v, v'=1/v:
# {u/v,1/v}=-{u,v}+{-1,v}, using {a,a}={a,-1}.
out={'schema':'marici.benincasa.cosmology-horn-full-overlap-cocycle.v1','materialized_overlap':'G12-G31','ratio_transition':{'u_prime':'u/v','v_prime':'1/v'},'milnor_K2_transform':'{u_prime,v_prime}=-{u,v}+{-1,v}','determinant_sign_part':'-{u,v}','integral_unit_correction':'{-1,v}','correction_two_torsion':True,'strict_integral_symbol_descent_on_overlap':False,'sign_local_descent_after_forgetting_two_torsion':True,'full_three_chart_cocycle_materialized':False,'missing_transitions':['G12-G23','G23-G31'],'decision':'The known overlap carries a nontrivial possible two-torsion unit correction {-1,v}; orientation sign alone proves logarithmic descent but not strict integral K2 descent. The full cocycle cannot be closed until the other two source transitions and their unit corrections are materialized.','next_test':'construct the two cyclic source transitions and test whether their three {-1,ratio} corrections sum to zero on the triple overlap','limitations':['does not assert {-1,v} is nonzero on the actual function field','strict descent could be restored by an explicit source trivialization'],'passed':True};(R/'cosmology_horn_full_overlap_cocycle.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
