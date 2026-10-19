"""Exact active-state observer for the declared native coefficient dynamics.

Not the unchanged J4, not a physical detector, and not a kernel reset.
"""
from dataclasses import dataclass
import sympy as S
from hamiltonian_descent_wg import generate, state, zero


@dataclass(frozen=True)
class HamiltonianObservation:
    active: S.ImmutableMatrix
    retained_kernel: S.ImmutableMatrix
    source: S.ImmutableMatrix
    energy: S.Expr
    provenance: str


@dataclass(frozen=True)
class RetainedHamiltonianObserver:
    witness: object

    def observe(self, field, provenance):
        if not provenance:
            raise ValueError('observation provenance required')
        field=S.ImmutableMatrix(field)
        if field.rows!=self.witness.source.D.rows or field.cols==0:
            raise ValueError('source coefficient field dimensions')
        if any(value.is_real is not True for value in field):
            raise ValueError('real coefficient field required')
        active=S.ImmutableMatrix(self.witness.P*field)
        hidden=S.ImmutableMatrix(self.witness.N*field)
        energy=S.simplify((active.T*self.witness.target.K*active).trace()/2)
        return HamiltonianObservation(active,hidden,field,energy,provenance)

    def observe_retained(self, target_field, T, L, provenance):
        """Read a supplied consistent complete value chart, not outer means."""
        target_field=S.ImmutableMatrix(target_field)
        n=self.witness.source.D.rows
        if T.cols!=n or L.shape!=(n,T.rows) or target_field.rows!=T.rows:
            raise ValueError('retained value chart dimensions')
        if any(value.is_real is not True for matrix in (target_field,T,L) for value in matrix):
            raise ValueError('real retained value chart required')
        if L*T!=S.eye(n) or T*L*target_field!=target_field:
            raise ValueError('inconsistent retained value chart')
        return self.observe(L*target_field,provenance)

    def reconstruct(self, observation):
        return self.witness.E*observation.active+observation.retained_kernel

    def energy_from_active(self, active):
        return S.simplify((active.T*self.witness.target.K*active).trace()/2)


def construct_observer(A):
    """Canonical rational row-basis choice, not a calibrated mode frame."""
    A=S.ImmutableMatrix(A)
    if (A.rows!=A.cols or not zero(A+A.T)
            or any(value.is_real is not True for value in A)):
        raise ValueError('real skew coefficient generator required')
    basis=A.T.columnspace()
    if not basis:
        raise ValueError('nonzero active generator required')
    C=S.Matrix.vstack(*(v.T for v in basis))
    E=C.T*(C*C.T).inv()
    source=state(S.eye(A.rows),A,A/2,A.T*A/2,
                 ('declared native coefficient Hamiltonian; energy ||A F||^2/4',))
    witness=generate(source,E,C,'exact active rowspace observer; rational chart supplied')
    return RetainedHamiltonianObserver(witness)
