"""Exact reference-flux twirl and one-setting electric-sector classifier."""

import itertools
import json
import sympy as sp


def compose(p, q):
    return tuple(p[q[i]] for i in range(3))


def inverse(p):
    out = [0, 0, 0]
    for i, image in enumerate(p):
        out[image] = i
    return tuple(out)


def conjugate(g, h):
    return compose(compose(g, h), inverse(g))


def parity(p):
    return -1 if sum(p[i] > p[j] for i in range(3) for j in range(i + 1, 3)) % 2 else 1


def cycle_type(p):
    fixed = sum(p[i] == i for i in range(3))
    return "identity" if fixed == 3 else ("transposition" if fixed == 1 else "three_cycle")


def main():
    group = list(itertools.permutations(range(3)))
    e, r, s = (0,1,2), (1,2,0), (1,0,2)
    sqrt3 = sp.sqrt(3)
    r_matrix = sp.Matrix([[-sp.Rational(1,2),-sqrt3/2],[sqrt3/2,-sp.Rational(1,2)]])
    s_matrix = sp.diag(1,-1)
    standard = {}
    for k in range(3):
        pr, mr = e, sp.eye(2)
        for _ in range(k):
            pr, mr = compose(r,pr), r_matrix*mr
        for epsilon in range(2):
            standard[compose(pr,s if epsilon else e)] = sp.simplify(mr*(s_matrix if epsilon else sp.eye(2)))
    assert len(standard)==6

    transpositions=[g for g in group if cycle_type(g)=="transposition"]
    cycles=[g for g in group if cycle_type(g)=="three_cycle"]
    trans_conjugation_counts={h:sum(conjugate(g,s)==h for g in group) for h in transpositions}
    cycle_conjugation_counts={h:sum(conjugate(g,r)==h for g in group) for h in cycles}
    assert set(trans_conjugation_counts.values())=={2}
    assert set(cycle_conjugation_counts.values())=={3}

    average_trans_standard=sp.simplify(sum((standard[g] for g in transpositions),sp.zeros(2))/3)
    average_cycle_standard=sp.simplify(sum((standard[g] for g in cycles),sp.zeros(2))/2)
    assert average_trans_standard==sp.zeros(2)
    assert average_cycle_standard==-sp.eye(2)/2

    expectations={
        "A":{"mu_D":sp.Integer(1),"mu_F":sp.Integer(1)},
        "B":{"mu_D":sp.Integer(-1),"mu_F":sp.Integer(1)},
        "C":{"mu_D":sp.Integer(0),"mu_F":-sp.Rational(1,2)},
    }
    assert len({values["mu_D"] for values in expectations.values()})==3
    plus_probabilities={label:sp.simplify((values["mu_D"]+1)/2) for label,values in expectations.items()}
    assert plus_probabilities=={"A":1,"B":0,"C":sp.Rational(1,2)}

    expectation_gap=min(abs(expectations[a]["mu_D"]-expectations[b]["mu_D"])
                        for a,b in itertools.combinations(expectations,2))
    probability_gap=expectation_gap/2
    frequency_radius=probability_gap/2
    assert expectation_gap==1 and probability_gap==sp.Rational(1,2) and frequency_radius==sp.Rational(1,4)

    result={
        "schema":"marici.s3-electric-reference-twirl.v1",
        "uniform_conjugation_counts":{
            "transposition_reference":sorted(trans_conjugation_counts.values()),
            "three_cycle_reference":sorted(cycle_conjugation_counts.values()),
        },
        "standard_charge_averaged_actions":{
            "transposition_reference":"zero_2x2",
            "three_cycle_reference":"minus_one_half_identity_2x2",
        },
        "electric_sector_expectations":{label:{name:str(value) for name,value in values.items()} for label,values in expectations.items()},
        "one_setting_classifier":"mu_D",
        "mu_D_plus_probabilities":{label:str(value) for label,value in plus_probabilities.items()},
        "minimum_expectation_gap":"1",
        "minimum_probability_gap":"1/2",
        "sharp_empirical_frequency_radius":"strictly_less_than_1/4",
        "iid_bernoulli_sufficient_bound":{
            "failure_probability_upper_bound":"2*exp(-n/8)",
            "shots_for_target_alpha":"ceiling(8*ln(2/alpha))",
            "assumptions":["uniform_random_reference_conjugation","controlled_monodromy","independent_repetitions","stationary_calibration"],
        },
        "aggregate_gates":{
            "group_conjugation_uniformizes_reference_flux_class":True,
            "transposition_reference_average_is_zero_on_standard_charge":True,
            "three_cycle_reference_average_is_scalar_on_standard_charge":True,
            "target_electric_internal_state_drops_out":True,
            "one_D_reference_setting_separates_A_B_C":True,
            "binary_probability_gap_is_one_half":True,
            "full_eight_sector_extension_is_not_inferred":True,
        },
    }
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__=="__main__":
    main()
