"""Audit the direction of frozen three-site source arrows."""
import json
# Frozen source: flat-space wavefunction -> site-energy integral -> graph coefficient -> twisted-period presentation.
edges={('flat_space_wavefunction','site_energy_integral'),('site_energy_integral','graph_coefficient'),('graph_coefficient','twisted_period_integrand')}
def reachable(src,dst):
 seen={src}; changed=True
 while changed:
  changed=False
  for a,b in edges:
   if a in seen and b not in seen: seen.add(b); changed=True
 return dst in seen
forward=reachable('flat_space_wavefunction','graph_coefficient')
reverse=reachable('graph_coefficient','flat_space_wavefunction')
assert forward and not reverse
print(json.dumps({'schema':'marici.nima.three-site-total-energy-reverse-arrow.v1','status':'passed','frozen_edges':[list(x) for x in sorted(edges)],'forward_source_map_exists':forward,'reverse_residue_to_independently_normalized_amplitude_exists':reverse,'bold_conjecture':'the frozen three-site source already supplies a normalized total-energy-residue map from graph coefficient to flat-space amplitude','disposition':'falsified as a source-typing claim','residual_conjecture':'the explicit E-pole defines a candidate residue object, but equality to an amplitude requires an independently sourced codomain and normalization'},sort_keys=True))
