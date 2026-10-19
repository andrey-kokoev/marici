"""Task-relative energy summary under the declared family-gain protocol.

Two nonnegative scalar statistics suffice for energy prediction. Full source
records remain retained; this is not a physical-state or detector reduction.
"""
from dataclasses import dataclass
import sympy as S
from hamiltonian_descent_wg import zero


@dataclass(frozen=True)
class EnergyTaskState:
    one_leg: S.Expr
    two_leg: S.Expr
    provenance: str

    @property
    def energy(self):
        return S.simplify(self.one_leg+self.two_leg)


@dataclass(frozen=True)
class EnergyTaskStep:
    parent: EnergyTaskState
    result: EnergyTaskState
    q: S.Expr


def split_projectors(P):
    Q=S.eye(11)-P
    mean=S.SparseMatrix(S.diag(S.kronecker_product(P,P),S.eye(16)))
    one=S.SparseMatrix(S.diag(S.kronecker_product(Q,P)+S.kronecker_product(P,Q),S.zeros(16)))
    two=S.SparseMatrix(S.diag(S.kronecker_product(Q,Q),S.zeros(16)))
    return mean,one,two


def read_energy_task(A,field,one,two,provenance):
    if not provenance:
        raise ValueError('energy-task provenance required')
    field=S.ImmutableMatrix(field)
    if field.rows!=A.rows or field.cols==0:
        raise ValueError('coefficient field dimensions')
    if any(value.is_real is not True for value in field):
        raise ValueError('real coefficient field required')
    a=A*one*field
    b=A*two*field
    return EnergyTaskState(S.simplify((a.T*a).trace()/4),
                           S.simplify((b.T*b).trace()/4),provenance)


def gain_step(parent,q):
    q=S.sympify(q)
    if q.is_nonnegative is not True or (1-q).is_nonnegative is not True:
        raise ValueError('declared contraction q in[0,1] required')
    if (parent.one_leg.is_nonnegative is not True
            or parent.two_leg.is_nonnegative is not True or not parent.provenance):
        raise ValueError('admitted nonnegative energy task state required')
    result=EnergyTaskState(S.simplify(q*q*parent.one_leg),
                           S.simplify(q**4*parent.two_leg),
                           parent.provenance+f'; declared family gain q={q}')
    return EnergyTaskStep(parent,result,q)


def infer_components(total,after,q):
    q=S.sympify(q)
    if q.is_positive is not True or (1-q).is_positive is not True:
        raise ValueError('two readings require0<q<1')
    V=S.Matrix([[1,1],[q*q,q**4]])
    components=V.inv()*S.Matrix([total,after])
    if any(value.is_nonnegative is not True for value in components):
        raise ValueError('readings inconsistent with nonnegative model energies')
    return tuple(S.simplify(value) for value in components)
