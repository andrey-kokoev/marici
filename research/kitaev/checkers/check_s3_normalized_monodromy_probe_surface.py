"""Exact source-typed normalized-monodromy probe surface for D(S3)."""

import itertools
import json
import sympy as sp


def text(value):
    return str(sp.simplify(value)).replace("sqrt(3)", "sqrt3")


def main():
    labels = ("A", "B", "C", "D", "E", "F", "G", "H")
    dimensions = (1, 1, 2, 3, 3, 2, 2, 2)
    sqrt3 = sp.sqrt(3)
    s_matrix = sp.Matrix([
        [sp.Rational(1,6),sp.Rational(1,6),sp.Rational(1,3),sp.Rational(1,2),sp.Rational(1,2),sp.Rational(1,3),sp.Rational(1,3),sp.Rational(1,3)],
        [sp.Rational(1,6),sp.Rational(1,6),sp.Rational(1,3),-sp.Rational(1,2),-sp.Rational(1,2),sp.Rational(1,3),sp.Rational(1,3),sp.Rational(1,3)],
        [sp.Rational(1,3),sp.Rational(1,3),sp.Rational(2,3),0,0,-sp.Rational(1,3),-sp.Rational(1,3),-sp.Rational(1,3)],
        [sp.Rational(1,2),-sp.Rational(1,2),0,sp.Rational(1,2),-sp.Rational(1,2),0,0,0],
        [sp.Rational(1,2),-sp.Rational(1,2),0,-sp.Rational(1,2),sp.Rational(1,2),0,0,0],
        [sp.Rational(1,3),sp.Rational(1,3),-sp.Rational(1,3),0,0,sp.Rational(2,3),-sp.Rational(1,3),-sp.Rational(1,3)],
        [sp.Rational(1,3),sp.Rational(1,3),-sp.Rational(1,3),0,0,-sp.Rational(1,3),-sp.Rational(1,3),sp.Rational(2,3)],
        [sp.Rational(1,3),sp.Rational(1,3),-sp.Rational(1,3),0,0,-sp.Rational(1,3),sp.Rational(2,3),-sp.Rational(1,3)],
    ])
    normalized = sp.Matrix(8, 8, lambda i, j: sp.simplify(6 * s_matrix[i,j] / (dimensions[i] * dimensions[j])))
    assert all(abs(normalized[i,j]) <= 1 for i in range(8) for j in range(8))

    probes = {
        "twist_Re": (1,1,1,1,-1,1,-sp.Rational(1,2),-sp.Rational(1,2)),
        "twist_Im": (0,0,0,0,0,0,sqrt3/2,-sqrt3/2),
    }
    for j, reference in enumerate(labels):
        probes["mu_" + reference] = tuple(normalized[i,j] for i in range(8))

    def signature(i, family):
        return tuple(probes[name][i] for name in family)

    def faithful(family):
        return len({signature(i, family) for i in range(8)}) == 8

    names = tuple(probes)
    minimum_size, minimum_families = None, []
    for size in range(1, len(names)+1):
        found = [family for family in itertools.combinations(names,size) if faithful(family)]
        if found:
            minimum_size, minimum_families = size, found
            break
    assert minimum_size == 3
    selected = ("twist_Im", "mu_D", "mu_F")
    assert selected in minimum_families

    signatures = {label:[text(x) for x in signature(i,selected)] for i,label in enumerate(labels)}
    distances = {}
    for i,j in itertools.combinations(range(8),2):
        distances[labels[i]+"-"+labels[j]] = max(abs(sp.simplify(a-b)) for a,b in zip(signature(i,selected),signature(j,selected)))
    minimum_expectation_distance = min(distances.values())
    closest_pairs = [pair for pair,value in distances.items() if value == minimum_expectation_distance]
    assert minimum_expectation_distance == sp.Rational(1,2)
    probability_gap = minimum_expectation_distance/2
    frequency_radius = probability_gap/2
    assert probability_gap == sp.Rational(1,4) and frequency_radius == sp.Rational(1,8)

    result = {
        "schema":"marici.s3-normalized-monodromy-probe-surface.v1",
        "normalization":"mu_ab=Tr(M_ab)/(d_a*d_b)=6*S_ab/(d_a*d_b)",
        "candidate_settings":["twist_Re","twist_Im"]+["mu_"+x for x in labels],
        "minimum_setting_count":minimum_size,
        "minimum_family_count":len(minimum_families),
        "minimum_families":[list(x) for x in minimum_families],
        "selected_family":list(selected),
        "selected_expectation_signatures":signatures,
        "minimum_expectation_distance":text(minimum_expectation_distance),
        "closest_pairs":closest_pairs,
        "binary_probability_gap":text(probability_gap),
        "sharp_empirical_frequency_radius":"strictly_less_than_1/8",
        "iid_bernoulli_sufficient_bound":{
            "failure_probability_upper_bound":"6*exp(-n/32)",
            "shots_per_setting_for_target_alpha":"ceiling(32*ln(6/alpha))",
            "assumptions":["controlled_monodromy_or_twist","maximally_mixed_internal_input_for_trace","independent_repetitions","stationary_calibration"],
        },
        "aggregate_gates":{
            "normalized_monodromy_expectations_lie_in_unit_interval":True,
            "three_source_typed_settings_are_jointly_faithful":True,
            "no_one_or_two_setting_family_is_faithful":True,
            "selected_expectation_gap_is_one_half":True,
            "binary_probability_gap_is_one_quarter":True,
            "empirical_frequency_radius_is_one_eighth":True,
            "controlled_trace_dilation_is_typed_but_local_fault_tolerance_is_open":True,
        },
    }
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__ == "__main__":
    main()
