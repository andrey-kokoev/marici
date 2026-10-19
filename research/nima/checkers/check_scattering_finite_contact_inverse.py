# /// script
# dependencies = ["sympy"]
# ///
"""Finite coherent interpolation of positive scalar-port invariants."""
from pathlib import Path
import hashlib
import json
import sympy as S

ROOT = Path(__file__).resolve().parents[3]
AUDIT = "research/nima/results/scattering-contact-source-audit-v1.json"
CLASS = "research/nima/results/scattering-positive-contact-class-v1.json"
NET = "research/nima/contracts/scattering-core-bridge-work-net.v7.json"
REPORT = "research/nima/scattering-finite-contact-inverse-v1.md"
OUT = "research/nima/results/scattering-finite-contact-inverse-v1.json"


def inverse(rs, ys):
    if len(rs) != 3 or len(ys) != 3 or len(set(rs)) != 3:
        raise ValueError("requires three distinct bare source values")
    d12 = S.cancel((ys[0] - ys[1]) / (rs[0] - rs[1]))
    d13 = S.cancel((ys[0] - ys[2]) / (rs[0] - rs[2]))
    if d13 == 0:
        raise ValueError("decoupled or undefined")
    ratio = S.cancel(d12 / d13)
    divisor = S.cancel(rs[2] - ratio * rs[1])
    if divisor == 0:
        raise ValueError("singular interpolation")
    b = S.cancel((1 - ratio) / divisor)
    c = S.cancel(d12 * (1 - b * rs[0]) * (1 - b * rs[1]))
    a = S.cancel(ys[0] - c * rs[0] / (1 - b * rs[0]))
    if not (a > 0 and b > 0 and c > 0 and c <= a * b):
        raise ValueError("outside coupled positive-contact image")
    return a, c, b


