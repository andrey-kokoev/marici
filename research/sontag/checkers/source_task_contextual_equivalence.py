"""Exact test of source-task equivalence relative to authorized future contexts."""

import json
from pathlib import Path


PRESENTATIONS = ("target0_a", "target0_b", "target1")
TARGET = {"target0_a": 0, "target0_b": 0, "target1": 1}
PLANT_STATE = 0


def coarse_readout(_presentation):
    return 0


def replay_readout(presentation):
    return int(TARGET[presentation] == PLANT_STATE)


def signature(presentation, contexts):
    outputs = []
    for context in contexts:
        if context == "coarse":
            outputs.append((context, coarse_readout(presentation)))
        elif context == "replay":
            outputs.append((context, replay_readout(presentation)))
    return tuple(outputs)


def partition(contexts):
    fibers = {}
    for presentation in PRESENTATIONS:
        fibers.setdefault(signature(presentation, contexts), []).append(presentation)
    return tuple(sorted(tuple(group) for group in fibers.values()))


def extension_descends(old_contexts, new_context):
    for group in partition(old_contexts):
        outputs = {
            replay_readout(presentation) if new_context == "replay" else coarse_readout(presentation)
            for presentation in group
        }
        if len(outputs) != 1:
            return False
    return True


def main():
    current = ("coarse",)
    completed = ("coarse", "replay")
    current_partition = partition(current)
    completed_partition = partition(completed)
    checks = {
        "all_presentations_agree_in_current_context": len(current_partition) == 1,
        "target_zero_and_target_one_are_currently_equivalent": signature("target0_a", current) == signature("target1", current),
        "authorized_replay_separates_target_zero_from_target_one": replay_readout("target0_a") != replay_readout("target1"),
        "replay_extension_does_not_descend_to_current_quotient": not extension_descends(current, "replay"),
        "completed_context_partition_has_two_classes": len(completed_partition) == 2,
        "duplicate_target_zero_presentations_remain_equivalent": signature("target0_a", completed) == signature("target0_b", completed),
        "completed_partition_separates_only_task_relevant_difference": completed_partition == (("target0_a", "target0_b"), ("target1",)),
        "replay_descends_after_contextual_refinement": extension_descends(completed, "replay"),
    }
    payload = {
        "schema": "marici.sontag.source_task_contextual_equivalence.v1",
        "passed": sum(checks.values()),
        "total": len(checks),
        "all_passed": all(checks.values()),
        "checks": checks,
        "current_partition": current_partition,
        "completed_partition": completed_partition,
        "verdict": (
            "Source-task identity is relative to the authorized future-context family. "
            "Current coarse behavior quotients incompatible tasks, but a source-authorized "
            "replay extension fails to descend and forces refinement. Duplicate presentations "
            "of the same task remain quotiented. A source boundary is intrinsic exactly to the "
            "extent required by a jointly conservative continuation family."
        ),
    }
    output = Path(__file__).parents[1] / "results" / "source_task_contextual_equivalence.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    raise SystemExit(0 if payload["all_passed"] else 1)


if __name__ == "__main__":
    main()
