from itertools import permutations
import json
from pathlib import Path


states = tuple(range(3))
identity = (0, 1, 2)
hidden_swap = (0, 2, 1)
move_probe = (1, 0, 2)


def compose(left, right):
    return tuple(left[right[x]] for x in states)


def agrees(left, right, domain):
    return all(left[x] == right[x] for x in domain)


domain = (0,)
assert agrees(identity, hidden_swap, domain)
assert not agrees(compose(identity, move_probe), compose(hidden_swap, move_probe), domain)

# Postcomposition preserves equality on the original domain for every left
# context, while unrestricted precomposition does not.
all_contexts = tuple(permutations(states))
assert all(
    agrees(compose(context, identity), compose(context, hidden_swap), domain)
    for context in all_contexts
)
assert any(
    not agrees(compose(identity, context), compose(hidden_swap, context), domain)
    for context in all_contexts
)


def saturation(contexts, seed_domain):
    return tuple(sorted({context[x] for context in contexts for x in seed_domain}))


full_saturation = saturation(all_contexts, domain)
assert full_saturation == states

fix_zero_contexts = tuple(context for context in all_contexts if context[0] == 0)
restricted_saturation = saturation(fix_zero_contexts, domain)
assert restricted_saturation == domain

# Equality on an invariant domain survives precomposition by every admitted
# restricted context.
assert all(
    agrees(compose(identity, context), compose(hidden_swap, context), domain)
    for context in fix_zero_contexts
)

result = {
    "schema": "marici.context-saturated-provenance-congruence.v1",
    "original_probe_domain": [0],
    "observational_equivalence_passes": True,
    "unrestricted_precomposition_congruence": False,
    "postcomposition_congruence": True,
    "full_context_saturation": list(full_saturation),
    "restricted_context_saturation": list(restricted_saturation),
    "restricted_precomposition_congruence": True,
    "claim_boundary": "compiler-safe provenance depends on recovery domain and admitted contexts",
    "status": "pass",
}

output = Path(__file__).resolve().parents[1] / "results" / "context-saturated-provenance-congruence.json"
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
