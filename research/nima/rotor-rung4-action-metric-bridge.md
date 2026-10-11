# A conditional rotor-to-rung-4 bridge, and its actual-seed sector boundary

## Inputs and scope

Reuse the actual active source basis and swap actions recovered in
`recovered-source-to-qp-clock-chain.md`, with coefficient Gram
`Gs=diag(1,2,2,4)`. The target is the EXISTING fixed stabilizer-probe
restriction tower from `carrier-gram-restriction-tower.md`, whose rung-4
Gram is `G4=10I+J`.

Declare a Bool² labelling of the four target probes. This is explicit
interface data, not a consequence of their common dimension. The 137-row
matrix-response fixture and the confirmed transport-role diagram are
separate constructions; this note does not identify them with this tower.

## Construct the action-and-metric intertwiner

Let W be the orthonormal Walsh frame, with columns ordered as trivial,
second-bit odd, first-bit odd, both odd. The source actions are

    SL=diag(1,1,-1,-1), SR=diag(1,-1,1,-1).

The target actions flip the first and second Bool bits. W intertwines them,
and `W^T G4 W=diag(14,10,10,10)`. Consequently

    M=W diag(1/sqrt(14), 1/sqrt(5), 1/sqrt(5), sqrt(2/5))

satisfies BOTH action equations and `M^T G4 M=Gs`. This is an actual
isometry between the two declared metric representations, not an assertion
that the original Clifford coefficient map was already isometric.

Solving all linear intertwiner equations gives `W diag(a,b,c,d)`.
The metric equations fix their magnitudes, leaving 16 independent sign
choices with labels fixed. The positive branch above is explicit; no
canonical unlabelled frame selection is claimed.

## Canonical readout and transported generator

For rung-4 coefficients x, let `(s,q,p,z)=M^-1 x`. In the inherited active
normalization, take

    q_c = sqrt(5)/2 * (x0-x1+x2-x3),
    p_c = sqrt(5)   * (x0+x1-x2-x3).

The previously declared angular generator transports to

    D4 = [[ 0, 1,-1, 0],
          [-1, 0, 0, 1],
          [ 1, 0, 0,-1],
          [ 0,-1, 1, 0]].

It is G4-skew. The active form is the pullback of `2 dq∧dp` and has rank
two on the four-dimensional carrier. The Hamiltonian is

    H_count=2 q_c² + p_c²/2,
    q_c'=p_c, p_c'=-4 q_c.

This reproduces the old rotor's angular flow. It is not inferred from the
Gram eigenvalues alone, and it is not silently substituted into the old
module-normalized contact Hamiltonian.

The common direction and the third contrast direction are stationary.
In particular, the common Gram mode is NOT the previously constructed
clock. G4 remains positive definite; no Lorentzian signature follows.
The retained phase/winding channel is still needed for T.

## Compatibility with the fixed Gram tower

Use the tower's actual direct projection, not coordinate deletion:

    (P_12,4 x)_i=x_i+sum_(j>=4) x_j/14.

If E embeds the first four coordinates, `PE=I` and
`E^T G12=G4 P`. The constructed extension `D12=E D4 P` satisfies

    P D12 = D4 P,
    D12^T G12 + G12 D12=0.

It fixes the discarded orthogonal sector. This proves existence of a
compatible extension; it is constructed from D4, not an independently
source-selected rung-12 generator. Its existence cannot be used as proof
that WG selected that generator.

## A concrete actual-seed clue

The existing `seed-endpoint-sections-and-unique-return-cycle.md` finds the
unique simultaneous incoming/outgoing section of the six-edge seed:

    A -> D -> B -> C -> A.

The checker reruns that enumeration. With probe labels
`A=0, D=2, B=3, C=1`, let C be this permutation's matrix. Exactly:

    D4=C-C^T.

Thus the transported rotor is the skew part of a source-existing reversible
routing, not merely an unrelated four-dimensional oscillator. The cycle-cover
objective and taking the skew part remain declared operations; their physical
selection has not been proved.

There is an important obstruction to identifying the WHOLE cycle with the
rotor. Define

    P_active=(I-C²)/2,
    P_minus=(I-C+C²-C³)/4.

Their ranks are two and one, respectively; `D4²=-4 P_active`. At angular
parameter pi/4,

    exp(pi D4/4)=I-P_active+D4/2,
    exp(pi D4/4)-C=2 P_minus.

The active plane agrees exactly. The alternating mode does not: C has
value -1 there, whereas the rotor has value +1. Indeed det(C)=-1 while
any real matrix exponential has positive determinant. A clock/parity or
extra carrier mechanism is required if one wants to realize that entire
one-step permutation, not just its active sector. The common mode is fixed
by both.

Selecting the cycle also does not preserve every six-arrow responsibility:
AB and BA remain in the original seed even though they are not in the cover.
They must not be silently pruned from a full-source interpretation.

## What is now established

- A metric-and-action preserving map to the particular fixed-Gram rung-4
  carrier, with its residual frame freedom explicitly classified.
- Concrete canonical q,p readout formulas in that chart.
- A compatible chosen extension through the fixed Gram projection.
- An exact relation to the actual seed cycle's active sector, and an exact
  description of the alternating information omitted by the rotor.

Still open: identification with the intended native tower/137 response
interface, selection of the analytic flow and phase module, the full parity
sector, and physical clock/action calibration. The remembered separate
uppercase P has not been identified by this calculation.

## Fresh verification

    uv run --with sympy python research/nima/checkers/check_rotor_rung4_intertwiner.py

45 exact/symbolic checks pass, including reruns of the source coordinate,
Gram tower, and seed section checkers. Receipt:
`results/rotor-rung4-intertwiner.json`. This is symbolic Python verification,
not a new Agda formalization.
