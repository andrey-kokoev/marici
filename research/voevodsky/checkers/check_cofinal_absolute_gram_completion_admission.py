"""Admission audit for the cofinal spectrally adapted absolute-Gram system."""
import importlib.util,json
from pathlib import Path
ROOT=Path(__file__).parents[1]
spec=importlib.util.spec_from_file_location('completion',ROOT/'checkers'/'check_coherence_pyramid_completion_interface.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
certificate={
 'finite_forms_source_derived':True,
 'candidate_form_source_derived':True,
 'comparison_maps_source_derived':True,
 'common_core_dense':True,
 'candidate_form_closable':True,
 'closure_domain_identified':True,
 'restriction_core_invariant':True,
 'mosco_or_strong_resolvent_witness':True,
 'closed_limit_positive':True,
 'finite_radicals_declared':True,
 'limit_radical_declared':True,
 # Strong convergence alone does not identify eventual finite radicals with ker |A_S|.
 'radical_stability':False,
 'comparison_descends_to_quotients':False,
 'positive_quotient_coercivity_bound':'0',
 'positive_reduced_minimum_modulus':'0',
 'restriction_completion_cells':True,
}
admitted,reason=mod.admit(certificate)
out={'schema':'marici.voevodsky.cofinal-absolute-gram-completion-admission.v1','admitted':admitted,'first_refusal':reason,'established_gates':[k for k,v in certificate.items() if v is True],'open_gates':['radical_stability','comparison_descends_to_quotients','positive_quotient_coercivity_bound','positive_reduced_minimum_modulus'],'interpretation':'The cofinal system constructs the positive strong limit, while the coercive radical-quotient completion interface awaits spectral control at zero.','next_test':'Determine whether zero is isolated in the spectrum of |A_S| on the declared quotient; equivalently compute a positive lower bound or certify reduced minimum modulus zero.'}
if __name__=='__main__':
 p=ROOT/'results'/'cofinal-absolute-gram-completion-admission.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
