import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def pole(name, residue, mass2, ports=("left", "right")):
    return {
        "name": name,
        "residue": Fraction(residue),
        "mass2": Fraction(mass2),
        "ports": frozenset(ports),
    }


def packet(prefix, masses):
    return [pole(f"{prefix}_{i:02d}", 1, m) for i, m in enumerate(masses, 1)]


# Minimal atom-level source cell for the WP1036 capacity point.  The integer
# label, residue sum, degeneracy, mass clock, and finite response are all
# derived from the same atoms.
degenerate_clock_one = packet("good", [1] * 23)

# Scalar repairs can declare the same spectrum while their atoms derive a
# different spectrum or clock.
split_declared_as_degenerate = packet("split", [1] * 22 + [4])
clock_two_declared_as_clock_one = packet("clock", [2] * 23)

DECLARED_SPECTRUM = {
    "k": 2,
    "C": 23,
    "degenerate": True,
    "M2": Fraction(1),
    "normalized_R1_over_R0": Fraction(1, 2),
}


def derive_spectrum(cell):
    assert cell
    residues = [a["residue"] for a in cell]
    masses = [a["mass2"] for a in cell]
    port_counts = {len(a["ports"]) for a in cell}
    assert all(r > 0 for r in residues)
    assert all(m > 0 for m in masses)
    assert all(a["ports"] for a in cell)

    k = next(iter(port_counts)) if len(port_counts) == 1 else None
    C = sum(residues, Fraction(0))
    R0 = C
    R1 = sum((r * m / (m + 1) for r, m in zip(residues, masses)), Fraction(0))
    normalized = R1 / R0
    degenerate = len(set(masses)) == 1
    mass_clock = masses[0] if degenerate else None
    h_pi2_coefficient = Fraction(C * 12, 1367 * k) if k else None
    mass_histogram = {}
    for m in masses:
        mass_histogram[str(m)] = mass_histogram.get(str(m), 0) + 1

    return {
        "atom_count": len(cell),
        "k": k,
        "C": C,
        "R0": R0,
        "R1": R1,
        "normalized_R1_over_R0": normalized,
        "degenerate": degenerate,
        "M2": mass_clock,
        "h_pi2_coefficient": h_pi2_coefficient,
        "mass_histogram": mass_histogram,
        "atom_provenance_ok": k is not None and C == len(cell),
    }


def matches_declared(derived, declared):
    return (
        derived["k"] == declared["k"]
        and derived["C"] == declared["C"]
        and derived["degenerate"] == declared["degenerate"]
        and derived["M2"] == declared["M2"]
        and derived["normalized_R1_over_R0"] == declared["normalized_R1_over_R0"]
    )


good = derive_spectrum(degenerate_clock_one)
assert good["k"] == 2
assert good["C"] == 23
assert good["h_pi2_coefficient"] == Fraction(138, 1367)
assert good["degenerate"] and good["M2"] == 1
assert good["normalized_R1_over_R0"] == Fraction(1, 2)
assert good["atom_provenance_ok"]
assert matches_declared(good, DECLARED_SPECTRUM)

split = derive_spectrum(split_declared_as_degenerate)
assert split["k"] == 2 and split["C"] == 23
assert not split["degenerate"] and split["M2"] is None
assert split["normalized_R1_over_R0"] == Fraction(59, 115)
assert not matches_declared(split, DECLARED_SPECTRUM)

clock_two = derive_spectrum(clock_two_declared_as_clock_one)
assert clock_two["k"] == 2 and clock_two["C"] == 23
assert clock_two["degenerate"] and clock_two["M2"] == 2
assert clock_two["normalized_R1_over_R0"] == Fraction(2, 3)
assert not matches_declared(clock_two, DECLARED_SPECTRUM)

# Both hostiles are exactly the scalar declaration if atom provenance is erased.
assert DECLARED_SPECTRUM == {
    "k": 2,
    "C": 23,
    "degenerate": True,
    "M2": 1,
    "normalized_R1_over_R0": Fraction(1, 2),
}


def encode(x):
    if isinstance(x, Fraction):
        return str(x)
    if isinstance(x, dict):
        return {k: encode(v) for k, v in x.items()}
    if isinstance(x, list):
        return [encode(v) for v in x]
    return x


result = {
    "schema": "marici.flavor.wp1053.v1",
    "status": "PASS",
    "question": "Can a typed pole spectrum and mass clock be derived from the same finite source atoms as the integer coefficient C=23?",
    "atom_model": {
        "ports_per_atom": ["left", "right"],
        "good_cell": {"count": 23, "residue_each": "1", "mass2_each": "1"},
        "split_hostile_atoms": {"count": 23, "mass_histogram": split["mass_histogram"]},
        "wrong_clock_hostile_atoms": {"count": 23, "mass_histogram": clock_two["mass_histogram"]},
    },
    "derived_good_spectrum": encode(good),
    "declared_scalar_spectrum": encode(DECLARED_SPECTRUM),
    "hostiles": {
        "split_declared_as_degenerate": {
            "derived": encode(split),
            "matches_declared_scalar_spectrum": matches_declared(split, DECLARED_SPECTRUM),
        },
        "clock_two_declared_as_clock_one": {
            "derived": encode(clock_two),
            "matches_declared_scalar_spectrum": matches_declared(clock_two, DECLARED_SPECTRUM),
        },
    },
    "classification": "conditional pole-atom provenance constructor: one finite atom cell derives k=2, C=23, unit residues, degeneracy, M^2=1, h=138 pi^2/1367, and normalized response 1/2; scalar spectrum declarations without matching atoms are rejected",
    "remaining_gate": "derive the 23 pole atoms, their two ports, unit residues, and common mass clock from the actual source representation/dynamics rather than posit the atom cell",
    "claim_boundary": "finite rational pole-atom algebra; no UV action, representation theorem, or physical momentum calibration is claimed",
    "disposition": "productive: WP1039 and WP1040 now have a minimal common-atom realization plus exact scalar-declaration falsifiers",
}

(ROOT / "results" / "wp1053_typed_pole_atom_provenance.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1053 PASS:", good["C"], good["M2"], good["normalized_R1_over_R0"], split["normalized_R1_over_R0"], clock_two["normalized_R1_over_R0"])
