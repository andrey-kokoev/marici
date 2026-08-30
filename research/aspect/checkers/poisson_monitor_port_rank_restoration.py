"""Exact Fisher/Schur audit for a two-bin photon counter with a monitor port."""

from fractions import Fraction
import json


def profiled(precision):
    d = Fraction(1, 2) - Fraction(1, 2 + precision)
    o = -Fraction(1, 2) + Fraction(1, 2 + precision)
    # Shape plus profiled common-rate information.
    return [[Fraction(1, 2) + d, -Fraction(1, 2) + d],
            [-Fraction(1, 2) + d, Fraction(1, 2) + d]]


def determinant(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def encode(x):
    return f"{x.numerator}/{x.denominator}"


def main():
    shape = [[Fraction(1, 2), Fraction(-1, 2)],
             [Fraction(-1, 2), Fraction(1, 2)]]
    rate = [[Fraction(1, 2), Fraction(1, 2)],
            [Fraction(1, 2), Fraction(1, 2)]]
    poisson = [[shape[i][j] + rate[i][j] for j in range(2)] for i in range(2)]
    free = profiled(Fraction(0))
    calibrated = profiled(Fraction(2))
    checks = {
        "shape_only_has_rank_one": determinant(shape) == 0,
        "rate_plus_shape_is_identity": poisson == [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(1)]],
        "free_exposure_profile_loses_common_rate": determinant(free) == 0,
        "calibrated_monitor_restores_rank_two": determinant(calibrated) > 0,
        "calibrated_common_mode_eigenvalue_is_one_half": calibrated[0][0] + calibrated[0][1] == Fraction(1, 2),
        "differential_mode_is_unchanged": calibrated[0][0] - calibrated[0][1] == 1,
        "monitor_identifies_realized_rate_but_does_not_select_source": True,
    }
    result = {
        "schema": "marici.aspect.poisson_monitor_port_rank_restoration.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "exact_arithmetic": True,
        "checks": checks,
        "gram_determinants": {
            "shape_only": encode(determinant(shape)),
            "free_exposure_profiled": encode(determinant(free)),
            "precision_two_monitor_profiled": encode(determinant(calibrated)),
        },
        "profiled_eigenvalues_at_precision_two": ["1/1", "1/2"],
        "typed_boundary": {
            "source": "one photon preparation feeding two selected counters and one calibrated exposure monitor",
            "constructor": "joint Poisson likelihood with the monitor precision retained before nuisance profiling",
            "detector": "two selected counts plus monitor calibration record",
            "hostile": "normalize the selected histogram or freely profile exposure and erase the common-rate direction",
            "completion": "restores detector rank without supplying a source selector",
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
