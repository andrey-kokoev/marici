#!/usr/bin/env python3
"""Classify the minimal integral ordered-boundary correction for the tau source cell."""
import json, itertools, math
from pathlib import Path
R=Path(__file__).resolve().parents[1]/'results'
obstruction=(0,2,-2)
required=tuple(-x for x in obstruction)
assert sum(obstruction)==sum(required)==0
# Exact cancellation has a unique literal correction vector.
solutions=[v for v in itertools.product(range(-3,4),repeat=3) if tuple(v[i]+obstruction[i] for i in range(3))==(0,0,0)]
assert solutions==[required]
assert sum(abs(x) for x in required)==4
assert sum(x!=0 for x in required)==2
assert math.gcd(*(abs(x) for x in required))==2
# One ordinary ordered simplex has incidence coefficients only 0,+/-1.
single_simplex_possible=all(abs(x)<=1 for x in required)
assert not single_simplex_possible
out={'schema':'marici.benincasa.cosmology-ordered-boundary-odd-principal-source-classification.v1','obstruction':list(obstruction),'unique_literal_correction':list(required),'downstream_boundary_sum':sum(required),'l1_norm':4,'support_size':2,'content_gcd':2,'single_unit_incidence_cell_possible':False,'minimal_source_shape':'an odd principal/logarithmic leg together with two even exceptional-face legs of opposite ordered sign','realization_alternatives':['two coherently oriented incidence occurrences on each supported exceptional face','one source cell with a degree-two attaching coefficient on each supported face'],'excluded_realization':'doubling the entire source generator, because that also doubles the principal coefficient and restores even parity','qualification':'closed boundary cycles may be added only after a separately sourced kernel class is specified; literal minimal cancellation is unique','passed':True};(R/'cosmology_ordered_boundary_odd_principal_source_classification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
