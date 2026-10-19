"""Top-down candidate from a supplied vertex cycle and twelve arrow labels.

No bottom rotor/generator is imported. Cycle selection, skew extraction,
metric and energy scale are declared mathematical rules, not physical laws.
"""
import sympy as S
from hamiltonian_descent_wg import state


def construct(vertices, forward, labels, alpha):
    alpha = S.sympify(alpha)
    if alpha.is_positive is not True:
        raise ValueError('positive declared energy normalization required')
    if set(forward) != set(vertices) or set(forward.values()) != set(vertices):
        raise ValueError('vertex permutation required')
    if set(labels) != set(vertices) or set(labels.values()) != set(range(4)):
        raise ValueError('declared four-port labels required')
    # First orbit is the cycle-cover edge from each source vertex. This is
    # specified by source endpoint roles, not by a target Hamiltonian fit.
    visible = tuple(v+forward[v] for v in sorted(vertices, key=labels.get))
    all_edges = tuple(a+b for a in vertices for b in vertices if a != b)
    if len(set(visible)) != 4 or any(e not in all_edges for e in visible):
        raise ValueError('fixed-point-free cover required')
    edges = visible+tuple(e for e in all_edges if e not in visible)
    moved = tuple(forward[e[0]]+forward[e[1]] for e in edges)
    C = S.Matrix(12,12,lambda i,j:int(edges[i] == moved[j]))
    G = 10*S.eye(12)+S.ones(12)
    D = C-C.T
    Omega = alpha*G*D
    K = D.T*Omega
    source = state(G,D,Omega,K,(
        'twelve directed carrier arrows with induced vertex permutation',
        'declared skew-part rule D=C-C^T and fixed stabilizer Gram',
        f'declared energy/form normalization alpha={alpha}',))
    return source, C, edges


def reducing_frame(source, E, P):
    """Keep supplied visible embedding; organize hidden rotors and zero modes.

    Rational Gram arithmetic; no discarded coordinate is set to vacuum.
    Requires the source's hidden active generator to square to -4I.
    """
    G,D = source.G,source.D
    N = S.eye(G.rows)-E*P
    active = -D**2/4
    stationary = S.eye(G.rows)-active
    pairs = []
    for e in S.eye(G.rows).columnspace():
        v = active*N*e
        if pairs:
            A = S.Matrix.hstack(*pairs)
            v -= A*(A.T*G*A).inv()*A.T*G*v
        v = S.simplify(v)
        if v != S.zeros(G.rows,1):
            w = D*v/2
            if S.simplify(D*w+2*v) != S.zeros(G.rows,1):
                raise ValueError('hidden active sector is not a frequency2 rotor')
            pairs.extend((v,w))
    zeros = []
    for e in S.eye(G.rows).columnspace():
        v = S.simplify(stationary*N*e)
        old_rank = len(zeros)
        if S.Matrix.hstack(*(zeros+[v])).rank() > old_rank:
            zeros.append(v)
    B = S.Matrix.hstack(E,*pairs,*zeros)
    if B.shape != G.shape or B.det() == 0:
        raise ValueError('incomplete reducing frame')
    framed = state(B.T*G*B, B.inv()*D*B, B.T*source.Omega*B,
                   B.T*source.K*B,source.provenance+('declared retained hidden-mode frame',))
    return framed,B,len(pairs)//2,len(zeros)
