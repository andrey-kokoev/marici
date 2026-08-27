from fractions import Fraction as F
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "correlated_phase_relational_rescue.json"


def moments(law):
    ex = sum(p * x for (x, _), p in law.items())
    ey = sum(p * y for (_, y), p in law.items())
    exy = sum(p * x * y for (x, y), p in law.items())
    covariance = exy - ex * ey
    return ex, ey, exy, covariance


def main():
    laws = {
        "independent_unbiased": {
            (1, 1): F(1, 4), (1, -1): F(1, 4),
            (-1, 1): F(1, 4), (-1, -1): F(1, 4),
        },
        "perfectly_correlated_unbiased": {(1, 1): F(1, 2), (-1, -1): F(1, 2)},
        "perfectly_anticorrelated_unbiased": {(1, -1): F(1, 2), (-1, 1): F(1, 2)},
        "independent_biased": {
            (1, 1): F(9, 16), (1, -1): F(3, 16),
            (-1, 1): F(3, 16), (-1, -1): F(1, 16),
        },
    }
    result = {}
    for name, law in laws.items():
        ex, ey, exy, covariance = moments(law)
        result[name] = {
            "kappa_A": str(ex), "kappa_B": str(ey),
            "joint_phase_factor": str(exy),
            "local_product": str(ex * ey), "covariance": str(covariance),
        }

    assert moments(laws["independent_unbiased"]) == (F(0), F(0), F(0), F(0))
    assert moments(laws["perfectly_correlated_unbiased"]) == (F(0), F(0), F(1), F(1))
    assert moments(laws["perfectly_anticorrelated_unbiased"]) == (F(0), F(0), F(-1), F(-1))
    assert moments(laws["independent_biased"]) == (F(1, 2), F(1, 2), F(1, 4), F(0))

    out = {
        "schema": "marici.aspect.correlated-phase-relational-rescue.v1",
        "status": "pass", "cases": result,
        "corrected_law": "V_joint = gamma*s*E[X_A X_B], not generally gamma*s*E[X_A]*E[X_B]",
        "surprise": "both local coherence factors can vanish while the joint relational visibility is full",
        "discriminator": "measure the joint phase-flip census or covariance in the same epoch before applying the product-law falsifier",
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
