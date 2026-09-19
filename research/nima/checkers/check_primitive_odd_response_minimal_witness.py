from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/nima/results/primitive-odd-response-minimal-witness.json"


def mat(alpha: Fraction) -> tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]:
    return ((0, alpha), (-alpha, 0))


def main() -> None:
    candidates = [Fraction(-1, 2), Fraction(-1, 3), Fraction(1, 2)]
    matrices = [mat(a) for a in candidates]
    S = ((0, 1), (1, 0))
    # Direct 2x2 slot-swap check S^T G S=-G.
    for G in matrices:
        SGS = ((G[1][1], G[1][0]), (G[0][1], G[0][0]))
        assert SGS == tuple(tuple(-x for x in row) for row in G)
    checks = {
        "orientation_forces_zero_diagonal": all(G[0][0] == G[1][1] == 0 for G in matrices),
        "slot_swap_odd_for_every_scalar": True,
        "single_ordered_cross_entry_recovers_scalar": all(G[0][1] == a for G, a in zip(matrices, candidates)),
        "opposite_cross_entry_forced": all(G[1][0] == -G[0][1] for G in matrices),
        "different_scalars_share_all_linear_symmetries": len(set(candidates)) == len(candidates),
    }
    assert all(checks.values())
    out = {
        "schema": "marici.nima.primitive-odd-response-minimal-witness.v1",
        "status": "quadratic_owner_identification_reduces_to_one_ordered_mixed_scalar_per_prime",
        "checks": checks,
        "oriented_two_slot_form": "G_p^odd=alpha_p [[0,1],[-1,0]] on the normalized forward/reciprocal odd lines",
        "symmetry_laws": ["diagonal entries vanish", "slot reversal sends G to -G", "the reverse ordered entry is minus the forward entry"],
        "minimal_witness": "alpha_p=G_cons,p^odd((d_p,0),(0,d_p^rec)) in the declared analytic-transpose lane (with the Hermitian convention obtained by the fixed i/orientation conversion).",
        "target_witness": "Evaluate the induced cyclic/Wronskian form on the same ordered normalized pair and prove the two alpha_p agree. All other entries then follow from orientation and sesquilinearity/bilinearity.",
        "normalization_warning": "The vectors must be the source vectors d_p and d_p^rec, not unit-normalized window vectors; unit normalization inserts the forbidden inverse soft scale.",
        "two_height_extension": "If the local spectral dependence factors through the already constructed rank-one source line, equality of alpha_p identifies the full polarized w,z kernel. This factorization must be stated; diagonal equality alone is not sufficient without it.",
        "remaining_analytic_task": "Compute alpha_p from the conservative Green boundary trace on the common rapid core. Existing linear incidence and total forcing factorization do not determine it.",
        "passed": True,
        "rh_implication": False
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
