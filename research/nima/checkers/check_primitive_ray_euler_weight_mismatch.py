from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/nima/results/primitive-ray-euler-weight-mismatch.json"
SOURCES = {
    "pushforward": "research/nima/results/coprime-ray-to-primitive-valuation-pushforward.json",
    "sign": "research/nima/results/primitive-ray-global-sign.json",
    "primitive": "research/voevodsky/a_second_position_graph_dual_functional_realizes_the_primitive_current_20260910.md",
    "global": "research/nima/results/global-forcing-reservoir-current-decomposition.json",
}


def main() -> None:
    raw = {name: (ROOT / path).read_text(encoding="utf-8") for name, path in SOURCES.items()}
    push = json.loads(raw["pushforward"])
    sign = json.loads(raw["sign"])
    global_result = json.loads(raw["global"])
    primes = [2, 3, 5, 7, 11, 13]
    ratios = {str(p): (math.log(p) / math.sqrt(p)) / math.log(p) for p in primes}
    checks = {
        "ray_pushforward_is_unweighted_valuation": push["pushforward"] == "P(a,b)=sum_{p} v_p(max(a,b)) c_(log p)",
        "ray_readout_is_log_max": "=log max(a,b)" in push["exact_identity"],
        "actual_primitive_row_has_half_density_weight": "(\\log p)p^{-1/2}" in raw["primitive"],
        "actual_synthesis_column_has_half_density_weight": "p^{-1/2}L_{\\rm prim}(c_{\\log p})" in raw["primitive"],
        "prime_dependent_ratios": len({round(v, 12) for v in ratios.values()}) == len(primes),
        "no_common_scalar_normalization": ratios["2"] != ratios["3"],
        "global_primitive_row_was_not_closed": global_result["coefficient_rows"][0]["equality"] == "open",
        "prior_sign_result_was_only_raywise": "raywise" in sign["status"],
    }
    assert all(checks.values())
    out = {
        "schema": "marici.nima.primitive-ray-euler-weight-mismatch.v1",
        "status": "primitive_equality_falsified_for_the_current_unweighted_ray_pushforward",
        "checks": checks,
        "ray_coefficient_on_max_equals_p": "log p",
        "declared_primitive_euler_row_on_p": "(log p)/sqrt(p)",
        "ratio_target_over_ray": ratios,
        "counterexample": "For the coprime ray (a,b)=(p,1), the constructed valuation pushforward reads log p, while the independently constructed Euler primitive row reads (log p)/sqrt(p). Their ratio p^(-1/2) depends on p.",
        "conclusion": "The existing source normalization does not give coefficientwise equality. Orientation, odd-endpoint normalization, and the two-height Laplace sign cannot repair the missing p^(-1/2) Euler weight.",
        "supersedes": [
            "The primitive_match claim in research/nima/results/barnes-odd-endpoint-primitive-normalization.json when interpreted as equality with the Euler-synthesized row.",
            "The exact arithmetic-current interpretation in research/nima/results/coprime-ray-to-primitive-valuation-pushforward.json; that file proves only the unweighted identity log(max)=sum v_p log p.",
            "Any suggestion in research/nima/results/primitive-ray-global-sign.json that sign closure suffices for the global k=1 row."
        ],
        "repair_gate": "Construct independently and justify a typed source map that contributes sqrt(p) to the p-labelled ray packet before Euler synthesis, or change the ray pushforward to an authorized half-density-weighted map. Without such a map the k=1 equality is false.",
        "objective_disposition": "falsified under the currently declared source normalization",
        "artifacts_sha256": {name: hashlib.sha256((ROOT / path).read_bytes()).hexdigest() for name, path in SOURCES.items()},
        "passed": True,
        "rh_implication": False,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
