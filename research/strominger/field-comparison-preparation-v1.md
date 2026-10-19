# Field-derived comparisons and a precise 5D/4D candidate

## Prepared from the field, not from the desired numerical readout

For each P directed patch e, the native frame gives a co-moving vector
q_e=R_e^T phi_e in C^3. Define the operator-valued ordered comparison

    C_ji = q_j q_i* : C^3 -> C^3.

Its factors have types C^3 -> C -> C^3. This is a declared comparison choice
using the existing field and frame; it is not a source-selected physical
instrument or the historical numerical T9 assignment.

With the declared excluded mark AB, there are 121 counted arrow-pair blocks.
The other 23 blocks touch that reference. Keeping all 144 blocks retains the
stacked co-moving field up to one common phase. Keeping one nonzero amplitude
anchor restores the full field:

    q_i = C_i,p / conjugate(q_p).

Here p is a component coordinate, and C_i,p denotes the corresponding column
of the assembled block matrix. The checker validates the anchor and reconstructs
all pair blocks from the recovered field. A zero field has its own no-anchor
case. The first-nonzero-coordinate choice is a chart convention, not a globally
smooth or physically selected phase reference.

The formula proves recovery for every generated packet in its stated chart;
six exact fixtures also test zero, two alignment-relative modes, a dense field,
a reference-only field and a common-phase change.

## What would have been lost

Two orthogonal unit vectors in the two-dimensional relative alignment sector
produce identical scalar pairings q_i* q_j and zero common return. Their
operator comparisons differ, and both anchored fields reconstruct exactly.

Two additional controls show:

- 121 counted blocks alone cannot distinguish zero from a reference-only field;
- even all 144 outer-product blocks cannot distinguish a common phase change.

Thus the excluded-reference records and phase anchor have distinct jobs.
Twelve exact proper-rotation checks verify covariance with the reference mark
transported. Omitting the frame or keeping the excluded mark fixed under an
unrelated relabelling would describe another preparation.

## The numbered transport is not yet bound

The candidate supplies the arrow comparison branch only. Four independent state
roots and their sixteen comparisons are not derived by this construction.
There is no new claim of a complete field-derived 137-slot preparation.

The actual existing DG numerical multiplication is two-dimensional. Feeding
it a 3-by-3 projector supported on its third coordinate produces a zero 2-by-2
answer: an out-of-contract misuse, not a reported bug in its declared domain.
The new blocks must therefore not be silently submitted to that implementation.
A different lower-dimensional encoding, or an explicitly changed typed
realization interface, would need its own preservation and recovery tests.
Matrix sizes alone do not prove that every alternative encoding is impossible.

## A five-dimensional state space is present under a precise restriction

An exact isometric embedding J identifies the native alignment sector with
C^3:

    J*J = I_3,   JJ* = G_P.

Choose its first coordinate as the rank-one return and the other two as the
relative alignment modes. Then the native dimensionless projector defect
Hhat=2I-L-G restricts to

    J* Hhat J = diag(0,1,1).

For w in C^3 with norm one, the aligned field Jw has unit norm. Its state space
is the real five-sphere S^5. This is the normalized ALIGNMENT sector, not the
whole 36-complex-dimensional field and not the fully coherent return sector.

There are two different four-dimensional constructions here.

### A. Four-dimensional projective readout

The unanchored pair data on this sector determine w w*. Unit vectors differing
only by common phase have the same data:

    U(1) -> S^5 -> CP^2.

CP^2 has real dimension four. Without fixed norm the base additionally retains
a positive norm scale. The zero field is a separate stratum.

The native Hermitian metric defines horizontal tangents by w* delta w=0.
They have real rank four inside the five-dimensional sphere tangent. But they
do not integrate into four-dimensional layers. For alpha=-i w* dw, at w=e0
and horizontal vectors delta=e1, epsilon=i e1, exactly

    d alpha(delta,epsilon) = 2.

The checker verifies this nonzero curvature and that the pair-readout
differential kills the vertical phase tangent while detecting four independent
horizontal tangents. This is a quotient with curved horizontal transport, not
an integrable codimension-one foliation or a clock construction.

### B. Genuine four-dimensional fixed-defect layers

Write the return coordinate as w0 and fix

    c = 1 - |w0|^2.

For 0<c<1 the normalized states at fixed c are

    sqrt(1-c) S^1 x sqrt(c) S^3.

These ARE four-dimensional codimension-one level sets in S^5. They retain the
common phase and freeze the return-versus-relative weight. They are not the
same four directions as the projective horizontal distribution.

The checker exhibits four independent skew-Hermitian tangent generators at
w=(1,1,0)/sqrt(2), all commuting with the return-coordinate projector. A fifth
Lie-algebra generator fixes that state. This agrees with the generic
U(1) x U(2) orbit dimension four and its one-dimensional stabilizer.

The endpoint levels are singular relative to this generic foliation:

- c=0: only the return circle S^1;
- c=1: the relative sphere S^3.

Full simultaneous L/G coherence forces c=0, not the entire S^5. Moreover,
requiring the ordered corner-cycle data reduces the internal symmetry to common
phase, as established in the preceding rigidity calculation. The four generic
orbit directions preserve metric and projectors, not all that extra cyclic data.

All metrics inherited here are positive. Neither the circle phase nor c has a
physical-time interpretation, and no Lorentzian spacetime is obtained merely
from the topology S^1 x S^3. There is no identification with native realization
grade, the numbered rung4 readout or a Postnikov stage.

## Disposition and replay

The earlier 5D/4D proposal now has explicit candidate mathematics within a
specified field sector: a five-dimensional normalized state space, genuine
four-dimensional fixed-defect levels, and a different four-dimensional
projective readout. Their distinction prevents a false identification of phase
quotient, internal symmetry orbit and spacetime.

The field-derived arrow preparation retains relative-mode information, but
remains outside the existing T9 numerical input type and lacks the separate
state-root branch. These are the current interface gates, not absence of a
comparison construction.

    python research/strominger/checkers/check_field_comparison_preparation.py
    python research/aspect/scc/scc.py check field-comparison-preparation-v1

Exact checks and the owner-local SCC model pass. The checker freshly replays
the native rigidity dependency. Receipt:
`results/field-comparison-preparation/verification.json`.
Protocol: `field-comparison-preparation-protocol-v1.md`.
No production/viewer, existing numerical fixture or earlier ledger checkpoint
was changed.
