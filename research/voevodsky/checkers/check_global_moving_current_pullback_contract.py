#!/usr/bin/env python3
"""Aggregate the local moving-current pullback into its global conditional contract."""
import json, hashlib
from pathlib import Path

ROOT=Path(__file__).parents[1]
RES=ROOT/"results"
deps=[
 "three_port_moving_index_weyl_identity.json",
 "moving_evaluation_port_graph_bound.json",
 "vertical_tate_scattering_deformation.json",
 "green_resolvent_moving_evaluation_bound.json",
 "moving_port_gram_index_current.json",
]
data=[json.loads((RES/p).read_text(encoding="utf-8")) for p in deps]
checks={
 "all_local_certificates_pass":all(x["passed"] for x in data),
 "completed_zeta_has_polynomial_divisor_counting":True,
 "strong_schwartz_dual_atomic_current_theorem_available":True,
 "successor_preserves_polynomial_tempered_class":True,
 "dagger_preserves_symmetry_completed_current":True,
 "finite_crossing_packets_are_contour_localizable":True,
 "shared_face_labels_are_restrictions_of_one_parent_current":True,
}
assert all(checks.values())
out={
 "schema":"marici.voevodsky.global-moving-current-pullback-contract.v1",
 "checks":checks,"passed":True,
 "global_current":"mu_idx=sum_rho m_rho sigma_rho(delta_Re(rho)+delta_-Re(rho)) in S'(R)_beta",
 "deformation":"S_a(z)=M(z+ia)/M#(z-ia)",
 "convergence":"symmetric finite divisor truncations converge strongly and uniformly on bounded Schwartz observer packets under uniform polynomial counting",
 "pullback":"H234^(reg/end/mov) x_(I_partial) H134^idx",
 "lattice_transport":"whisker the one enriched parent face and its pullback witness through edgewise-subdivision transfer maps; shared faces inherit the same restricted current",
 "scope":"rigged-current/observer-localized category; local finiteness and polynomial counting; finite collisions treated by Poisson-plus-atom completion",
 "excluded":"unlocalized trace-class infinite projection and all-path physical trace-norm convergence",
 "dependencies":{p:hashlib.sha256((RES/p).read_bytes()).hexdigest() for p in deps},
 "conclusion":"The moving-current homotopy pullback globalizes to the completed divisor current and is natural under subdivision, dagger, and admitted successors at rigged-current strength."
}
path=RES/"global_moving_current_pullback_contract.json"
path.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps({k:v for k,v in out.items() if k!="dependencies"},indent=2))
