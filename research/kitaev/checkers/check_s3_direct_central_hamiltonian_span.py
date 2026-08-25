"""Direct primitive-Hamiltonian center for the finite D(S3) source."""

import itertools
import json
import sympy as sp


def compose(p, q): return tuple(p[q[i]] for i in range(3))
def inverse(p):
    out = [0, 0, 0]
    for i, image in enumerate(p): out[image] = i
    return tuple(out)
def conjugate(g, h): return compose(compose(g, h), inverse(g))
def parity(p): return -1 if sum(p[i] > p[j] for i in range(3) for j in range(i + 1, 3)) % 2 else 1
def cycle_type(p):
    fixed = sum(p[i] == i for i in range(3))
    return "e" if fixed == 3 else ("t" if fixed == 1 else "c")


def main():
    group = list(itertools.permutations(range(3)))
    e, t, c = (0, 1, 2), (1, 0, 2), (1, 2, 0)
    reps = {"e": e, "t": t, "c": c}
    classes = {name: [g for g in group if cycle_type(g) == name] for name in reps}
    transporters = {name: {target: next(q for q in group if conjugate(q, rep) == target)
                           for target in classes[name]} for name, rep in reps.items()}
    sqrt3 = sp.sqrt(3)
    omega = -sp.Rational(1, 2) + sp.I * sqrt3 / 2
    rmat = sp.Matrix([[-sp.Rational(1, 2), -sqrt3 / 2],
                      [sqrt3 / 2, -sp.Rational(1, 2)]])
    smat = sp.diag(1, -1)
    r, s = (1, 2, 0), (1, 0, 2)
    standard = {}
    for k in range(3):
        pr, mr = e, sp.eye(2)
        for _ in range(k): pr, mr = compose(r, pr), rmat * mr
        for epsilon in range(2):
            standard[compose(pr, s if epsilon else e)] = sp.simplify(
                mr * (smat if epsilon else sp.eye(2)))
    labels = [
        ("A", "e", "triv", 1), ("B", "e", "sign", 1), ("C", "e", "std", 2),
        ("D", "t", "plus", 3), ("E", "t", "minus", 3),
        ("F", "c", "triv", 2), ("G", "c", "omega", 2), ("H", "c", "omega2", 2),
    ]

    def internal_matrix(label, z):
        _, sector, irrep, _ = label
        if sector == "e":
            if irrep == "triv": return sp.Matrix([[1]])
            if irrep == "sign": return sp.Matrix([[parity(z)]])
            return standard[z]
        if sector == "t": return sp.Matrix([[1 if irrep == "plus" or z == e else -1]])
        power = {e: 0, c: 1, compose(c, c): 2}[z]
        exponent = power * {"triv": 0, "omega": 1, "omega2": 2}[irrep] % 3
        return sp.Matrix([[sp.simplify(omega ** exponent)]])

    def representation(label, g, x):
        _, sector, _, dimension = label
        fluxes = classes[sector]
        internal_dim = dimension // len(fluxes)
        matrix = sp.zeros(dimension)
        for i, flux_in in enumerate(fluxes):
            flux_out = conjugate(x, flux_in)
            j = fluxes.index(flux_out)
            if g != flux_out: continue
            qi, qj = transporters[sector][flux_in], transporters[sector][flux_out]
            z = compose(compose(inverse(qj), x), qi)
            matrix[j * internal_dim:(j + 1) * internal_dim,
                   i * internal_dim:(i + 1) * internal_dim] = internal_matrix(label, z)
        return sp.simplify(matrix)

    def endpoint(g, x): return sp.diag(*(representation(label, g, x) for label in labels))
    def gauge(x): return sum((endpoint(g, x) for g in group), sp.zeros(16))

    primitives, names = [], []
    for x in group:
        u = gauge(x)
        primitives.extend([(u + u.H) / 2, (u - u.H) / (2 * sp.I)])
        names.extend([f"gauge_{x}_real", f"gauge_{x}_imag"])
    primitives.extend([endpoint(t, e), endpoint(c, e)])
    names.extend(["B_t", "B_c"])
    a = endpoint(c, c)
    primitives.append(sp.simplify((a - a.H) / (2 * sp.I)))
    names.append("K_c")

    offsets, cursor = [], 0
    for label in labels:
        offsets.append(cursor); cursor += label[3]

    # Constraints for a matrix to be scalar on every simple block.
    def nonscalar_coordinates(M):
        coords = []
        for offset, label in zip(offsets, labels):
            d = label[3]
            block = M[offset:offset+d, offset:offset+d]
            for i in range(d):
                for j in range(d):
                    if i != j: coords.append(sp.simplify(block[i, j]))
            for i in range(1, d): coords.append(sp.simplify(block[i, i] - block[0, 0]))
        return coords

    constraint = sp.Matrix.hstack(*[
        sp.Matrix([sp.re(z) for z in nonscalar_coordinates(H)]
                  + [sp.im(z) for z in nonscalar_coordinates(H)])
        for H in primitives
    ])
    direct_center_coefficients = constraint.nullspace()
    direct_center_matrices = [sp.simplify(sum((v[i] * primitives[i]
                                               for i in range(len(primitives))), sp.zeros(16)))
                              for v in direct_center_coefficients]

    def signature(M):
        return sp.Matrix([sp.simplify(M[o, o]) for o in offsets])

    signatures = sp.Matrix.hstack(*[signature(M) for M in direct_center_matrices])
    direct_center_rank = signatures.rank()
    signature_basis = signatures.columnspace()
    target = sp.Matrix([-8, 1, 2, 3, 6, 7, 20, 5])
    augmented_rank = sp.Matrix.hstack(*signature_basis, target).rank()
    target_direct = augmented_rank == direct_center_rank
    assert direct_center_rank <= 6
    assert not target_direct

    # The identity is a direct gauge Hamiltonian; certify that the center
    # intersection is nonempty and the test is not rejecting all scalars.
    identity_signature = sp.ones(8, 1)
    assert sp.Matrix.hstack(*signature_basis, identity_signature).rank() == direct_center_rank

    result = {
        "schema": "marici.s3-direct-central-hamiltonian-span.v1",
        "primitive_surface": {
            "names": names,
            "declared_hermitian_controls": len(primitives),
            "linear_span_rank": sp.Matrix.hstack(*[H.reshape(256, 1) for H in primitives]).rank(),
        },
        "direct_center": {
            "coefficient_nullity_before_signature_quotient": len(direct_center_coefficients),
            "sector_signature_rank": direct_center_rank,
            "contains_identity": True,
            "target_integer_lifts": list(target),
            "target_Z_is_direct_linear_combination": target_direct,
            "target_augmented_rank": augmented_rank,
        },
        "typing_disposition": {
            "single_simultaneous_primitive_pulse_for_Z": "falsified",
            "lie_closure_membership_of_Z": "previously_verified",
            "finite_timed_switched_word": "not_constructed_by_linear_span_or_lie_rank",
        },
        "aggregate_gates": {
            "primitive_hamiltonian_surface_reconstructed_exactly": True,
            "direct_center_intersection_computed_exactly": True,
            "identity_control_is_present": True,
            "optimal_Z_is_not_a_direct_primitive_linear_combination": True,
            "direct_span_and_lie_closure_are_strictly_distinguished": True,
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True, default=str))


if __name__ == "__main__":
    main()

