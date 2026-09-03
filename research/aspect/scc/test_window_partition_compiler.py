#!/usr/bin/env python3
from fractions import Fraction
from window_partition_compiler import compile_window_partition


def septic(**overrides):
    value={"chart_normalization":"periodic_2pi","window_kind":"c3_profile",
      "finite_fourier_support":False,"partition_unity_verified":True,
      "partition_law":"linear","localization_formula":"commutator_linear",
      "proper_interval_support":True,"c3_endpoint_jets_verified":True,
      "overlap_width":"1","third_derivative_l1":{"kind":"exact_quadratic_surd","coefficient":"336/25","radicand":5},
      "window_count":2,"transitions_per_window":2}
    value.update(overrides);return value


def directed_square(**overrides):
    value=septic(partition_law="square",localization_formula="ims_quadratic",
      third_derivative_l1={"kind":"directed_dyadic_upper","hex_endpoint":"0x1.7d5a6321b0566p+5",
       "direction":"upper","cell_count":32768,"backend":"mpmath.iv",
       "checker_locator":"research/voevodsky/checkers/check_angular_ims_interval_integration.py",
       "result_locator":"research/voevodsky/results/angular_ims_interval_integration.json",
       "aggregation_rule":"upper_darboux"})
    value.update(overrides);return value


def main():
    exact=compile_window_partition(septic());assert exact["passed"]
    assert exact["fourier_first_moment_bound"]["expression"]=="224/25*pi*sqrt(5)"
    assert compile_window_partition(septic(window_kind="sharp_cut"))["first_failed_gate"]=="regularity"
    assert compile_window_partition(septic(finite_fourier_support=True))["first_failed_gate"]=="analytic_support"
    assert compile_window_partition(septic(localization_formula="ims_quadratic"))["first_failed_gate"]=="localization_convention"
    directed=compile_window_partition(directed_square());assert directed["passed"]
    assert directed["fourier_first_moment_bound"]["budget_kind"]=="directed_dyadic_upper"
    assert directed["fourier_first_moment_bound"]["direction"]=="upper"
    malformed=directed_square();del malformed["third_derivative_l1"]["result_locator"]
    assert compile_window_partition(malformed)["first_failed_gate"]=="derivative_budget"
    cover=compile_window_partition({"cover":[septic(),septic(overlap_width="2")],"aggregation_rule":"sum"})
    assert cover["passed"] and cover["aggregate_upper_coefficient_times_pi"]=="56/5"
    assert cover["profile_comparison"]["least_leakage_member"]==1
    bounded=compile_window_partition({"cover":[septic(overlap_width="10")],"available_margin":"1","aggregation_rule":"sum"})
    assert bounded["passed"] and bounded["margin"]["survives"]
    failed=compile_window_partition({"cover":[septic()],"available_margin":"1","aggregation_rule":"sum"})
    assert failed["first_failed_gate"]=="margin"
    assert Fraction.from_float(float.fromhex("0x1.43b3d9e9bf596p+3")) > 10
    print("window partition compiler: 12 checks passed")


if __name__=="__main__":main()
