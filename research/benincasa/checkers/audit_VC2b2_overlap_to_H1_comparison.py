#!/usr/bin/env python3
"""Fast typing audit before attempting an expensive VC2b2 matrix computation."""
import gzip,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
domain=json.loads((ROOT/'research/benincasa/results/G12_source_labelled_overlap_domain.json').read_text())
pres=json.loads((ROOT/'research/benincasa/results/G12_char0_H1_presentation.json').read_text())
core=json.loads((ROOT/'research/benincasa/results/filtered_IBP_normal_crossing_core.json').read_text())
checks={'domain_constructed':domain['VC2b1_resolution']=='++','char0_presentation_constructed':pres['VC2b0_resolution']=='++','matrix_artifact_exists':(ROOT/pres['matrix_artifact']).exists(),'domain_is_incidence_only':'domain and incidence differentials only' in domain['scope'],'no_coefficient_realization':all(k not in domain for k in ('coefficient_map','form_representatives','map_to_C1')),'local_overlap_anticommutator_zero':core['two_wall_coherence']['identity']=='H_i H_j + H_j H_i=0 on ordered normal-crossing top forms','comparison_not_in_presentation':all(k not in pres for k in ('overlap_map','stage2_matrix'))}
assert all(checks.values()),checks
out={'schema':'marici.benincasa.VC2b2-overlap-to-H1-comparison-audit.v1','prospective_action':'VC2b2_compare_overlap_to_H1','resolution':'--','reason':'The overlap object is only the integral Cech incidence complex. It has no coefficient-valued form representatives or map into C1=Q^1330. The local Koszul anticommutator is zero and therefore cannot be promoted into a nonzero H1 differential by incidence data alone.','available_interfaces':['overlap_domain','char0_H1_presentation'],'missing_interface':'coefficient_realization_of_overlap_primitives_in_C1','avoided_computation':'No 1330-by-6 comparison matrix was fabricated or fitted; the typing failure is decidable from artifact schemas.','repair':'Insert VC2b1a_construct_coefficient_valued_overlap_representatives before VC2b2.','cost_observation':{'elapsed_class':'schema-only, subsecond expected','large_matrix_reconstruction_avoided':True},'checks':checks,'passed':True}
d=ROOT/'research/benincasa/results/VC2b2_overlap_to_H1_comparison_audit.json';d.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'VC2b2':'--','missing':out['missing_interface'],'avoided_large_compute':True}))
