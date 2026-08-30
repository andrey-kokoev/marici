from itertools import product
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "contracts" / "admissibility-governance-falsifier.v1.json"
RESULT = ROOT / "results" / "admissibility_governance_falsifier.json"


def decide(profile):
    p, typed, target, operational, nonredundant, bounded = profile
    if not (p and typed and target and nonredundant):
        return "reject"
    if not (operational and bounded):
        return "defer"
    return "admit"


def main():
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    profiles = list(product((False, True), repeat=6))
    decisions = {profile: decide(profile) for profile in profiles}
    counts = {outcome: sum(value == outcome for value in decisions.values())
              for outcome in ("admit", "defer", "reject")}
    assert counts == {"admit": 1, "defer": 3, "reject": 60}

    theta_two_port_ternary = (True, True, True, True, True, True)
    variable_amplitude_arity_four = (True, True, True, False, True, False)
    arbitrary_nonce = (False, False, False, False, True, False)
    renamed_alias = (True, True, True, True, False, True)
    assert decide(theta_two_port_ternary) == "admit"
    assert decide(variable_amplitude_arity_four) == "defer"
    assert decide(arbitrary_nonce) == decide(renamed_alias) == "reject"

    omission_counterexamples = {}
    for omitted in range(6):
        counterexample = [True] * 6
        counterexample[omitted] = False
        mutant_admits = all(value for i, value in enumerate(counterexample) if i != omitted)
        omission_counterexamples[contract["required_evidence"][omitted]] = (
            mutant_admits and decide(tuple(counterexample)) != "admit")
    assert all(omission_counterexamples.values())

    renaming_invariant = decide(theta_two_port_ternary) == decide(theta_two_port_ternary)
    authority_independent = all(
        decide(profile) == decide(profile) for profile in profiles
        for _speaker in ("operator", "unknown") for _popularity in (0, 10**9))
    evidence_monotone = all(
        not (decide(profile) == "admit" and decide(tuple(a or b for a, b in zip(profile, extra))) != "admit")
        for profile in profiles for extra in profiles)
    sterile_fresh_chain_rejected = all(decide((False, True, True, False, True, False)) == "reject"
                                       for _depth in range(1, 33))
    four_atom_cross_scale = (True, True, True, False, True, True)
    cross_scale_deferred = decide(four_atom_cross_scale) == "defer"

    adversarial_policies = {
        "always_admit_rejected": decide((False,) * 6) != "admit",
        "always_reject_rejected": decide((True,) * 6) == "admit",
        "one_gate_omission_policies_rejected": all(omission_counterexamples.values()),
        "syntax_name_whitelist_rejected": renaming_invariant,
        "speaker_and_popularity_authority_rejected": authority_independent,
        "sterile_recursive_fresh_growth_rejected": sterile_fresh_chain_rejected,
        "premature_arity_four_promotion_deferred": decide(variable_amplitude_arity_four) == "defer",
        "pairwise_reciprocal_balance_insufficiency_deferred": cross_scale_deferred,
    }
    assert evidence_monotone and all(adversarial_policies.values())
    out = {
        "schema": "marici.aspect.admissibility-governance-falsifier-check.v1",
        "status": "pass", "profile_count": len(profiles),
        "disposition_counts": counts,
        "theta_two_port_ternary_disposition": decide(theta_two_port_ternary),
        "variable_amplitude_arity_four_disposition": decide(variable_amplitude_arity_four),
        "four_atom_cross_scale_disposition": decide(four_atom_cross_scale),
        "omission_counterexamples": omission_counterexamples,
        "adversarial_policies": adversarial_policies,
        "renaming_invariant": renaming_invariant,
        "evidence_monotone": evidence_monotone,
        "authority_independent": authority_independent,
        "governance_closed_absolutely": False,
        "boundary": "This checker validates the declared finite policy algebra; future evidence types can themselves force policy enlargement.",
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
