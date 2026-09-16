"""Dual-mode admission audit for coercive and gapless positive completions."""
import copy,json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).parents[1]
COMMON=['finite_forms_source_derived','candidate_form_source_derived','comparison_maps_source_derived','common_core_dense','candidate_form_closable','closure_domain_identified','restriction_core_invariant','mosco_or_strong_resolvent_witness','closed_limit_positive','limit_radical_declared','restriction_completion_cells']
COERCIVE=['finite_radicals_declared','radical_stability','comparison_descends_to_quotients']
SPECTRAL=['spectral_thresholds_positive','spectral_thresholds_decrease_to_zero','spectral_projections_source_derived','stage_coercivity_verified','spectral_stage_transitions_compatible','spectral_tower_strongly_exhausts_radical_complement','zero_spectral_projection_equals_declared_radical','finite_comparisons_lift_to_spectral_stages']
def admit(c):
 for k in COMMON:
  if c.get(k) is not True:return False,k
 mode=c.get('mode')
 if mode=='coercive_quotient':
  for k in COERCIVE:
   if c.get(k) is not True:return False,k
  for k in ('positive_quotient_coercivity_bound','positive_reduced_minimum_modulus'):
   if Fraction(str(c.get(k,0)))<=0:return False,k
  return True,'admitted_coercive_quotient'
 if mode=='gapless_spectral_tower':
  for k in SPECTRAL:
   if c.get(k) is not True:return False,k
  thresholds=[Fraction(str(x)) for x in c.get('spectral_thresholds',[])]
  if not thresholds or any(x<=0 for x in thresholds):return False,'spectral_thresholds'
  if any(thresholds[i+1]>=thresholds[i] for i in range(len(thresholds)-1)):return False,'spectral_threshold_order'
  return True,'admitted_gapless_spectral_tower'
 return False,'mode'
base={k:True for k in COMMON}
coercive=base|{k:True for k in COERCIVE}|{'mode':'coercive_quotient','positive_quotient_coercivity_bound':'1/3','positive_reduced_minimum_modulus':'1/4'}
spectral=base|{k:True for k in SPECTRAL}|{'mode':'gapless_spectral_tower','spectral_thresholds':['1','1/2','1/4','1/8']}
assert admit(coercive)==(True,'admitted_coercive_quotient')
assert admit(spectral)==(True,'admitted_gapless_spectral_tower')
hostiles={}
for field in SPECTRAL:
 c=copy.deepcopy(spectral);c[field]=False;ok,reason=admit(c);assert not ok and reason==field;hostiles[field]=reason
for name,vals,reason in [('zero_threshold',['1','0'],'spectral_thresholds'),('unordered',['1','1/2','3/4'],'spectral_threshold_order')]:
 c=copy.deepcopy(spectral);c['spectral_thresholds']=vals;ok,got=admit(c);assert not ok and got==reason;hostiles[name]=got
out={'schema':'marici.voevodsky.coherence-pyramid-completion-interface-v2-check.v1','coercive_fixture':admit(coercive)[1],'gapless_fixture':admit(spectral)[1],'spectral_hostile_refusals':hostiles,'archimedean_mode':'gapless_spectral_tower','completion_functor_claimed':False,'next_gate':'transport spectral-stage certificates under horizontal and vertical composition','passed':True}
if __name__=='__main__':
 p=ROOT/'results'/'coherence-pyramid-completion-interface-v2.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
