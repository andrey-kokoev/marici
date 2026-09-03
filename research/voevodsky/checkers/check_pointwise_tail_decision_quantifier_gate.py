from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


CONTRACT = Path("research/voevodsky/pointwise-tail-decision-quantifier-gate-v1.json")


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))

    # Packet rank r has limiting margin 1/r and tail radius r/N.
    # Every r has a cutoff, but the least integer cutoff grows as r^2+1.
    ranks = range(1, 17)
    cutoffs = []
    for r in ranks:
        cutoff = r * r + 1
        assert sp.Rational(r, cutoff) < sp.Rational(1, r)
        assert sp.Rational(r, cutoff - 1) >= sp.Rational(1, r)
        cutoffs.append(cutoff)
    assert cutoffs == sorted(cutoffs) and len(set(cutoffs)) == len(cutoffs)

    # Every proposed uniform cutoff fails for a sufficiently large packet.
    for uniform_cutoff in range(1, 65):
        r = sp.ceiling(sp.sqrt(uniform_cutoff))
        assert sp.Rational(r, uniform_cutoff) >= sp.Rational(1, r)

    # Repeated labels create a presentation kernel; quotienting removes it.
    repeated_gram = sp.Matrix([[1, 1], [1, 1]])
    assert repeated_gram.det() == 0
    assert repeated_gram.rank() == 1
    quotient_gram = sp.Matrix([[1]])
    assert quotient_gram.is_positive_definite

    # A finite distinct-label fixture can be strictly positive without proving the general claim.
    features = sp.Matrix([[1, 1], [1, 2]])
    distinct_gram = features.T * features
    assert distinct_gram.det() > 0 and distinct_gram.is_positive_definite

    status = contract["status"]
    assert status["unconditional_all_packet_termination"] == "not supplied"
    result = {
        "schema":"marici.voevodsky.pointwise-tail-decision-quantifier-gate-check.v1",
        "status":"pointwise_nonuniform_quantifier_verified",
        "packet_ranks_checked":len(list(ranks)),
        "pointwise_cutoffs_exist":True,
        "uniform_cutoff_refuted_in_fixture":True,
        "repeated_label_presentation_kernel":True,
        "quotient_removes_fixture_kernel":True,
        "conditional_zeta_zero_argument_verified":False,
        "unconditional_all_packet_termination":False,
        "rh_implication":False,
        "acceptance_test":contract["acceptance_test"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
