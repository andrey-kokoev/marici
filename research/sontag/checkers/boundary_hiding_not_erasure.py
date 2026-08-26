import itertools
import json
from pathlib import Path


open_states = tuple(itertools.product((0, 1), repeat=2))
closed_states = (0, 1)


def q(state):
    system, _memory = state
    return system


def recall(state):
    _system, memory = state
    return memory, memory


def system_flip(state):
    system, memory = state
    return 1 - system, memory


sections = []
for memory_for_zero, memory_for_one in itertools.product((0, 1), repeat=2):
    section = {
        0: (0, memory_for_zero),
        1: (1, memory_for_one),
    }
    sections.append(section)


def is_right_inverse(section):
    return all(q(section[state]) == state for state in closed_states)


def is_left_inverse(section):
    return all(section[q(state)] == state for state in open_states)


def descends(action):
    for left in open_states:
        for right in open_states:
            if q(left) == q(right) and q(action(left)) != q(action(right)):
                return False
    return True


checks = {
    "projection_has_four_sections": len(sections) == 4,
    "every_section_is_a_right_inverse": all(
        is_right_inverse(section) for section in sections
    ),
    "no_section_is_a_left_inverse": not any(
        is_left_inverse(section) for section in sections
    ),
    "restricted_state_does_not_select_a_section": len(
        {tuple(section.items()) for section in sections}
    )
    == 4,
    "system_only_flip_descends": descends(system_flip),
    "memory_recall_does_not_descend": not descends(recall),
    "recall_separates_one_projection_fiber": q((0, 0)) == q((0, 1))
    and q(recall((0, 0))) != q(recall((0, 1))),
}

result = {
    "status": "PASS" if all(checks.values()) else "FAIL",
    "checks": checks,
    "sections": [
        {str(state): list(image) for state, image in section.items()}
        for section in sections
    ],
    "classification": {
        "hiding": "restricts accessible Tasks while retaining the open Carrier state",
        "erasure": "quotients the Carrier and has no state-recovering inverse",
        "section": "prepares a chosen replacement fiber coordinate",
        "revelation": "restores access only when the latent coordinate was retained",
    },
}

output = Path(__file__).parents[1] / "results" / "boundary_hiding_not_erasure.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

