"""Restricted exact WG for finite quadratic Hamiltonian descent.

Inputs include the proposed embedding/projection. The generator verifies a
reducing Hamiltonian split, or refuses. It does not discover a physical map.
The full source and hidden sector are retained in the returned witness.
"""
from dataclasses import dataclass
from fractions import Fraction
import sympy as S


def zero(matrix):
    return all(S.simplify(value) == 0 for value in matrix)


def require(condition, message):
    if not condition:
        raise ValueError(message)


@dataclass(frozen=True)
class HamiltonianState:
    G: S.ImmutableMatrix
    D: S.ImmutableMatrix
    Omega: S.ImmutableMatrix
    K: S.ImmutableMatrix
    # Energy is x^T K x/2; convention D^T Omega=K. Omega may be degenerate.
    provenance: tuple[str, ...]


def state(G, D, Omega, K, provenance):
    return HamiltonianState(*(S.ImmutableMatrix(m) for m in (G, D, Omega, K)),
                            tuple(provenance))


def positive_metric(G):
    """Exact rational Schur pivots avoid symbolic elimination coefficient blowup."""
    if not zero(G-G.T):
        return False
    if G.is_diagonal():
        return all(value.is_positive is True for value in G.diagonal())
    if all(value.is_Rational for value in G):
        rows=[[Fraction(int(value.p),int(value.q)) for value in G.row(i)]
              for i in range(G.rows)]
        for k in range(G.rows):
            pivot=rows[k][k]
            if pivot<=0:
                return False
            for i in range(k+1,G.rows):
                for j in range(i,G.rows):
                    value=rows[i][j]-rows[i][k]*rows[k][j]/pivot
                    rows[i][j]=rows[j][i]=value
        return True
    return G.is_positive_definite is True


def validate(s):
    n = s.G.rows
    require(all(m.shape == (n, n) for m in (s.G, s.D, s.Omega, s.K)), 'state dimensions')
    require(all(value.is_real is True for matrix in (s.G, s.D, s.Omega, s.K)
                for value in matrix), 'real finite quadratic model')
    require(positive_metric(s.G), 'positive coefficient metric')
    require(zero(s.Omega+s.Omega.T), 'antisymmetric form')
    require(zero(s.K-s.K.T), 'symmetric energy Hessian')
    require(zero(s.D.T*s.Omega-s.K), 'Hamiltonian equation')
    require(zero(s.D.T*s.G+s.G*s.D), 'metric-conservative generator')
    require(zero(s.D.T*s.K+s.K*s.D), 'energy-conservative generator')
    require(bool(s.provenance), 'source provenance')


@dataclass(frozen=True)
class DescentWitness:
    source: HamiltonianState
    target: HamiltonianState
    E: S.ImmutableMatrix
    P: S.ImmutableMatrix
    N: S.ImmutableMatrix
    identities: tuple[str, ...]


def generate(source, E, P, interface_provenance):
    """Execute only on admitted reducing interfaces; reject all other inputs."""
    validate(source)
    E, P = S.ImmutableMatrix(E), S.ImmutableMatrix(P)
    n, m = E.shape
    require(n == source.G.rows and P.shape == (m, n) and 0 < m < n, 'interface dimensions')
    require(bool(interface_provenance), 'interface provenance')
    require(zero(P*E-S.eye(m)), 'projection left inverse')
    G = E.T*source.G*E
    require(zero(E.T*source.G-G*P), 'metric adjoint projection')
    N = S.eye(n)-E*P
    D = P*source.D*E
    # Equivalent to invariance of ker(P). Without this the visible future
    # depends on hidden input, so there is no autonomous target generator.
    require(zero(P*source.D*N), 'hidden-to-visible dynamical obstruction')
    Omega, K = E.T*source.Omega*E, E.T*source.K*E
    require(zero(source.Omega-P.T*Omega*P-N.T*source.Omega*N), 'mixed symplectic-form obstruction')
    require(zero(source.K-P.T*K*P-N.T*source.K*N), 'mixed energy obstruction')
    target = state(G, D, Omega, K, source.provenance+(interface_provenance,))
    validate(target)
    require(zero(P*source.D-D*P), 'generator intertwining')
    require(zero(N*source.D-source.D*N), 'retained hidden dynamics')
    return DescentWitness(source, target, E, P, S.ImmutableMatrix(N),
                          ('PE=I', 'E^T G_source=G_target P',
                           'P D_source=D_target P', 'N D_source=D_source N',
                           'Omega_source=P^T Omega_target P+N^T Omega_source N',
                           'K_source=P^T K_target P+N^T K_source N',
                           'x=E(Px)+Nx'))
