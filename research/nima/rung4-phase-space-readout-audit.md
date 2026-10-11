# Return to the tower: test the rung-4 readout before naming q,p,t

## Question

Could classical `(q,p,t)` arise as a readout of the larger WG realization
tower, rather than being supplied to an isolated Bool Tick?

The fixed-source Bool Tick classification does not classify the whole tower,
changing sources, retained ancestry, or primitive source production. It is
not a no-go theorem for this proposal.

## Actual prior interface used

The existing `rung-transport-diagram-and-fixed-reference.md` and
`checkers/check_rung_transport_diagram.py` specify

    12 --9--> 6
     |       |
    11 --8--> 5
     |       |
    10 --7--> 4.

The reference/readout sits at rung 4. The checked fixture uses 137 retained
shared-leg matrix rows, member-mass weighted responses, supplied reference
`d4=2I`, and horizontal candidates built from incoming-family promotion.
This is NOT the four-edge paw used by the separate ancestry-coordinate
experiment. The present audit reuses this exact fixture and reruns its
assertions, without modifying its source or reference.

## Test 1: is the existing readout a moving state coordinate?

For rows `(m_i,C_i)`, write

    J4 = sum_i m_i C_i / M - d4.

An incoming family `F` carries mass `M_F=sum_(i in F) m_i` and response
`C_F=sum_(i in F) m_i C_i / M_F`. Therefore

    sum_F M_F C_F = sum_i m_i C_i.

The existing J4 is conserved exactly. The checker confirms this through
four promotion states for both existing policies, while retained leaves
remain recoverable. A finite difference of J4 along these promotions is
zero. Calling that difference momentum would add a name, not a canonical
conjugate structure.

This does NOT imply that physical position cannot emerge at rung 4 or that
WG evolution is stationary. Presentation transport may properly preserve
an observable. The result warns against confusing rung transport with a
physical time evolution, or a conserved response with a position chart.

## Test 2: does a richer observable determine its own next value?

Use the covariance of the four matrix entries in addition to the mean,
and hold the promotion index fixed. Freeze the inherited-key promotion
policy; do not compare different generators.

Swap the values on existing leaf rows 0 and 1, leaving their labels,
endpoints, masses, and all other rows unchanged. This preserves the ENTIRE
unlabelled multiset of values, hence the current mean and covariance
(and every statistic depending only on that value multiset). It changes
how values are attached to target families.

The next response variances are exactly

    original: 5885249/6081156
    swapped:  147170681/152028900.

Thus mean, covariance, and the same promotion counter do not define a
closed next-state law on this Row-domain. This is a fibre/projectability
failure, not a claim that no alternative phase-space readout can close.

**Admissibility boundary:** the swap is legal in the declared Row interface.
It is NOT proved to arise from native seed constructors or from a new
shared-leg matrix factorization. Consequently the hostile is not yet a
no-go result on a narrower source-admitted domain.

## What repairs this particular prediction?

Retain target-labelled pairs `(M_F,C_F)`. These exactly determine the
next covariance under incoming-family promotion. Both the original and
swapped fixtures pass that reconstruction check.

The relevant lost information is therefore relational attachment, not
another unlabelled scalar moment. This makes a position/response or
configuration/dual pairing a useful next hypothesis. It does NOT make
the family profile a canonical momentum: its dimension, transformation
law, pairing, and any symplectic reduction must still be established.

## Recovered prior canonical-pair construction

A subsequent deeper search recovered the existing rotor programme. It DOES
construct canonical q,p and an unwrapped angular clock conditionally on its
Clifford/phase realization. All three old checkers now pass fresh runs, and
a new exact source-coordinate trace verifies the map from the actual source
swap sector, including its distinct counting-metric normalization. See
`recovered-source-to-qp-clock-chain.md`. The open question below is therefore
identification of that construction with the rung-4 fixture—not absence of
any prior canonical-pair construction.

## Candidate roles, without premature identification

| Classical role | What prior work currently supplies | Missing identification |
|---|---|---|
| q | Separate ancestry contrast coordinates, or matrix response coordinates here | Which is the actual rung-4 configuration readout, and on which source domain? |
| p | Retained labelled incidence, response and comparison information | A dual pairing/symplectic or variational construction; not just a second coordinate or finite difference |
| t | Promotion counters, witness counts, common-mode clock candidates | A source successor distinguished from presentation transport, then clock calibration |

The symmetric Gram/covariance pairing is not by itself an antisymmetric
symplectic form. Four rungs or four coordinates do not establish canonical
conjugacy or spacetime signature.

## Next discriminating task

Identify the actual WG source-changing successor separately from `T9/T8/T7`.
Keep its before/after retained comparison data and a chosen rung-4 projection.
Then test projectability:

    J4(x)=J4(y)  implies  J4(Fx)=J4(Fy).

If it fails on SOURCE-ADMITTED histories, identify the relational fields
that restore closure. Only then test whether their natural response pairing
is canonical, presymplectic with a reduction, or neither. This does not
require selecting a Hamiltonian up front.

## Fresh verification

    python research/nima/checkers/check_rung4_readout_descent.py

31 new exact checks pass, in addition to the imported fixture's assertions.
Results: `results/rung4-readout-descent.json`. No source-derived momentum,
physical clock, Hamiltonian, or continuum-limit claim is made.
