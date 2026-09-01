import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "contracts" / "flavor-interaction-net-state.v1.json"
RESULT = ROOT / "results" / "wp1043_flavor_interaction_net_state.json"

data = json.loads(CONTRACT.read_text())
assert data["schema"] == "marici.flavor.interaction-net-state-contract.v1"

nodes = {node["id"]: node for node in data["nodes"]}
assert len(nodes) == len(data["nodes"])
assert data["terminal_node"] in nodes
assert nodes[data["terminal_node"]]["status"] == "open"

# Dependency graph is acyclic and every dependency exists.
visiting = set()
visited = set()

def visit(nid):
    assert nid in nodes
    if nid in visited:
        return
    assert nid not in visiting, f"cycle at {nid}"
    visiting.add(nid)
    for dep in nodes[nid].get("depends_on", []):
        visit(dep)
    visiting.remove(nid)
    visited.add(nid)

for nid in nodes:
    visit(nid)
assert len(visited) == len(nodes)

constructed = [n for n in nodes.values() if n["status"] == "constructed"]
open_nodes = [n for n in nodes.values() if n["status"] == "open"]
assert len(constructed) == 150
assert len(open_nodes) == 5

# Constructed nodes must have durable locators in the flavor programme.
for node in constructed:
    loc = node.get("locator")
    assert loc, node["id"]
    assert (ROOT.parents[1] / loc).exists(), loc
    assert node["authority_class"] in {"arithmetic_capacity", "negative_gate", "conditional_instrument", "conditional_gate", "productive_gate"}

# Open slots cannot be promoted by depending only on constructed negative gates.
for node in open_nodes:
    assert node["authority_class"] in {"formal_slot", "blocked_claim"}
    assert node.get("depends_on"), node["id"]

# Terminal remains blocked because all four required predecessor slots are open.
terminal = nodes[data["terminal_node"]]
terminal_deps = terminal["depends_on"]
assert set(terminal_deps) == {
    "common_integer_substrate_with_preparation_law",
    "typed_pole_spectrum_and_mass_clock",
    "calibrated_momentum_and_ratio_law",
    "physical16_gain_or_interference_law",
}
assert all(nodes[d]["status"] == "open" for d in terminal_deps)

# Rewrite rules point to constructed witnesses and do not target open slots.
for rule in data["rewrite_rules"]:
    witness = rule["witness_node"]
    assert witness in nodes
    assert nodes[witness]["status"] == "constructed"
    assert "rejects" in rule and rule["rejects"]
    assert rule.get("preserves_interface")

# Required semantic invariants are all active.
assert all(data["semantic_invariants"].values())
assert len(data["hostile_fixtures"]) == 148

# Interaction-net first open frontier: preparation, pole/clock, ratio, gain.
frontier = [n["id"] for n in open_nodes if n["id"] != data["terminal_node"]]
assert frontier == [
    "common_integer_substrate_with_preparation_law",
    "typed_pole_spectrum_and_mass_clock",
    "calibrated_momentum_and_ratio_law",
    "physical16_gain_or_interference_law",
]

