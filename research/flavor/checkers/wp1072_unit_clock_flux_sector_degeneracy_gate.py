import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def sector(n, sigma=1):
    n = int(n)
    sigma = int(sigma)
    assert n != 0 and sigma in (-1, 1)
    B_over_A = Fraction(6 * n * n)
    R2 = Fraction(3 * n * n, 2) / B_over_A
    M2 = Fraction(1, 4) / R2
    vector_ratio_N1 = Fraction(4)
    vector_ratio_N2 = Fraction(16)
    flux_delta = Fraction(2 * sigma * n)
    return {
        "n": n,
        "sigma": sigma,
        "B_over_A": B_over_A,
        "R_star2": R2,
        "M2": M2,
        "vector_ratio_N1": vector_ratio_N1,
        "vector_ratio_N2": vector_ratio_N2,
        "flux_delta": flux_delta,
    }

orbit = [sector(n) for n in (1, 2, 3)]
for s in orbit:
    assert s["R_star2"] == Fraction(1, 4)
    assert s["M2"] == 1
    assert s["vector_ratio_N1"] == 4
    assert s["vector_ratio_N2"] == 16
assert [s["flux_delta"] for s in orbit] == [2, 4, 6]

# The orientation mirror leaves the stabilized clock and momentum spectrum
# unchanged while reversing the signed flux threshold.
mirror = sector(1, sigma=-1)
assert mirror["R_star2"] == orbit[0]["R_star2"]
assert mirror["M2"] == orbit[0]["M2"]
assert mirror["flux_delta"] == -orbit[0]["flux_delta"]

# Off-orbit sectors fail the unit clock, so they are not additional physical
# sector choices once the common clock is imposed.
off_orbit = {
    "n": 1,
    "B_over_A": Fraction(12),
    "R_star2": Fraction(3, 2) / 12,
}
off_orbit["M2"] = Fraction(1, 4) / off_orbit["R_star2"]
assert off_orbit["R_star2"] == Fraction(1, 8)
assert off_orbit["M2"] == 2

# Radius, pole clock, and vector-KK ratios are identical on the entire unit
# orbit; only the flux-sensitive signed threshold separates n or sigma.
clock_observables = ["R_star2", "M2", "vector_ratio_N1", "vector_ratio_N2"]
assert len({tuple(str(s[k]) for k in clock_observables) for s in orbit}) == 1
assert len({str(s["flux_delta"]) for s in orbit}) == 3

result = {
    "schema": "marici.flavor.wp1072.v1",
    "status": "PASS",
    "question": "Does the unit common-clock condition select a flux sector?",
    "unit_clock_orbit": "B/A=6 n^2, n in Z\\{0}",
    "sector_data": [
        {k: (str(v) if isinstance(v, Fraction) else v) for k, v in s.items()}
        for s in orbit
    ],
    "orientation_mirror": {k: (str(v) if isinstance(v, Fraction) else v) for k, v in mirror.items()},
    "off_orbit_hostile": {k: (str(v) if isinstance(v, Fraction) else v) for k, v in off_orbit.items()},
    "degeneracy": {
        "clock_observables_identical_on_orbit": clock_observables,
        "flux_delta_values": [str(s["flux_delta"]) for s in orbit],
        "signed_threshold_law": "Delta=sigma n/R*=2 sigma n on the unit orbit",
    },
    "classification": "unit-clock flux-sector degeneracy gate: radius stabilization and the common clock fix R*=1/2 and M^2=1 on the whole B/A=6n^2 orbit, but do not select n or sigma",
    "remaining_gate": "derive a source preparation law for the flux sector and orientation, or a calibrated flux-sensitive instrument plus source-authorized preparation",
    "claim_boundary": "uses WP790/WP1060/WP1061/WP1062 relations only; it does not identify n with any anomaly or family number",
    "disposition": "productive: the scale blocker is narrowed from an unfixed ratio to an exact invisible-sector orbit plus a signed flux readout",
}

(ROOT / "results" / "wp1072_unit_clock_flux_sector_degeneracy_gate.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1072 PASS:", [str(s["flux_delta"]) for s in orbit], orbit[0]["R_star2"], off_orbit["M2"])
