"""Exact four-point spinor-helicity / Feynman comparison.
All-outgoing momenta; independent lambda and tilde-lambda factorization.
Angle brackets are det(lambda_i,lambda_j); square brackets use the reverse
orientation, so <ij>[ji]=2 p_i.p_j. No conjugation is inferred across crossing.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q

from qed_fermion_scattering import C, ZERO, I, dot
import yang_mills_four as YM


@dataclass(frozen=True)
class Spinors:
    lam: tuple[C, C]
    tilde: tuple[C, C]


def bispinor(p):
    e, x, y, z = map(C.of, p)
    return ((e+z, x-I*y), (x+I*y, e-z))


def factor(p):
    m = bispinor(p)
    if m[0][0]*m[1][1]-m[0][1]*m[1][0] != ZERO:
        raise ValueError("Spinor factorization requires null momentum")
    for column in range(2):
        lam = (m[0][column], m[1][column])
        for row in range(2):
            if lam[row] != ZERO:
                tilde = (m[row][0]/lam[row], m[row][1]/lam[row])
                return Spinors(lam, tilde)
    raise ValueError("Zero momentum has no spinor chart here")


def angle(a, b):
    return a.lam[0]*b.lam[1]-a.lam[1]*b.lam[0]


def square(a, b):
    return a.tilde[1]*b.tilde[0]-a.tilde[0]*b.tilde[1]


def vector(m):
    return ((m[0][0]+m[1][1])/2, (m[0][1]+m[1][0])/2,
            -I*(m[1][0]-m[0][1])/2, (m[0][0]-m[1][1])/2)


def outer(a, b):
    return tuple(tuple(x*y for y in b) for x in a)


def polarization(p, reference, helicity):
    """sqrt(2) times a normalized polarization; four legs require /4."""
    if helicity == 1:
        denominator = angle(reference, p)
        matrix = outer(reference.lam, p.tilde)
    elif helicity == -1:
        denominator = square(p, reference)
        matrix = outer(p.lam, reference.tilde)
    else:
        raise ValueError("Helicity must be +/-1")
    if denominator == ZERO:
        raise ValueError("Collinear reference spinor")
    return tuple(2*x/denominator for x in vector(matrix))


REFERENCE_MOMENTA = tuple(tuple(Q(x) for x in p) for p in (
    (1,1,0,0), (1,0,1,0), (1,0,0,1), (1,0,0,-1), (1,-1,0,0), (1,0,-1,0)))
REFERENCES = tuple(factor(p) for p in REFERENCE_MOMENTA)


def references_for(spinors, offset=0):
    result = []
    for p in spinors:
        for step in range(len(REFERENCES)):
            r = REFERENCES[(offset+step) % len(REFERENCES)]
            if angle(r,p) != ZERO and square(p,r) != ZERO:
                result.append(r)
                break
        else:
            raise ValueError("No non-collinear reference available")
    return tuple(result)


def ordered_feynman_parts(ps, spinors, helicities, order=(0,1,2,3), references=None):
    """Coupling/i-stripped ordered coefficient in the convention below.

    In the T basis with Tr(Ta Tb)=delta_ab/2, the full amplitude is
    -2 g^2 [C_12,34 A(1234) + C_13,24 A(1324)].
    The planar coefficient is (K_s-K_u)/2 for normalized polarizations.
    """
    if sorted(order) != [0,1,2,3] or len(spinors) != 4 or len(helicities) != 4:
        raise ValueError("Four legs and a permutation of their labels required")
    if any(outer(z.lam,z.tilde) != bispinor(p) for p,z in zip(ps,spinors)):
        raise ValueError("Spinors do not factor the supplied momenta")
    references = references if references is not None else references_for(spinors)
    if len(references) != 4:
        raise ValueError("Four reference spinors required")
    eps = tuple(polarization(p,r,h) for p,r,h in zip(spinors,references,helicities))
    exchange, contact = YM.lorentz_parts(tuple(ps[i] for i in order), tuple(eps[i] for i in order))
    # /2 defines the ordered coefficient; /4 supplies the four sqrt(2)s.
    return (C.of(exchange[0])/8, -C.of(exchange[2])/8,
            C.of(contact[0]-contact[2])/8)


def ordered_feynman(ps, spinors, helicities, order=(0,1,2,3), references=None):
    return sum(ordered_feynman_parts(ps,spinors,helicities,order,references), ZERO)


def parke_taylor(spinors, helicities, order=(0,1,2,3)):
    if len(spinors) != 4 or len(helicities) != 4 or sorted(order) != [0,1,2,3]:
        raise ValueError("This benchmark implements four-point Parke-Taylor")
    if any(h not in (-1,1) for h in helicities):
        raise ValueError("Helicity must be +/-1")
    if any(sum((z.lam[i]*z.tilde[j] for z in spinors), ZERO) != ZERO
           for i in range(2) for j in range(2)):
        raise ValueError("Spinor momenta do not conserve momentum")
    negative = [i for i,h in enumerate(helicities) if h == -1]
    denominator = C.of(1)
    for i,j in zip(order, order[1:]+order[:1]):
        denominator *= angle(spinors[i],spinors[j])
    if denominator == ZERO:
        raise ValueError("Adjacent spinor bracket pole")
    if len(negative) != 2:
        return ZERO
    a = angle(spinors[negative[0]], spinors[negative[1]])
    return (a*a*a*a)/denominator


def circular_adapter(ps, spinors, helicities, references=None):
    """Expose per-leg phase/scale and longitudinal gauge change explicitly.

    The rational spinor chart is not assumed to give unit-Hermitian-norm
    polarizations. eps_spinor = alpha*eps_circular + beta*p is the bridge
    to the earlier physical circular basis (both omit 1/sqrt(2)).
    """
    references = references if references is not None else references_for(spinors)
    result = []
    for p,z,h,r,(e1,e2) in zip(ps,spinors,helicities,references,YM.polarizations(ps)):
        eps = polarization(z,r,h)
        circular = tuple(C.of(x)-I*h*y for x,y in zip(e1,e2))
        opposite = tuple(C.of(x)+I*h*y for x,y in zip(e1,e2))
        alpha = -C.of(dot(eps,opposite))/2
        beta = (eps[0]-alpha*circular[0])/p[0]
        result.append({"spinor_polarization": eps, "circular_polarization": circular,
                       "alpha": alpha, "beta": beta})
    return tuple(result)