result = {
    "schema": "marici.flavor.wp1043.v1",
    "status": "PASS",
    "contract": str(CONTRACT.relative_to(ROOT)),
    "constructed_nodes": len(constructed),
    "open_nodes": len(open_nodes),
    "terminal_node": data["terminal_node"],
    "terminal_status": terminal["status"],
    "frontier": frontier,
    "rewrite_rule_count": len(data["rewrite_rules"]),
    "hostile_fixture_count": len(data["hostile_fixtures"]),
    "classification": "valid interaction-net state contract; constructed part is a negative/rigidifier chain and terminal physical selector remains open",
    "first_blockers": {
        "source": "integer labels need a common substrate with a derived preparation order; WP1055-WP1057, WP1066-WP1071, and WP1080 give SU12/top-cell, SU6/localized-quartet, inflow, anomaly-vector, Green-Schwarz, shifted-coset, shifted-flux-interface, and SU3xSU3-carrier constructors but not a UV boundary action realizing the exact coset and temporal carrier dynamics",
        "threshold": "C=23 and degeneracy need atom-derived residues, spectrum, and mass clock; WP1053-WP1064 and WP1072-WP1073 give atom, irreducible, SU12/top-cell, SU6/localized-quartet, inflow, clock-alignment, parent-clock, common-twist, radius-clock, momentum, event-cell, flux-sector-degeneracy, and chirality-interface constructors but not localization, common compactification/preparation, or physical16 source dynamics",
        "instrument": "finite response needs calibrated momentum; WP1044-WP1052 give conditional coherent gain, visibility, common-frame transport, live-epoch, cofinality, null-accounting, shared-cell, typed event-cell, and common-source support rows; WP1060-WP1065 and WP1074-WP1079 close the inter-parent clock, vector-ratio cofiber, two-port lock, vector-ratio event cell, pole-event interface, soft-channel degeneracy, reweighting-rank, symmetric-production cofiber, four-state acquisition, Aspect-pattern composition, and Nima-candidate audit conditionally; WP1080 adds the SU3xSU3 bipartite carrier signature, WP1081 its Krylov-history composition gate, WP1082 the Strominger determinant-line audit, WP1083 the SU3-natural endomorphism no-go, WP1084 the localized-quartet flag no-go, WP1085 the conditional flux-Wilson flag gate, WP1086 the Wilson cyclic-ray gate, WP1087 the conditional history-dilation gate, WP1088 the history-volume-reference gate, WP1089 the oriented-adjoint no-go, WP1090 the reciprocal-determinant rho no-go, WP1091 the source-natural negative-weight scalar no-go, WP1092 the conditional-Wilson production-kernel no-go, WP1093 the history-dilation gain no-go, WP1094 the coset-to-boundary-action fiber, WP1095 the Wilson integer-lift clock no-go, WP1096 the normalization-packet authority audit, WP1097 the finite-scheme-port gain no-go, WP1098 the contact-counterterm boundary-lift no-go, WP1099 the integral-lattice clock-orientation no-go, WP1100 the alternating-cubic production-kernel no-go, WP1101 the anomaly-denominator clock no-go, WP1102 the bifundamental-pairing production-kernel no-go, WP1103 the pairing-cyclic-ray rho no-go, WP1104 the pairing-trace clock no-go, WP1105 the history-pairing gain no-go, WP1106 the minimal source-packet authority bundle, WP1107 the source-packet embodiment class gate, WP1108 the existing-defect fused-packet no-go, WP1109 the fused-boundary-defect field fiber, WP1110 the fused-defect anomaly-analyticity fiber, WP1111 the local Green-Schwarz split realizability fiber, WP1112 the endpoint-exchange split no-go, WP1113 the Wilson-orientation split-clock no-go, WP1114 the extended-line rho no-go, WP1115 the quotient-descent production-kernel no-go, WP1116 the localized-brane Green-function production-kernel no-go, WP1117 the brane-coupling representation fiber, WP1118 the physical16 event-representation no-go, WP1119 the physical16 amplitude algebra gate, WP1120 the complete-mixing source no-go, WP1121 the irreversible-boundary-mixing no-go, WP1122 the boundary S-matrix Hadamard gate, WP1123 the unitary S-matrix Hadamard classification, WP1124 the Hadamard phase-matching gate, WP1125 the anomaly-sector phase-provenance no-go, WP1126 the Green-residue event-basis no-go, WP1127 the production-constructor closure audit, WP1128 the event-production packet admission contract, WP1129 the event-production packet corpus search, WP1130 the six-branch preparation-law gate, WP1131 the parent-branching preparation no-go, WP1132 the dimension-trace preparation gate, WP1133 the UV boundary-state matching no-go, WP1134 the preparation-constructor closure audit, WP1135 the parent-projection mass-clock no-go, WP1136 the common-twist localization clock no-go, WP1137 the radius absolute-clock no-go, WP1138 the mass-clock constructor closure audit, WP1139 the physical16 two-port channel no-go, WP1140 the vector-KK gain-chain uniqueness audit, WP1141 the gain-compatibility no-go, WP1142 the common-gain reweighting-map classification, WP1143 the local rank-two no-go, WP1144 the minimal-support reweighting classification, WP1145 the rank-three matching gate, WP1146 the matching symmetry-orbit classification, WP1147 the twin-exchange no-go, WP1148 the quartet-quotient gate, WP1149 the quotient anomaly-invariance gate, and WP1150 the S-matrix phase matching gate, and WP1151 the fixed-q S-matrix disjointness gate, and WP1152 the doubly stochastic support gate, and WP1153 the support-three witness, and WP1154 the unistochastic witness no-go, and WP1155 the support-graph search, and WP1156 the support-four witness, and WP1157 the support-four graph search, and WP1158 the support-four polytope point, and WP1159 the support-four interior point, and WP1160 the phase-lift no-go, and WP1161 the phase-compatible constraint census, and WP1162 the split minimal amplitude no-go, and WP1163 the connected minimal amplitude no-go, and WP1164 the higher-constraint classification, and WP1165 the three-C4 amplitude no-go, and WP1166 the C4+C8 amplitude no-go, and WP1167 the boundary unistochastic audit, and WP1168 the support-five graph search, and WP1169 the support-five phase obstruction, and WP1170 the numerical unistochastic candidate, and WP1171 the exact unistochastic certificate, and WP1172 the production-realization no-go, and WP1173 the phase-gauge quotient, and WP1174 the channel-map no-go, and WP1175 the minimum-rank production kernel gate, and WP1176 the UV ensemble matching no-go, and WP1177 the UV boundary density no-go, and WP1178 the portal-to-sector dilation gate, and WP1179 the nontrivial dilation gate, and WP1180 the source-dynamics selection no-go, and WP1181 the transient sector interface, and WP1182 the threshold intertwiner no-go, and WP1183 the threshold basis/scale no-go, and WP1184 the dimensionful threshold anchor no-go, and WP1185 the threshold packet contract, and WP1186 the threshold boundary authority no-go but they leave scale preparation, explicit production kernel, event reweighting provenance, temporal constructors, and source gain open"
    }
}

RESULT.write_text(json.dumps(result, indent=2) + "\n")
print("WP1043 PASS:", len(constructed), len(open_nodes), ",".join(frontier))
