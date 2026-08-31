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
assert len(constructed) == 60
assert len(open_nodes) == 5

# Constructed nodes must have durable locators in the flavor programme.
for node in constructed:
    loc = node.get("locator")
    assert loc, node["id"]
    assert (ROOT.parents[1] / loc).exists(), loc
    assert node["authority_class"] in {"arithmetic_capacity", "negative_gate", "conditional_instrument", "conditional_gate"}

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
assert len(data["hostile_fixtures"]) == 58

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
        "instrument": "finite response needs calibrated momentum; WP1044-WP1052 give conditional coherent gain, visibility, common-frame transport, live-epoch, cofinality, null-accounting, shared-cell, typed event-cell, and common-source support rows; WP1060-WP1065 and WP1074-WP1079 close the inter-parent clock, vector-ratio cofiber, two-port lock, vector-ratio event cell, pole-event interface, soft-channel degeneracy, reweighting-rank, symmetric-production cofiber, four-state acquisition, Aspect-pattern composition, and Nima-candidate audit conditionally; WP1080 adds the SU3xSU3 bipartite carrier signature, WP1081 its Krylov-history composition gate, WP1082 the Strominger determinant-line audit, WP1083 the SU3-natural endomorphism no-go, WP1084 the localized-quartet flag no-go, WP1085 the conditional flux-Wilson flag gate, WP1086 the Wilson cyclic-ray gate, WP1087 the conditional history-dilation gate, WP1088 the history-volume-reference gate, WP1089 the oriented-adjoint no-go, WP1090 the reciprocal-determinant rho no-go, WP1091 the source-natural negative-weight scalar no-go, WP1092 the conditional-Wilson production-kernel no-go, WP1093 the history-dilation gain no-go, WP1094 the coset-to-boundary-action fiber, WP1095 the Wilson integer-lift clock no-go, and WP1096 the normalization-packet authority audit but they leave scale preparation, explicit production kernel, event reweighting provenance, temporal constructors, and source gain open"
    }
}

RESULT.write_text(json.dumps(result, indent=2) + "\n")
print("WP1043 PASS:", len(constructed), len(open_nodes), ",".join(frontier))
