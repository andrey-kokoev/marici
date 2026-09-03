"""Typed gate audit for promoting the negative spline packet to an RH conclusion."""
import json
gates={
 'standard_Weil_functional_global_sign':False,
 'criterion_autocorrelation_involution':False,
 'scaling_and_spectral_positivity_orientation':False,
 'scale_covariant_double_pole_annihilator':False,
 'independent_archimedean_and_prime_reproduction':False,
}
missing=[k for k,v in gates.items() if not v]
assert len(missing)==5
print(json.dumps({'schema':'marici.nima.negative-spline-criterion-gate.v2','status':'passed','negative_hybrid_functional_value_established':True,'comparison_gates':gates,'missing_gates':missing,'rh_conclusion_defined':False,'correction':'fixed a under c=1/2 moves annihilator zeros to plus/minus 1/4, so omitted pole cells are unjustified','bold_conjecture':'the corrected N=3 negative spline packet is already a criterion-level alarm with pole deletion closed','disposition':'falsified','residual_conjecture':'regenerate with a_c=c*a or explicit pole cells before applying independent zero-side, digamma, and theorem-sign discriminators'},sort_keys=True))
