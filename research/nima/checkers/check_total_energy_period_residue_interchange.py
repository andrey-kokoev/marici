"""Audit whether the formal E-residue descends through the source period integral."""
import json
available={'rational_integrand','explicit_simple_E_denominator','common_oriented_chain_at_generic_E','formal_integrand_residue'}
required={'relative_chain_specialization_to_E0','residue_integral_interchange','endpoint_trivialization_at_E0'}
missing=sorted(required-available)
assert len(missing)==3
print(json.dumps({'schema':'marici.nima.total-energy-period-residue-interchange.v1','status':'passed','available_objects':sorted(available),'required_period_residue_arrows':sorted(required),'missing':missing,'bold_conjecture':'the explicit simple E pole supplies a computable twisted-period residue','disposition':'falsified as a period-level claim','surviving_scope':'a formal rational-integrand residue exists generically','residual_conjecture':'the period residue requires source-derived E=0 relative-chain specialization and a residue/integration interchange theorem'},sort_keys=True))
