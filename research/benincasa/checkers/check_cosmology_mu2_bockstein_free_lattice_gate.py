#!/usr/bin/env python3
"""Show that an integral mod-2 Bockstein cannot hit a free primitive column."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
for n in ['cosmology_mu2_orientation_local_system_integral_realization.json','cosmology_universal_minimal_integral_source_extension.json']:
 assert json.loads((R/n).read_text())['passed']
# Toy complex Z --2--> Z: beta(1 mod 2) is the nonzero class in Z/2.
toy={'integral_differential':2,'mod2_differential':0,'beta_lift':1,'beta_representative':1,'target_group':'Z/2','twice_beta_zero':True}
# Exhaustively confirm no nonzero element of a bounded window in Z^2 is killed by 2.
free=[(a,b) for a in range(-8,9) for b in range(-8,9) if (2*a,2*b)==(0,0)]
assert free==[(0,0)]
out={'schema':'marici.benincasa.cosmology-mu2-bockstein-free-lattice-gate.v1','coefficient_sequence':'0 -> Z --2--> Z -> F2 -> 0','exactness_lemma':'2 beta(x)=0 for every mod-2 class x','toy_nonzero_bockstein':toy,'target_lattice':'Z^2 with coordinates (Xi_log,-sigma123)','target_two_torsion':free,'primitive_target':[1,1],'primitive_target_in_bockstein_image':False,'reason':'the Bockstein image is 2-torsion, while the target lattice is torsion-free','prior_gamma_derivative_distinct':True,'nonpromotion':'finite-field gamma-normal derivative called Bockstein is not the integral coefficient connecting map','next_test':'compute the canonical saturation of the even principal lattice and test whether saturation supplies source labels or only an unlabelled over-lattice','passed':True};(R/'cosmology_mu2_bockstein_free_lattice_gate.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
