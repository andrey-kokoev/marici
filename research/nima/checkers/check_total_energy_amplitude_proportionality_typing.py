"""Test whether the frozen source types an E-residue/amplitude proportionality claim."""
import json
objects={'flat_space_wavefunction','site_energy_integral','graph_coefficient','twisted_period_integrand','E_residue_candidate'}
edges={('flat_space_wavefunction','site_energy_integral'),('site_energy_integral','graph_coefficient'),('graph_coefficient','twisted_period_integrand'),('twisted_period_integrand','E_residue_candidate')}
required={'scattering_amplitude','common_coefficient_object','comparison_map'}
missing=sorted(required-objects)
assert missing==['common_coefficient_object','comparison_map','scattering_amplitude']
print(json.dumps({'schema':'marici.nima.total-energy-amplitude-proportionality-typing.v1','status':'passed','frozen_objects':sorted(objects),'frozen_edges':[list(x) for x in sorted(edges)],'required_for_proportionality':sorted(required),'missing_typed_objects':missing,'bold_conjecture':'the E-residue candidate is proportional to a flat-space scattering amplitude','disposition':'falsified as a typed claim: the comparison is undefined','residual_conjecture':'only the E-residue candidate exists; amplitude interpretation must remain withdrawn until a common coefficient object and comparison map are sourced'},sort_keys=True))
