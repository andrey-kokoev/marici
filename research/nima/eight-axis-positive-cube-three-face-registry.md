# Three-face registry for the operator-decorated positive cube

The eight-axis cube has

$$
\binom{8}{3}=56
$$

generic 3-face types and

$$
56\cdot2^5=1792
$$

3-face instances.

## Classification

| Class | Generic types | Instances | Filler |
|---|---:|---:|---|
| strict or canonical coherence | 45 | 1440 | equality of composites |
| coherent leakage transport | 5 | 160 | shell-cocycle modification |
| historical chart-realization gate | 6 | 192 | awaits native chart-realization square |
| open | 0 | 0 | — |

The coherent lax types are

$$
HqR,
\qquad
VqR,
\qquad
DqR,
\qquad
qLR,
\qquad
qOR.
$$

Their fillers come from preservation of the shell identity

$$
A_X
=
P_X\mathcal F(P_Y-P_X)
+
P_X\mathcal F(I-P_Y)
$$

under rooted multiplication, marked Laurent cuts, admitted degree multipliers, and retained observation.

The six historical gates are the triples containing

$$
qC.
$$

They are

$$
HqC,
\quad
VqC,
\quad
DqC,
\quad
qLC,
\quad
qCO,
\quad
qCR.
$$

For the dagger-leakage cube,

$$
DA_X^qD^{-1}=A_X^{q^\dagger}.
$$

Centered cutoffs are dagger invariant, and dagger reverses the chart arrow. The shell decomposition is carried to its reverse-chart mate.

All other generic 3-faces have pair decorations represented by equalities in the strict or canonical retained model. Their six boundary paths reduce to the same composite, giving the cube filler.

The checker `check_eight_axis_operator_three_face_registry.py` materializes all 56 types and 1792 instances and verifies the classification counts.
