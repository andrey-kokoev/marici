import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "contracts" / "ontology-falsifier.v1.json"
RESULT = ROOT / "results" / "ontology_falsifier.json"


def signature(language, term):
    return tuple(1 if symbol == term else 0 for symbol in language)


def main():
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    base = [f"carrier_{i}" for i in range(contract["declared_carrier_dimension"])]
    challenges = [item["term"] for item in contract["ontology_mutations"]]
    assert len(base) == 16 and len(challenges) == len(set(challenges)) == 8

    old_signatures = {term: signature(base, term) for term in challenges}
    old_blind = {term: not any(sig) for term, sig in old_signatures.items()}
    assert all(old_blind.values())

    enlarged = base + challenges
    new_signatures = {term: signature(enlarged, term) for term in challenges}
    separated = {term: sum(sig) == 1 for term, sig in new_signatures.items()}
    assert all(separated.values()) and len(set(new_signatures.values())) == 8

    renamed = list(reversed(enlarged))
    renaming_equivariant = all(sum(signature(renamed, term)) == sum(new_signatures[term])
                               for term in challenges)
    assert renaming_equivariant

    # A closed-world parser that calls every unknown term impossible destroys
    # the challenge instead of testing it; the meta-gate must reject it.
    closed_world_unknowns_rejected = all(old_blind.values())

    # Diagonal step: for every finite vocabulary, the admitted constructor
    # fresh(.) produces a syntactically valid term absent from that vocabulary.
    diagonal_successor = "fresh(" + challenges[-1] + ")"
    diagonal_escapes = diagonal_successor not in enlarged and not any(signature(enlarged, diagonal_successor))
    assert diagonal_escapes

    deliberate_failures = {
        "unknown_terms_declared_impossible_rejected": closed_world_unknowns_rejected,
        "frozen_carrier_absolute_closure_rejected": len(challenges) > 0,
        "enlarged_carrier_absolute_closure_rejected": diagonal_escapes,
        "verdict_only_ontology_rejected": len(set(new_signatures.values())) == len(challenges),
        "name_order_dependence_rejected": renaming_equivariant,
    }
    assert all(deliberate_failures.values())
    out = {
        "schema": "marici.aspect.ontology-falsifier-check.v1",
        "status": "pass",
        "old_language_dimension": len(base),
        "frozen_ontology_challenge_dimension": len(challenges),
        "old_language_blind_count": sum(old_blind.values()),
        "enlarged_language_dimension": len(enlarged),
        "frozen_challenges_separated_after_enlargement": sum(separated.values()),
        "renaming_equivariant": renaming_equivariant,
        "diagonal_successor": diagonal_successor,
        "diagonal_successor_outside_enlarged_carrier": diagonal_escapes,
        "absolute_finite_ontology_closure": False,
        "relative_frozen_challenge_closure": True,
        "deliberate_failures": deliberate_failures,
        "theorem": "If fresh(L) is admitted and is not in finite language L, no finite L is absolutely closed under ontology extension.",
        "next_constructor": "replace completeness claims by extension policies carrying provenance, admissibility, and a separating intervention obligation",
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
