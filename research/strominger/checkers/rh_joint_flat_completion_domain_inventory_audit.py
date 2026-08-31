import json
from pathlib import Path

base=Path(__file__).parents[2]
results=Path(__file__).parents[1]/"results"
flat=(base/"nima"/"theta-log-moment-flatness-and-band-asymptotic-flatness-are-distinct-quotients.md").read_text(encoding="utf-8")
band=(base/"grothendieck"/"theta-boundaryless-band-sum-is-beyond-all-algebraic-orders.md").read_text(encoding="utf-8")
mass=json.loads((results/"rh_source_label_mass_prime_inverse_escape_audit.json").read_text(encoding="utf-8"))
graph=json.loads((results/"rh_log_degree_graph_prime_inverse_escape_audit.json").read_text(encoding="utf-8"))
isometry=json.loads((results/"rh_prime_isometry_synthesis_graph_dilation_audit.json").read_text(encoding="utf-8"))
checks={
 "flat_packet_requires_declared_arithmetic_completion":"Let \\(\\mathcal C_{\\mathrm{arith}}\\) be a completion" in flat,
 "completed_flat_sector_is_only_conditional":"can nevertheless be nontrivial if the chosen\ntopology admits" in flat,
 "boundary_current_requires_own_graph_topology":"Its own graph topology\nand completion domain still must be source-derived" in flat,
 "band_theorem_uses_superexponential_source_decay":"completed theta density decays super-exponentially" in band,
 "source_mass_inverse_completion_is_rejected":mass["checks"]["cutoff_uniform_inverse_bound_fails_already_on_associated_graded"],
 "log_graph_inverse_completion_is_rejected":graph["checks"]["logarithmic_weight_does_not_cancel_polynomial_escape"],
 "forward_isometric_domain_has_no_response_compression_theorem":"does not yet prove" in isometry["verdict"],
}
result={
 "schema":"marici.strominger.rh_joint_flat_completion_domain_inventory_audit.v1",
 "status":"passed" if all(checks.values()) else "failed",
 "sources":[
  "research/nima/theta-log-moment-flatness-and-band-asymptotic-flatness-are-distinct-quotients.md",
  "research/grothendieck/theta-boundaryless-band-sum-is-beyond-all-algebraic-orders.md",
  "research/strominger/results/rh_source_label_mass_prime_inverse_escape_audit.json",
  "research/strominger/results/rh_log_degree_graph_prime_inverse_escape_audit.json",
  "research/strominger/results/rh_prime_isometry_synthesis_graph_dilation_audit.json"],
 "inventory":{
  "source_label_mass":{"forward_transport":"contractive","all_joint_moments":"not established continuous","boundary_current":"not established continuous","uniform_inverse":"falsified"},
  "log_degree_graph":{"fixed_prime_transport":"bounded","all_joint_moments":"only finite graph powers individually","boundary_current":"domain suggested but not constructed","uniform_inverse":"falsified"},
  "forward_isometric_synthesis_graph":{"prime_transport":"uniform one-sided isometry","all_joint_moments":"not completed","boundary_current":"not extended","response_compression":"unproved"},
  "band_schwartz_domain":{"boundary_current":"supported by superexponential decay","arithmetic_pair_preimage":"not constructed","prime_transport":"not compared"}},
 "verdict":"No inspected source supplies one completion on which every joint product-ratio moment, the polarized theta synthesis, and the boundaryless current are simultaneously continuous. Source label mass and the logarithmic graph fail uniform inverse control; the forward isometric graph is only one-sided and lacks response compression; the band Schwartz-type domain has no constructed arithmetic pair preimage. Therefore a completed joint-flat witness cannot yet be posed as an element of an admitted common domain. The next construction must define a source-derived projective graph completion and prove continuity of both the joint jet family and the boundary current before searching for coefficients.",
 "checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=results/"rh_joint_flat_completion_domain_inventory_audit.json"
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
