import json
from pathlib import Path


OUT = Path(__file__).resolve().parents[1] / "results" / "t7_bulk_period_uv_gate.json"

# At large Euclidean loop momentum r, all three loop-edge energies scale as r
# and q_G12=E+y12 scales as r.  The physical loop measure is d^3 ell, whose
# radial factor is r^2 dr.  Each tuple is (numerator degree, q power).
basis = {
    "e1": (2, 1),
    "e2": (1, 1),
    "e3": (1, 2),
    "e4": (1, 1),
    "e5": (1, 2),
    "e6": (0, 2),
}

rows = {}
for name, (numerator_degree, q_power) in basis.items():
    integrand_power = numerator_degree - q_power
    radial_power = 2 + integrand_power
    cutoff_power = radial_power + 1
    rows[name] = {
        "numerator_degree": numerator_degree,
        "q_power": q_power,
        "integrand_power_r": integrand_power,
        "radial_power_r": radial_power,
        "cutoff_power": cutoff_power,
        "absolutely_convergent_at_infinity": radial_power < -1,
    }

result = {
    "checker": "t7_bulk_period_uv_gate",
    "dimension": 3,
    "large_loop_scaling": "y12~y23~y31~r and q_G12~r",
    "basis": rows,
    "all_six_raw_periods_uv_divergent": all(not row["absolutely_convergent_at_infinity"] for row in rows.values()),
    "v_alg_generic_leading_behavior": "Lambda^4 through its e8/e9 tail; the coefficient may vanish on special symmetric loci",
    "positive_e1_cutoff_growth": "Lambda^4",
    "bunch_davies_i_epsilon_is_uv_subtraction": False,
    "raw_seven_period_rank_test_well_typed": False,
    "required_next_input": "source-normalized analytic regulator and finite-part/counterterm map, or a proved UV-finite residual quotient pairing",
}

assert result["all_six_raw_periods_uv_divergent"]
assert rows["e1"]["cutoff_power"] == 4
assert rows["e6"]["cutoff_power"] == 1
OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
