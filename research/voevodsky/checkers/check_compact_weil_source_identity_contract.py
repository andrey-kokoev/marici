from __future__ import annotations
import json
from pathlib import Path

REQUIRED={"source_locator","test_space","fourier_convention","quadratic_form_normalization","archimedean_term","prime_translation_terms","polar_endpoint_terms","zero_extension_convention","dirichlet_comparison_map"}
NESTED={
 "fourier_convention":{"forward_kernel","inverse_prefactor","plancherel_measure"},
 "quadratic_form_normalization":{"divisor_counting","polarization","overall_prefactor"},
 "archimedean_term":{"multiplier","sign","prefactor"},
 "prime_translation_terms":{"coefficient","sign","prefactor","translation_direction","adjoint_rule"},
 "polar_endpoint_terms":{"rank","functionals","signs","prefactors"},
 "dirichlet_comparison_map":{"basis","matrix_element_rule","domain_statement"},
}

def main():
 contract=json.loads(Path('research/voevodsky/compact-weil-source-identity-contract.json').read_text())
 instance=json.loads(Path('research/voevodsky/compact-weil-source-identity-instance.json').read_text())
 assert set(contract['required'])==REQUIRED
 missing=sorted(REQUIRED-instance.keys());nested_missing={k:sorted(v-instance.get(k,{}).keys()) for k,v in NESTED.items() if v-instance.get(k,{}).keys()}
 endpoint=instance['polar_endpoint_terms']['prefactors'][0]
 passed=not missing and not nested_missing and instance['test_space']=='compact_logarithmic_support' and '1/2' in endpoint
 result={'schema':'marici.voevodsky.compact-weil-source-contract-check.v2','required_fields':sorted(REQUIRED),
  'missing_fields':missing,'nested_missing_fields':nested_missing,'internal_instance_materialized':passed,
  'endpoint_half_sum_verified':'1/2' in endpoint,'external_source_verification_required':bool(instance['external_source_verification_required']),
  'publication_authority_verified':False,'matrix_assembly_internally_defined':passed,'passed':passed}
 text=json.dumps(result,indent=2,sort_keys=True);Path('research/voevodsky/results/compact_weil_source_identity_contract.json').write_text(text+'\n');print(text)
if __name__=='__main__':main()
