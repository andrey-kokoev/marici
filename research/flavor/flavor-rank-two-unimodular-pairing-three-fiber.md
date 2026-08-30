# Rank two admits primitive pairing three but leaves inequivalent flux orbits: WP783

## Question

Does the smallest higher-rank unimodular Green--Schwarz lattice contain a
unique primitive characteristic/flux pair of pairing three?

## The two signature-(1,1) lattices

The even hyperbolic plane and odd unimodular form are

\[
U=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix},
\qquad
I_{1,1}=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}.
\]

In the even lattice, the characteristic condition forces both coordinates to
be even. Hence there is no primitive characteristic vector.

In the odd lattice, characteristic vectors have odd coordinates. The vector

\[
b=(1,1)
\]

is primitive, characteristic, and null.

## Pairing three is not an orbit selector

For the odd pairing \(x_1y_1-x_2y_2\), both

\[
f_1=(2,-1),
\qquad
f_2=(4,1)
\]

are primitive and satisfy

\[
b\cdot f_1=b\cdot f_2=3.
\]

Their norms differ:

\[
f_1^2=3,
\qquad
f_2^2=15.
\]

Norm is preserved by every lattice isometry, so the two flux constructors are
physically inequivalent in the faithful lattice quotient. The pairing-three
readout therefore has a non-singleton fiber. The bounded checker also finds
further primitive solutions.

## The kinetic metric is still independent

The exact positive matrices

\[
H_0=
\begin{pmatrix}
1&0\\
0&1
\end{pmatrix},
\qquad
H_1=
\begin{pmatrix}
5/4&3/4\\
3/4&5/4
\end{pmatrix}
\]

both obey

\[
H I_{1,1}H=I_{1,1}.
\]

For the same flux \(f_1\), they give kinetic energies

\[
f_1^TH_0f_1=5,
\qquad
f_1^TH_1f_1=\frac{13}{4}.
\]

The integral lattice therefore does not stabilize the tensor metric or fix
the Stückelberg threshold.

## Classification

Rank two repairs WP782's primitive-pairing obstruction but not selection.
The even lattice has no primitive characteristic sector; the odd lattice has
multiple norm-distinguished pairing-three orbits and a continuous compatible
metric.

The next admissible operation must be independently derived dynamics that
selects one orbit and one metric—not a rule fitted to \(f_1\). It must then
break or relationally type the orientation symmetry and provide the massive
mediator's production and decay instrument.

Reproduce with:

    uv run --with sympy python research/flavor/checkers/wp783_rank_two_unimodular_pairing_three_fiber.py

Generated result:
research/flavor/results/wp783_rank_two_unimodular_pairing_three_fiber.json
