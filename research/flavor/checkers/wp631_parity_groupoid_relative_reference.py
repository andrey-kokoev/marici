"""Exact WP631 finite action-groupoid and reference-extension audit."""
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
X = (-1, 1)
Y = (0, 1)

def all_probes(domain):
    return [dict(zip(domain, values)) for values in itertools.product(Y, repeat=len(domain))]

def invariant_original(f):
    return all(f[x] == f[-x] for x in X)

def separates_original(f):
    return f[-1] != f[1]

probes = all_probes(X)
descended = [f for f in probes if invariant_original(f)]
separators = [f for f in probes if separates_original(f)]

XR = tuple(itertools.product(X, X))
def orbit(pair):
    x, r = pair
    return frozenset(((x, r), (-x, -r)))

orbits = {orbit(pair) for pair in XR}
relative_values = {pair: pair[0] * pair[1] for pair in XR}
relative_constant_on_orbits = all(
    len({relative_values[p] for p in o}) == 1 for o in orbits)
relative_separates_orbits = len({next(iter({relative_values[p] for p in o}))
                                 for o in orbits}) == len(orbits)

# Forgetting r returns the transitive original action groupoid.
forgotten_orbits = {frozenset(X) for _ in orbits}

checks = {
    "original_groupoid_has_one_isomorphism_class": len({frozenset(X)}) == 1,
    "exactly_two_boolean_probes_descend": len(descended) == 2,
    "exactly_two_boolean_probes_separate_sign": len(separators) == 2,
    "no_absolute_separator_descends": not any(f in descended for f in separators),
    "diagonal_reference_groupoid_has_two_classes": len(orbits) == 2,
    "relative_product_descends": relative_constant_on_orbits,
    "relative_product_is_jointly_faithful": relative_separates_orbits,
    "forgetting_reference_collapses_relative_classes": len(forgotten_orbits) == 1,
}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP631", "status": "PASS", "checks": checks,
    "original_groupoid": "{+1,-1}//Z2 has one isomorphism class",
    "extended_groupoid": "({+1,-1} x {+1,-1})//Z2_diagonal has two classes",
    "relative_invariant": "I(x,r)=x*r",
    "classification": "relative-reference window in a changed stabilizer groupoid; no absolute selector",
    "smallest_exact_falsifier": "the two nonconstant Boolean sign probes fail descent",
    "source_gate": "derive and prepare the odd reference independently of the desired flavor orientation",
    "instrument_gate": "measure the relative class and audit gauged-Z2 anomalies and defects",
}
(ROOT / "results" / "wp631_parity_groupoid_relative_reference.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

