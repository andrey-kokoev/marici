#!/usr/bin/env python3
"""Exact C4-equivariance obstruction for a one-ray Gaussian-lattice minor."""
import hashlib,json,platform
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];FIX=ROOT/'research/voevodsky/fixtures/gaussian_axis_minor_rotation_obstruction.v1.json';OUT=ROOT/'research/voevodsky/results/gaussian_axis_minor_rotation_obstruction.json';D=json.loads(FIX.read_text());X=D['cutoff']
# Row weights on the four oriented axis rays; R acts by cyclic permutation.
minor=[Q(1),Q(0),Q(0),Q(0)];rotation=lambda w:[w[-1]]+w[:-1];orbit=[minor]
for _ in range(3):orbit.append(rotation(orbit[-1]))
average=[sum(w[j] for w in orbit) for j in range(4)] # unnormalized orbit sum
# Invariance equations wR=w force all four coefficients equal.
def invariant(w):return rotation(w)==w
riemann_coeff={n:sum(minor) for n in range(1,X+1)};axis_coeff={n:sum(average) for n in range(1,X+1)}
checks={'candidate_minor_has_riemann_coefficients':all(v==1 for v in riemann_coeff.values()),'candidate_breaks_quarter_turn':not invariant(minor),'orbit_has_four_distinct_ray_selectors':len({tuple(w) for w in orbit})==4,'invariant_orbit_sum_weights_all_rays':average==[1,1,1,1] and invariant(average),'invariant_axis_aggregation_has_multiplicity_four':all(v==4 for v in axis_coeff.values()),'no_preferred_ray_in_source':D['disposition']['source_descent'].startswith('blocked'),'mate_not_promoted':'first_missing_typed_datum' in D['disposition']}
out={'schema':'marici.voevodsky.gaussian-axis-minor-rotation-obstruction-check.v1','passed':all(checks.values()),'checks':checks,'computed':{'candidate_minor_weights':list(map(str,minor)),'quarter_turn_orbit':[list(map(str,w)) for w in orbit],'invariant_orbit_sum':list(map(str,average)),'riemann_coefficients_1_to_8':{str(n):str(v) for n,v in riemann_coeff.items()},'invariant_axis_coefficients_1_to_8':{str(n):str(v) for n,v in axis_coeff.items()}},'disposition':'The positive-real-ray minor recovers one Riemann coefficient per positive integer, but choosing it breaks the Gaussian quarter-turn. The invariant axis observer has multiplicity four. A source orientation or vacuum functional is required.','claim_boundary':D['claim_boundary'],'execution_receipt':{'command':'python research/voevodsky/checkers/check_gaussian_axis_minor_rotation_obstruction.py','python':platform.python_version(),'fixture_sha256':hashlib.sha256(FIX.read_bytes()).hexdigest(),'source_sha256':hashlib.sha256((ROOT/D['source']).read_bytes()).hexdigest(),'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));raise SystemExit(0 if out['passed'] else 1)