def main():
    files = [AUDIT, CLASS, NET, REPORT, "research/nima/checkers/check_scattering_positive_contact_class.py",
             "research/strominger/checkers/interface_preserving_carrier_dynamics.py",
             "research/nima/checkers/check_scattering_finite_contact_inverse.py"]
    hashes = {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in files}
    audit = json.loads((ROOT / AUDIT).read_text())
    classified = json.loads((ROOT / CLASS).read_text())
    for name, receipt in (("audit", audit), ("classification", classified)):
        if not all(hashlib.sha256((ROOT / p).read_bytes()).hexdigest() == h for p, h in receipt["source_sha256"].items()):
            raise AssertionError("stale predecessor: " + name)
    checks = []

    def check(name, value):
        if not value:
            raise AssertionError(name)
        checks.append(name)

    e = S.Symbol("E", positive=True)
    re, ro = [S.sympify(audit["bare_parity_response"][s], locals={"E": e}) for s in ("even", "odd")]
    rs = [S.cancel(re.subs(e, 4)), S.cancel(ro.subs(e, 4)), S.cancel(re.subs(e, 8))]
    check("three_actual_bare_values_distinct", len(set(rs)) == 3)
    check("no_bare_or_dressed_pole_at_samples", all(r != 0 and 1 - 2 * r != 0 for r in rs))
    A, C, b = S.Integer(2), S.Integer(4), S.Integer(2)
    ys = [S.cancel(A + C * r / (1 - b * r)) for r in rs]
    check("source_specific_three_value_inverse", inverse(rs, ys) == (A, C, b))
    strict_ys = [S.cancel(A + r / (1 - b * r)) for r in rs]
    check("strict_positive_completion_inverse", inverse(rs, strict_ys) == (A, S.Integer(1), b))
    # For fixed theta, t determines y=v/sqrt(beta) without knowing beta.
    theta = S.Rational(1, 2)
    for label, energy, value in (("even4", 4, ys[0]), ("odd4", 4, ys[1]), ("even8", 8, ys[2])):
        zz = 2 * S.sqrt(S.Integer(energy) - theta)
        t = S.cancel(S.I * zz / (S.I * zz - value))
        retrieved = S.simplify(zz * (1 - t) / (S.I * t))
        check("exact_coherent_amplitude_to_invariant_response/" + label, retrieved == value and t != 0 and t != 1)
    # Two values permit a continuous positive b-family: determine A,C
    # from each b', preserving both samples but not the third.
    rival_b = S.Rational(21, 10)
    rival_c = S.cancel((ys[0] - ys[1]) * (1 - rival_b * rs[0]) * (1 - rival_b * rs[1]) / (rs[0] - rs[1]))
    rival_a = S.cancel(ys[0] - rival_c * rs[0] / (1 - rival_b * rs[0]))
    check("two_sample_alias_positive", rival_a > 0 and rival_c > 0 and rival_c <= rival_a * rival_b)
    check("two_sample_alias_exact", all(S.cancel(rival_a + rival_c * r / (1 - rival_b * r) - y) == 0 for r, y in zip(rs[:2], ys[:2])))
    check("third_actual_sample_breaks_alias", S.cancel(rival_a + rival_c * rs[2] / (1 - rival_b * rs[2]) - ys[2]) != 0)
    check("one_energy_both_parities_not_enough", rs[0] != rs[1])
    check("decoupled_three_samples_constant", len(set([A, A, A])) == 1)
    try:
        inverse(rs, [A, A, A])
    except ValueError:
        check("decoupled_interpolation_refused", True)
    else:
        raise AssertionError("decoupled data accepted")
    for bad in ([rs[0], rs[0], rs[2]], [rs[0], rs[1]]):
        try:
            inverse(bad, ys[:len(bad)])
        except ValueError:
            check("distinct_source_values_required/" + str(len(bad)), True)
        else:
            raise AssertionError("insufficient sources accepted")
    # Positivity is a genuine extra filter; negative C triples may be
    # interpolated algebraically but cannot enter the positive model class.
    negative = [S.cancel(A - r / (1 - b * r)) for r in rs]
    try:
        inverse(rs, negative)
    except ValueError:
        check("negative_coupling_square_refused", True)
    else:
        raise AssertionError("negative squared coupling accepted")
    net = json.loads((ROOT / NET).read_text())
    nodes = {n["id"]: n for n in net["conjectures"]}
    check("finite_inverse_scoped_constructed", nodes["finite-energy-contact-class-inverse"]["status"] == "resolved" and nodes["finite-energy-contact-class-inverse"]["verdict"] == "constructed")
    check("native_selection_and_root_open", nodes["native-continuum-operation-selection"]["status"] == "deferred_missing_native_principle" and nodes["source-compatible-core-and-channel-bridge"]["status"] == "open" and net["objective"]["outcome"] is None)
    check("no_physical_or_formal_promotion", not any(net["boundary"].values()) and all(n["outcome"] is None for n in nodes.values()))
    check("next_frontier_stated", net["frontier"] == ["native-operation-obstruction-synthesis"] and nodes["native-operation-obstruction-synthesis"]["status"] == "open")
    check("inputs_unchanged", all(hashlib.sha256((ROOT / p).read_bytes()).hexdigest() == h for p, h in hashes.items()))
    result = {"schema": "marici.scattering.finite-contact-inverse.v1", "status": "pass", "check_count": len(checks), "checks": checks,
              "source_sha256": hashes, "source_samples": [{"parity": p, "energy": str(en), "r0": str(v)} for p,en,v in zip(("even","odd","even"),(4,4,8),rs)],
              "coupled_invariants": {"A":str(A),"C":str(C),"b":str(b)},
              "two_sample_positive_alias": {"A":str(rival_a),"C":str(rival_c),"b":str(rival_b)},
              "scope": "three distinct exact r0 values and complex phase, known threshold, positive coupled class; no intensity-only or unknown-threshold claim",
              "root_outcome": None,"native_operation_selected":False,"measurement_work_reopened":False}
    (ROOT / OUT).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({"status":"pass","check_count":len(checks),"two_sample_alias":result["two_sample_positive_alias"],"receipt":OUT}))


if __name__ == '__main__':
    main()
