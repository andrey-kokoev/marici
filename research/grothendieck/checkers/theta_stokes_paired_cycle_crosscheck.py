"""Cross-check the post-Stokes paired cycle against the real source contour."""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE))

from theta_one_copy_orbit_factorization import one_copy


trace_result = json.loads(
    (ROOT / "research" / "grothendieck" / "results" / "theta-stokes-upward-thimble-trace.json").read_text(encoding="utf-8")
)
paired = trace_result["oriented_plus_pair_thimble_quadrature"]
paired_integral = complex(*paired["paired_integral"])
paired_barycenter = complex(*paired["paired_log_barycenter"])

a, b = 0.5, 6.03
data = [one_copy(label, a, b, 20000) for label in range(1, 9)]
direct_integral = sum((item[0] for item in data), 0j)
direct_derivative = sum((item[1] for item in data), 0j)
direct_barycenter = 2 * direct_derivative / direct_integral

result = {
    "parameters_a_b": [a, b],
    "paired_cycle_integral": [paired_integral.real, paired_integral.imag],
    "direct_real_contour_integral": [direct_integral.real, direct_integral.imag],
    "relative_integral_difference": abs(paired_integral - direct_integral) / abs(direct_integral),
    "paired_cycle_log_barycenter": [paired_barycenter.real, paired_barycenter.imag],
    "direct_real_contour_log_barycenter": [direct_barycenter.real, direct_barycenter.imag],
    "absolute_barycenter_difference": abs(paired_barycenter - direct_barycenter),
    "plus_orientation_supported": abs(paired_integral - direct_integral) / abs(direct_integral) < 1e-3,
    "interval_certified": False,
    "rh_proved_or_disproved": False,
}


if __name__ == "__main__":
    output = ROOT / "research" / "grothendieck" / "results" / "theta-stokes-paired-cycle-crosscheck.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
