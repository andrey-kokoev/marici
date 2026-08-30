"""Exact Boolean test of source-counterfactual explanatory rigidity."""

import itertools
import json
from pathlib import Path


STATES = tuple(itertools.product((0, 1), repeat=2))  # (source, realization)
MECHANISMS = tuple(itertools.product((0, 1), repeat=2))  # f(0), f(1)


def act(mechanism, state):
    source, _realization = state
    return source, mechanism[source]


def replay(state):
    source, realization = state
    return source == realization


def source_flip(state):
    source, realization = state
    return 1 - source, 1 - realization


def fits_actual_case(mechanism):
    return replay(act(mechanism, (1, 0)))


def repairs_source_family(mechanism):
    return all(replay(act(mechanism, (source, realization))) for source, realization in STATES)


def commutes_with_source_flip(mechanism):
    return all(
        act(mechanism, source_flip(state)) == source_flip(act(mechanism, state))
        for state in STATES
    )


def preserves_predicate(mechanism, predicate):
    return all(predicate[STATES.index(act(mechanism, state))] == predicate[STATES.index(state)] for state in STATES)


def main():
    actual_fitters = tuple(m for m in MECHANISMS if fits_actual_case(m))
    family_repairs = tuple(m for m in MECHANISMS if repairs_source_family(m))
    natural_actual_fitters = tuple(m for m in actual_fitters if commutes_with_source_flip(m))
    constant_predicate = (0, 0, 0, 0)

    identity = (0, 1)
    lookup_one = (1, 1)
    checks = {
        "actual_case_has_two_rival_mechanisms": set(actual_fitters) == {identity, lookup_one},
        "lookup_one_passes_actual_replay": fits_actual_case(lookup_one),
        "lookup_one_fails_source_zero_counterfactual": not replay(act(lookup_one, (0, 1))),
        "identity_repairs_both_source_values": repairs_source_family(identity),
        "source_family_replay_selects_identity_uniquely": family_repairs == (identity,),
        "identity_commutes_with_source_flip": commutes_with_source_flip(identity),
        "lookup_one_breaks_source_flip_naturality": not commutes_with_source_flip(lookup_one),
        "actual_fit_plus_naturality_selects_identity": natural_actual_fitters == (identity,),
        "arbitrary_constant_predicate_certifies_lookup": preserves_predicate(lookup_one, constant_predicate),
        "arbitrary_constant_predicate_certifies_every_mechanism": all(
            preserves_predicate(m, constant_predicate) for m in MECHANISMS
        ),
    }
    payload = {
        "schema": "marici.sontag.source_counterfactual_explanatory_rigidity.v1",
        "passed": sum(checks.values()),
        "total": len(checks),
        "all_passed": all(checks.values()),
        "checks": checks,
        "mechanism_table": {
            "all": MECHANISMS,
            "actual_case_fitters": actual_fitters,
            "source_family_repairs": family_repairs,
            "actual_fit_and_source_natural": natural_actual_fitters,
        },
        "verdict": (
            "Actual-case replay and arbitrary invariant predicates underdetermine mechanism. "
            "Source-derived replay across the admitted counterfactual family, equivalently "
            "actual fit plus source-flip naturality in this Boolean model, uniquely selects "
            "the relational corrector y:=s over the lookup rival y:=1."
        ),
    }
    output = Path(__file__).parents[1] / "results" / "source_counterfactual_explanatory_rigidity.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    raise SystemExit(0 if payload["all_passed"] else 1)


if __name__ == "__main__":
    main()
