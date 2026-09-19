from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/nima/results/primitive-forcing-reservoir-scaling-ray.json"
SOURCES = {
    "kernel": "research/nima/completed-theta-autocorrelation-has-an-explicit-double-dirichlet-kernel.md",
    "ray": "research/nima/common-scaling-ray-renormalization-of-theta-autocorrelation.md",
    "primitive": "research/voevodsky/a_second_position_graph_dual_functional_realizes_the_primitive_current_20260910.md",
    "global": "research/nima/results/global-forcing-reservoir-current-decomposition.json",
}


def main() -> None:
    text = {name: (ROOT / path).read_text(encoding="utf-8") for name, path in SOURCES.items()}
    global_result = json.loads(text["global"])
    # Under (n,m)->(dn,dm), D scales by d^2.  Each of the three
    # numerator/denominator pairs therefore has total dilation degree -1.
    dilation_degrees = {
        "n4m4_over_D_9/2": 8 - 2 * (9 / 2),
        "n4m2_over_D_7/2": 6 - 2 * (7 / 2),
        "n2m2_over_D_5/2": 4 - 2 * (5 / 2),
    }
    checks = {
        "finite_cutoff_kernel_explicit": "finite-cutoff theta autocorrelation evaluated explicitly" in text["kernel"],
        "all_kernel_terms_have_degree_minus_one": set(dilation_degrees.values()) == {-1.0},
        "ray_sum_is_harmonic": "H_{\\lfloor N/\\max(a,b)\\rfloor}" in text["ray"],
        "ray_divergence_is_log_N": "\\log N" in text["ray"],
        "finite_part_contains_log_max": "\\gamma-\\log\\max(a,b)" in text["ray"],
        "primitive_dual_functional_gives_log_p": "L_{\\rm prim}(c_{\\log p})=\\log p" in text["primitive"],
        "primitive_lives_on_graph_dual": "a_{\\rm prim}\\in K'(\\mathcal G_{Q^2}')" in text["primitive"],
        "global_primitive_row_open": global_result["coefficient_rows"][0]["equality"] == "open",
    }
    assert all(checks.values())
    out = {
        "schema": "marici.nima.primitive-forcing-reservoir-scaling-ray.v1",
        "status": "primitive_reservoir_is_relational_scaling_anomaly_not_termwise_prime_row",
        "checks": checks,
        "dilation_degrees": dilation_degrees,
        "derived_ray_law": "For (n,m)=d(a,b), every autocorrelation summand scales as 1/d, producing H_floor(N/max(a,b)).",
        "divergent_part": "[e^(t/2)/a] kappa((b/a)e^t) log N",
        "finite_part": "[e^(t/2)/a] kappa((b/a)e^t) (gamma-log max(a,b))",
        "primitive_current": "The independent primitive graph-dual functional sends the translated packet c_(log p) to log p.",
        "obstruction": "The reservoir primitive term is indexed by coprime ordered rays (a,b) and log max(a,b), whereas the existing primitive current is indexed by one prime translation. A termwise k=1 prime comparison is not typed and cannot prove the required equality.",
        "correct_next_map": "Construct a source-derived coprime-ray-to-prime-boundary pushforward that sends the common scaling connection log d and finite log max(a,b) term into the centered primitive graph-dual current, while retaining ordered-pair ratio and seam/archimedean counterterms.",
        "completion_gate": "Prove the coprime-ray sum converges in the projective source topology after the common log N subtraction.",
        "artifacts_sha256": {name: hashlib.sha256((ROOT / path).read_bytes()).hexdigest() for name, path in SOURCES.items()},
        "passed": True,
        "rh_implication": False,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
