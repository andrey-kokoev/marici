"""Exact bounded audit of the smallest ordinary-matter U(1) completion."""
import itertools
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
wp779 = json.loads((ROOT/"results"/"wp779_minimal_external_u1_family_charge_no_go.json").read_text(encoding="utf-8"))

# Common family charge +1. The family mixed index is
# T(15)+2T(anti-6)=2+1/2+1/2=3.
family_charge = 1
family_dimension = 27
family_mixed = sp.Rational(3)

# The smallest SU(6)-vectorlike nontrivial pair is 6+anti-6.
pair_dimension = 12
fundamental_dynkin_index = sp.Rational(1,2)
pair_charges = (-3,-3)
pair_mixed = fundamental_dynkin_index * sum(pair_charges)

# Residual linear and cubic anomalies before singlets.
linear_before_singlets = family_dimension*family_charge + 6*sum(pair_charges)
cubic_before_singlets = family_dimension*family_charge**3 + 6*sum(q**3 for q in pair_charges)
target_sum = -linear_before_singlets
target_cubes = -cubic_before_singlets

bound = 12
solutions_by_count = {}
for count in range(1,5):
    sols = [
        charges for charges in itertools.combinations_with_replacement(range(-bound,bound+1),count)
        if sum(charges)==target_sum and sum(q**3 for q in charges)==target_cubes
    ]
    solutions_by_count[count] = sols
singlet_charges = solutions_by_count[4][0]

mixed_total = family_mixed + pair_mixed
linear_total = linear_before_singlets + sum(singlet_charges)
cubic_total = cubic_before_singlets + sum(q**3 for q in singlet_charges)

flux = 3
family_weighted_degree = family_dimension * abs(flux*family_charge)
pair_weighted_degree = 6*sum(abs(flux*q) for q in pair_charges)
singlet_weighted_degree = sum(abs(flux*q) for q in singlet_charges)
total_weighted_degree = family_weighted_degree + pair_weighted_degree + singlet_weighted_degree
vector_degree = 35+1
equal_weight_index = 2 + vector_degree - total_weighted_degree

checks = {
    "wp779_dependency_passed": wp779["status"]=="PASS" and all(wp779["checks"].values()),
    "fundamental_pair_cancels_family_mixed_anomaly": mixed_total==0,
    "residual_singlet_targets_are_nine_and_297": (target_sum,target_cubes)==(9,297),
    "no_one_two_or_three_singlet_solution_in_declared_box": all(not solutions_by_count[n] for n in (1,2,3)),
    "first_four_singlet_solution_is_minus7_4_4_8": singlet_charges==(-7,4,4,8),
    "all_ordinary_anomalies_cancel": mixed_total==0 and linear_total==0 and cubic_total==0,
    "flux_weighted_degrees_are_81_108_69": (family_weighted_degree,pair_weighted_degree,singlet_weighted_degree)==(81,108,69),
    "complete_weighted_degree_is_258": total_weighted_degree==258,
    "equal_weight_index_is_minus220": equal_weight_index==-220,
    "anomaly_equations_leave_global_orientation_reverse": all(
        value==0 for value in (-mixed_total,-linear_total,-cubic_total)
    ),
}
checks={name:bool(value) for name,value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result={
    "work_package":"WP780","status":"PASS","checks":checks,"dependency":"WP779",
    "admitted_state_domain":"common unit U(1)_F charge on one 15+2 anti-6 family, one fundamental vectorlike SU(6) pair, and one to four integer-charged singlets with |q|<=12",
    "faithful_coordinate":"the complete integral charge vector, ordinary mixed/linear/cubic anomaly coefficients, and flux-weighted Landau multiplicity",
    "source_authorized_probe":"ordinary four-dimensional anomaly equations plus full absolute flux-index weighting of every charged representation",
    "bounded_completion":"family charge +1, vectorlike 6+anti-6 charges (-3,-3), and singlet charges (-7,4,4,8)",
    "contextual_partition":"anomaly cancellation admits the completion and its global charge reverse; common rescaling is removed only by choosing primitive normalization",
    "spectral_result":"at flux three the family, vectorlike pair, and singlets contribute weighted degrees 81,108,69, totaling 258 and giving equal-weight index -220",
    "tadpole_result":"ordinary gravitational anomaly cancellation forces zero total linear charge, so the completion still does not supply the oriented localized tadpole",
    "classification":"ordinary added matter accommodates common-sign family flux but neither selects its orientation nor preserves the positive spectral basin; it is not the sought source selector",
    "smallest_exact_falsifier":"the first bounded anomaly-complete charge packet has equal-weight index -220 and an equally valid global charge reverse",
    "search_scope":"singlet number 1 through 4 and integer charge box [-12,12]; minimality is claimed only in this declared box",
    "next_source_gate":"test whether a geometrically quantized Green-Schwarz coupling can fix the charge orientation and tadpole without adding the flux-weighted chiral tower or making the U(1) non-executable",
    "instrument_gate":"no physical16 production/decay response or uncertainty matrix is supplied by the anomaly completion",
}
(ROOT/"results"/"wp780_added_matter_u1_completion_spectral_no_go.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
