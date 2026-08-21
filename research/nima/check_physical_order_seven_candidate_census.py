"""Bounded five-gate census of repository order-seven candidates.

This is an inventory audit, not a theorem excluding future C7 packets.  It
checks the exact D7 group action for the closest existing physical candidate
and records the first failed or unresolved realization gate in each current
sector.
"""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "research/nima/results/physical-order-seven-candidate-census.json"
N = 7


def compose(g, h):
    return tuple(g[h[i]] for i in range(N))


identity = tuple(range(N))
rotation = tuple((i + 1) % N for i in range(N))
reflection = tuple((-i) % N for i in range(N))


def power(g, exponent):
    out = identity
    for _ in range(exponent):
        out = compose(g, out)
    return out


def inverse(g):
    return power(g, next(k for k in range(1, 2 * N + 1)
                         if power(g, k) == identity) - 1)


def main():
    elements = []
    normal_forms = {}
    for parity in (0, 1):
        for exponent in range(N):
            g = power(rotation, exponent)
            if parity:
                g = compose(reflection, g)
            elements.append(g)
            normal_forms[g] = (exponent, parity)
    assert len(set(elements)) == 14

    # Parke--Taylor fixed-trivialization character.  The fully transported
    # cycle/cocycle pairing is functorial; this character is not a trace map.
    def pt_character(g):
        return (-1) ** (N * normal_forms[g][1])

    checks = 0
    commutators = set()
    for g in elements:
        for h in elements:
            assert pt_character(compose(g, h)) == pt_character(g) * pt_character(h)
            commutators.add(compose(compose(compose(g, h), inverse(g)), inverse(h)))
            checks += 1
    rotations = {power(rotation, k) for k in range(N)}
    assert commutators == rotations
    assert all(pt_character(g) == 1 for g in rotations)

    evidence = {
        "seven_point_scattering": [
            "src/ledger/20260813-42 Pairwise Trace Sectors and the Cyclic Transmutation Counit.md",
            "src/ledger/20260813-45 Strict Physical-Cut Coaction of the Transmutation Counit.md",
        ],
        "seven_point_string_control": [
            "research/nima/phase-i-string-disk-readout-d5.md",
            "research/nima/five-point-disk-reflection-pairing-correction.md",
        ],
        "abstract_C7": [
            "research/nima/results/prime-to-exponent-readout-operations.json",
        ],
    }
    for paths in evidence.values():
        for path in paths:
            assert (ROOT / path).exists(), path

    gates = [
        "source_finite_symmetry",
        "physical_fixed_or_supported_locus",
        "coherent_coefficient_action",
        "source_trace_or_readout",
        "nonzero_relative_totalization",
    ]
    candidates = [
        {
            "candidate": "seven-point planar scattering cyclic ordering",
            "sector": "scattering",
            "group": "C7",
            "gates": [True, True, True, False, None],
            "first_blocker": "source_trace_or_readout",
            "reason": (
                "Cyclic covariance through seven points is established, but "
                "the source identifies cyclic relabellings of one color-ordered "
                "object; it does not prescribe a seven-occurrence trace."
            ),
        },
        {
            "candidate": "seven-point disk dihedral ordering",
            "sector": "strings",
            "group": "D7 with rotation subgroup C7",
            "gates": [False, None, None, None, None],
            "first_blocker": "source_finite_symmetry",
            "reason": (
                "The formal D7 ordering audit has commutator subgroup C7 and "
                "rotations act trivially on the ordering character, but the "
                "repository does not serialize the seven-point disk "
                "cycle/cocycle packet needed to promote this control to a "
                "source-derived physical candidate."
            ),
        },
        {
            "candidate": "seven-site cyclic cosmological packet",
            "sector": "cosmology",
            "group": "C7",
            "gates": [False, None, None, None, None],
            "first_blocker": "source_finite_symmetry",
            "reason": "No source-derived seven-site C7 coefficient/physical packet is serialized in the current repository.",
        },
        {
            "candidate": "flavor order-seven phase descent",
            "sector": "flavor",
            "group": "C7",
            "gates": [False, None, None, None, None],
            "first_blocker": "source_finite_symmetry",
            "reason": "The admitted sparse flavor presentation group is S3^3; it supplies no element or cover of order seven.",
        },
        {
            "candidate": "radiative-gravity finite order-seven descent",
            "sector": "radiative gravity",
            "group": "C7 subgroup of a continuous rotation group",
            "gates": [False, None, None, None, None],
            "first_blocker": "source_finite_symmetry",
            "reason": "No distinguished finite C7 branch/occurrence packet or trace is source-defined; choosing a subgroup of a continuous symmetry is insufficient.",
        },
        {
            "candidate": "abstract cyclic arithmetic control",
            "sector": "arithmetic",
            "group": "C7",
            "gates": [True, False, None, None, None],
            "first_blocker": "physical_fixed_or_supported_locus",
            "reason": "The exact algebraic norm spectrum exists, but no sector-valued physical realization map is supplied.",
        },
    ]
    assert all(len(row["gates"]) == len(gates) for row in candidates)
    assert not any(all(value is True for value in row["gates"])
                   for row in candidates)

    out = {
        "schema": "marici.physical_order_seven_candidate_census.v1",
        "scope": "Existing repository packets in scattering, cosmology, strings, flavor, radiative gravity, plus one abstract arithmetic control.",
        "gate_order": gates,
        "candidate_count": len(candidates),
        "fully_typed_physical_C7_candidate_count": 0,
        "d7_exact_control": {
            "group_order": len(elements),
            "commutator_subgroup": "C7",
            "commutator_subgroup_order": len(commutators),
            "rotation_character": pt_character(rotation),
            "reflection_character": pt_character(reflection),
            "homomorphism_checks": checks,
            "interpretation": "formal ordering-character control, not a serialized physical seven-point disk packet",
        },
        "candidates": candidates,
        "conclusion": (
            "No existing source-derived physical packet realizes p=7. The "
            "closest serialized seven-point scattering candidate fails at "
            "the trace/readout gate; other sectors lack a distinguished "
            "physical C7 packet."
        ),
        "typing_boundary": (
            "This bounded zero is not a no-go theorem for future seven-site "
            "geometry or a new seven-sheeted physical cover."
        ),
        "evidence": evidence,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: out[key] for key in (
        "schema", "candidate_count", "fully_typed_physical_C7_candidate_count",
        "d7_exact_control", "conclusion", "typing_boundary")}, indent=2))


if __name__ == "__main__":
    main()
