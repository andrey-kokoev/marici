import json
from pathlib import Path


def machine(depth):
    states = [(side, level) for side in (0, 1) for level in range(depth + 2)]

    def output(state):
        side, level = state
        return side if level == depth + 1 else 0

    def step(state):
        side, level = state
        return side, min(level + 1, depth + 1)

    return states, output, step


def refine(states, output, step):
    partition = {state: output(state) for state in states}
    rounds = 0
    while True:
        signatures = {state: (partition[state], partition[step(state)]) for state in states}
        unique = {signature: i for i, signature in enumerate(sorted(set(signatures.values())))}
        successor = {state: unique[signatures[state]] for state in states}
        rounds += 1
        if all((partition[a] == partition[b]) == (successor[a] == successor[b])
               for a in states for b in states):
            return successor, rounds
        partition = successor


fixtures = []
for depth in range(7):
    states, output, step = machine(depth)
    left, right = (0, 0), (1, 0)
    cursor_left, cursor_right = left, right
    finite_agreement = True
    for _ in range(depth + 1):
        finite_agreement &= output(cursor_left) == output(cursor_right)
        cursor_left, cursor_right = step(cursor_left), step(cursor_right)
    separating_outputs = [output(cursor_left), output(cursor_right)]
    partition, rounds = refine(states, output, step)
    assert finite_agreement
    assert separating_outputs == [0, 1]
    assert partition[left] != partition[right]
    fixtures.append({
        "tested_horizon": depth,
        "agreement_through_horizon": finite_agreement,
        "separated_at_word_length": depth + 1,
        "partition_refinement_rounds": rounds,
        "greatest_behavioral_equivalence_separates_sources": True,
    })

result = {
    "schema": "marici.nima.contextual-equivalence-stabilization.v1",
    "fixtures": fixtures,
    "fixture_count": len(fixtures),
    "verdict": "Source-task presentations may be quotiented only by equivalence under the full authorized context closure, certified by a stabilized congruent partition; bounded observations alone are insufficient."
}

out = Path(__file__).parents[1] / "results" / "contextual-equivalence-stabilization.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
