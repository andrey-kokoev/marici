import json
from pathlib import Path


semantic_profile = {
    "source_state_separation": True,
    "target_image_admission": True,
    "local_and_global_coherence": True,
    "completion_stability": True,
    "source_authority": True,
}

resource = {
    "input_tokens": 1,
    "claimed_output_tokens": 2,
}
resource["conserves"] = resource["input_tokens"] == resource["claimed_output_tokens"]
assert not resource["conserves"]

temporal = {
    "evidence_epoch": 1,
    "execution_epoch": 2,
    "authorized_transition": False,
}
temporal["valid"] = (
    temporal["evidence_epoch"] == temporal["execution_epoch"]
    or temporal["authorized_transition"]
)
assert not temporal["valid"]

n, q, f = 3, 2, 1
minimum_overlap = max(0, 2 * q - n)
byzantine_safe = minimum_overlap > f
fault = {
    "replicas": n,
    "quorum": q,
    "byzantine_fault_bound": f,
    "minimum_overlap": minimum_overlap,
    "safe": byzantine_safe,
}
assert not fault["safe"]

hostiles = {
    "resource_overdraft": {"semantic": semantic_profile, "operational": resource},
    "expired_authority": {"semantic": semantic_profile, "operational": temporal},
    "wrong_fault_model": {"semantic": semantic_profile, "operational": fault},
}

for hostile in hostiles.values():
    assert all(hostile["semantic"].values())

result = {
    "status": "pass",
    "claim": "semantic validity and operational realizability are independent compiler axes",
    "hostiles": hostiles,
    "semantic_gate_count": 5,
    "operational_obligations": ["resource", "temporal_epoch", "fault_model"],
    "operative_constructor_admitted": False,
}

out = Path(__file__).parents[1] / "results" / "semantic-vs-operational-axes.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

