"""Weak finite control test separating repair from reset-based erasure."""

import json
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Packet:
    source: tuple | None
    realization: tuple
    repair_capacity: int
    original_obligations: int


def weighted_defect(packet):
    if packet.source is None:
        return 2 * packet.original_obligations
    return sum(expected != actual for expected, actual in zip(packet.source, packet.realization))


def margin(packet):
    return packet.repair_capacity - weighted_defect(packet)


def repair(packet):
    if packet.source is None:
        return None
    return Packet(packet.source, packet.source, packet.repair_capacity, packet.original_obligations)


def reset_erase(packet):
    return Packet(None, tuple(0 for _ in packet.realization), packet.repair_capacity, packet.original_obligations)


def propose_generation(packet, target, realized):
    if packet.source is None:
        return None
    proposal = Packet(
        packet.source + (target,),
        packet.realization + (realized,),
        packet.repair_capacity,
        packet.original_obligations + 1,
    )
    return proposal if margin(proposal) >= 0 else None


def target_replay(packet, index):
    if packet.source is None:
        return None
    return packet.realization[index] == packet.source[index]


def main():
    initial = Packet(source=(1,), realization=(0,), repair_capacity=1, original_obligations=1)
    repaired = repair(initial)
    erased = reset_erase(initial)
    hostile_growth = propose_generation(initial, target=1, realized=0)
    repaired_growth = propose_generation(repaired, target=1, realized=0)
    erased_growth = propose_generation(erased, target=1, realized=0)

    checks = {
        "initial_margin_is_exactly_zero": margin(initial) == 0,
        "unrepaired_faulty_growth_is_rejected": hostile_growth is None,
        "repair_uses_source_reference": repaired.realization == initial.source,
        "repair_preserves_source": repaired.source == initial.source,
        "repair_restores_positive_margin": margin(repaired) == 1,
        "one_fault_growth_after_repair_is_admitted": repaired_growth is not None,
        "admitted_growth_ends_at_zero_margin": margin(repaired_growth) == 0,
        "reset_makes_visible_bits_zero": erased.realization == (0,),
        "reset_erases_the_reference": erased.source is None,
        "weighted_audit_counts_erasure_as_defect": weighted_defect(erased) == 2,
        "reset_has_negative_true_margin": margin(erased) == -1,
        "reset_cannot_authorize_new_generation": erased_growth is None,
        "repair_passes_original_target_replay": target_replay(repaired, 0) is True,
        "reset_cannot_even_state_target_replay": target_replay(erased, 0) is None,
    }
    payload = {
        "schema": "marici.sontag.source_derived_repair_margin.v1",
        "passed": sum(checks.values()),
        "total": len(checks),
        "all_passed": all(checks.values()),
        "checks": checks,
        "margins": {
            "initial": margin(initial),
            "repaired": margin(repaired),
            "erased": margin(erased),
            "repaired_then_grown": margin(repaired_growth),
        },
        "verdict": (
            "Generative command capacity may increase only when the post-command weighted "
            "defect margin remains nonnegative. Reset-based erasure is not repair: it deletes "
            "the source reference required for replay, incurs a lost-obligation defect, and "
            "cannot authorize subsequent generation."
        ),
    }
    output = Path(__file__).parents[1] / "results" / "source_derived_repair_margin.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    raise SystemExit(0 if payload["all_passed"] else 1)


if __name__ == "__main__":
    main()
