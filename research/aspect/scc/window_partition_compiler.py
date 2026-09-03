"""Typed source-gate compiler for periodic localization windows and covers."""
from fractions import Fraction

SCHEMA = "marici.scc.window-partition.v2"


def F(value):
    return Fraction(str(value))


def fail(gate, reason, **evidence):
    return {"schema": SCHEMA, "passed": False, "first_failed_gate": gate,
            "reason": reason, "evidence": evidence}


def _budget(spec):
    kind = spec.get("kind", "exact_quadratic_surd")
    if kind == "exact_quadratic_surd":
        coefficient = F(spec["coefficient"])
        radicand = int(spec.get("radicand", 1))
        if coefficient < 0 or radicand < 1:
            raise ValueError("inadmissible exact quadratic-surd budget")
        return {"kind": kind, "coefficient": coefficient, "radicand": radicand,
                "direction": "equality", "provenance": spec.get("provenance", {})}
    if kind == "directed_dyadic_upper":
        required = ("hex_endpoint", "direction", "cell_count", "backend",
                    "checker_locator", "result_locator", "aggregation_rule")
        missing = [key for key in required if not spec.get(key)]
        if missing or spec.get("direction") != "upper" or spec.get("aggregation_rule") != "upper_darboux":
            raise ValueError("malformed directed dyadic upper budget: " + ",".join(missing))
        endpoint = Fraction.from_float(float.fromhex(spec["hex_endpoint"]))
        if endpoint < 0 or int(spec["cell_count"]) < 1:
            raise ValueError("inadmissible directed endpoint or cell count")
        return {"kind": kind, "coefficient": endpoint, "radicand": 1,
                "direction": "upper", "hex_endpoint": spec["hex_endpoint"],
                "provenance": {key: spec[key] for key in required if key != "hex_endpoint"}}
    raise ValueError("unknown derivative-budget kind")


def _compile_window(candidate):
    if candidate.get("chart_normalization") != "periodic_2pi":
        return fail("chart", "the Fourier normalization must be the declared periodic 2pi chart")
    if candidate.get("window_kind") == "sharp_cut":
        return fail("regularity", "sharp interval cuts fail the finite first-absolute-moment certificate")
    if candidate.get("finite_fourier_support") and candidate.get("proper_interval_support"):
        return fail("analytic_support", "a nonzero trigonometric polynomial cannot have proper-interval support")
    for field in ("partition_unity_verified", "proper_interval_support", "c3_endpoint_jets_verified"):
        if candidate.get(field) is not True:
            return fail(field, field + " must be independently verified")
    law, formula = candidate.get("partition_law"), candidate.get("localization_formula")
    if law not in ("linear", "square") or formula not in ("commutator_linear", "ims_quadratic"):
        return fail("localization_convention", "partition law and localization formula must be declared")
    if formula == "ims_quadratic" and law != "square":
        return fail("localization_convention", "IMS localization requires a verified square partition")
    try:
        h = F(candidate["overlap_width"])
        windows, transitions = int(candidate["window_count"]), int(candidate["transitions_per_window"])
        budget = _budget(candidate["third_derivative_l1"])
    except (KeyError, TypeError, ValueError, ZeroDivisionError) as exc:
        return fail("derivative_budget", "malformed typed derivative budget", detail=str(exc))
    if h <= 0 or windows < 1 or transitions < 1:
        return fail("derivative_budget", "width and counts must be positive")
    multiplier = Fraction(windows * transitions, 6) / (h * h)
    coefficient = multiplier * budget["coefficient"]
    expression = f"{coefficient}*pi"
    if budget["radicand"] != 1:
        expression += f"*sqrt({budget['radicand']})"
    return {"schema": SCHEMA, "passed": True, "first_failed_gate": None,
            "fourier_first_moment_bound": {"budget_kind": budget["kind"],
                "direction": budget["direction"], "coefficient": str(coefficient),
                "factors": ["pi"], "sqrt_radicand": budget["radicand"], "expression": expression,
                "provenance": budget["provenance"]},
            "source_gate": {"chart_normalization": "periodic_2pi", "overlap_width": str(h),
                "window_count": windows, "transitions_per_window": transitions,
                "partition_law": law, "localization_formula": formula,
                "partition_unity_verified": True, "proper_interval_support": True,
                "c3_endpoint_jets_verified": True},
            "explanation": {"mechanism": "third-derivative regularity controls Fourier leakage",
                "resolution_tradeoff": "fixed-profile leakage scales as inverse overlap width squared",
                "failure_taxonomy": ["regularity", "analytic_support", "localization_convention",
                                     "derivative_budget", "margin"]},
            "scope": "localization certificate only; not a physical or arithmetic source derivation"}


def compile_window_partition(candidate):
    if "cover" not in candidate:
        return _compile_window(candidate)
    windows = candidate.get("cover")
    if not isinstance(windows, list) or not windows:
        return fail("cover", "cover must contain at least one typed window")
    reports = [_compile_window(item) for item in windows]
    for index, report in enumerate(reports):
        if not report["passed"]:
            return fail("cover_window", "a cover member failed", index=index, report=report)
    if len({r["source_gate"]["localization_formula"] for r in reports}) != 1:
        return fail("cover_formula", "all cover members must use one declared localization formula")
    coefficients = [F(r["fourier_first_moment_bound"]["coefficient"]) for r in reports]
    rule = candidate.get("aggregation_rule", "sum")
    if rule == "sum": aggregate = sum(coefficients, Fraction(0))
    elif rule == "max": aggregate = max(coefficients)
    else: return fail("cover_aggregation", "aggregation rule must be sum or max")
    margin = candidate.get("available_margin")
    margin_report = None
    if margin is not None:
        margin = F(margin)
        margin_report = {"available": str(margin), "consumed_upper": str(aggregate),
                         "survives": aggregate < margin, "residual": str(margin - aggregate)}
        if aggregate >= margin:
            return fail("margin", "aggregated leakage does not preserve the declared margin",
                        aggregate=str(aggregate), available=str(margin), rule=rule)
    best = min(range(len(coefficients)), key=coefficients.__getitem__)
    return {"schema": "marici.scc.window-cover.v1", "passed": True, "first_failed_gate": None,
            "members": reports, "aggregation_rule": rule,
            "aggregate_upper_coefficient_times_pi": str(aggregate), "margin": margin_report,
            "profile_comparison": {"least_leakage_member": best,
                "member_coefficients": [str(x) for x in coefficients]},
            "auxiliary_choice_stability": {"bounded_by_member_sum": rule == "sum",
                "comparison_defined": True},
            "cross_sector_scope": ["optical_apodization", "spectral_commutators",
                                   "PDE_localization", "radial_arithmetic_estimates"]}
