"""Spanning-tree test for group-valued annotation holonomy."""


def triangle_holonomy(ab, bc, ca):
    return ab + bc + ca


def tree_potentials(ab, bc):
    # Gauge convention a_xy + p_x - p_y = 0, with p_A = 0.
    p_a = 0
    p_b = ab
    p_c = ab + bc
    return {"A": p_a, "B": p_b, "C": p_c}


def transformed(label, source, target, potentials):
    return label + potentials[source] - potentials[target]


bad = {"AB": 2, "BC": 3, "CA": -4}
good = {"AB": 2, "BC": 3, "CA": -5}

assert triangle_holonomy(**{k.lower(): v for k, v in bad.items()}) == 1
assert triangle_holonomy(**{k.lower(): v for k, v in good.items()}) == 0

p = tree_potentials(good["AB"], good["BC"])
gauged = {
    "AB": transformed(good["AB"], "A", "B", p),
    "BC": transformed(good["BC"], "B", "C", p),
    "CA": transformed(good["CA"], "C", "A", p),
}
assert gauged == {"AB": 0, "BC": 0, "CA": 0}

# The non-tree residual equals cycle holonomy and survives every potential.
bad_residual = transformed(bad["CA"], "C", "A", tree_potentials(bad["AB"], bad["BC"]))
assert bad_residual == 1

print("obstructed triangle holonomy:", triangle_holonomy(2, 3, -4))
print("flat triangle holonomy:", triangle_holonomy(2, 3, -5))
print("flat gauge potentials:", p)
print("all flat transformed labels:", gauged)
print("non-tree obstruction residual:", bad_residual)
print("PASS: nonzero cycle holonomy cannot be removed by node retyping")
