"""Small exact momentum-twistor constructors used by source-backed checks.

Arguments are four-component SymPy column matrices. Constructed points and
lines are projective: overall nonzero normalization is immaterial.
"""
import sympy as s


def four_bracket(a, b, c, d):
    """Return <abcd>."""
    return s.det(s.Matrix.hstack(a, b, c, d))


def line_plane_point(a, b, c, d, e):
    """Return a representative of (ab) intersect (cde)."""
    return s.expand(a * four_bracket(b, c, d, e) + b * four_bracket(c, d, e, a))


def plane_plane_line_contraction(a, b, c, x, y, z, A, B):
    """Return <AB|(abc) intersect (xyz)> in the source convention."""
    return s.expand(
        four_bracket(A, a, b, c) * four_bracket(B, x, y, z)
        - four_bracket(B, a, b, c) * four_bracket(A, x, y, z)
    )


def plane_covector(a, b, c):
    """Return the row covector p with p*X = <Xabc>."""
    basis = s.eye(4)
    return s.Matrix([[four_bracket(basis[:, i], a, b, c) for i in range(4)]])


def plane_plane_line_dual_plucker(a, b, c, x, y, z):
    """Return the antisymmetric dual Plücker matrix of (abc) intersect (xyz).

    If p and q are the two plane covectors, L=p.T*q-q.T*p.  Thus
    A.T*L*B equals <AB|(abc) intersect (xyz)>, and the geometric line
    is ker(L).
    """
    p = plane_covector(a, b, c)
    q = plane_covector(x, y, z)
    return s.expand(p.T * q - q.T * p)


def four_mass_psi(A, B, z1, z2, z4, z5, z6, z8):
    """Return the branch-dependent four-mass prefactor psi."""
    cross_ratio = (
        four_bracket(A, z4, z5, z6) * four_bracket(B, z8, z1, z2)
        / (four_bracket(A, z4, z1, z2) * four_bracket(B, z8, z5, z6))
    )
    return s.factor(1 / (1 - cross_ratio))


def four_mass_auxiliary_branches(z1, z2, z3, z4, z5, z6, z7, z8):
    """Return both generic solutions of A=(78)∩(56B), B=(34)∩(12A).

    Each result is ``(alpha, beta, A, B)`` with
    A=z7+alpha*z8 and B=z3+beta*z4, following arXiv:1212.5605.
    """
    alpha, beta = s.symbols("alpha beta")
    n0 = four_bracket(z5, z6, z3, z7)
    n1 = four_bracket(z5, z6, z4, z7)
    d0 = four_bracket(z8, z5, z6, z3)
    d1 = four_bracket(z8, z5, z6, z4)
    m0 = four_bracket(z1, z2, z7, z3)
    m1 = four_bracket(z1, z2, z8, z3)
    e0 = four_bracket(z4, z1, z2, z7)
    e1 = four_bracket(z4, z1, z2, z8)
    f = s.expand(alpha * (d0 + beta*d1) - (n0 + beta*n1))
    g = s.expand(beta * (e0 + alpha*e1) - (m0 + alpha*m1))
    polynomial = s.factor(s.resultant(f, g, beta))
    roots = s.solve(polynomial, alpha)
    if len(roots) != 2:
        raise ValueError("four-mass system does not have two generic branches")
    out = []
    for av in roots:
        bv = s.factor((n0-av*d0)/(av*d1-n1))
        if s.simplify(f.subs({alpha:av,beta:bv})) != 0 or s.simplify(g.subs({alpha:av,beta:bv})) != 0:
            raise ValueError("failed to reconstruct four-mass branch")
        out.append((av, bv, s.simplify(z7+av*z8), s.simplify(z3+bv*z4)))
    return tuple(out)


def plane_plane_line_basis(a, b, c, x, y, z):
    """Return two column vectors spanning (abc) intersect (xyz).

    Raises ValueError when the two inputs do not define a unique projective
    line (equivalently, when the dual Plücker matrix does not have rank two).
    The returned basis normalization is implementation-dependent.
    """
    line = plane_plane_line_dual_plucker(a, b, c, x, y, z)
    if line.rank() != 2:
        raise ValueError("planes do not define a unique intersection line")
    basis = line.nullspace()
    if len(basis) != 2:
        raise ValueError("intersection-line kernel is not two-dimensional")
    return tuple(basis)
