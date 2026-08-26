# The Gamma-Wall Transfer Has No Fixed Conformal Clifford Metric

## Question

Can the oriented tail-wall carrier be upgraded to a genuine geometric algebra
by equipping every degree with one fixed nondegenerate quadratic form that the
source transfers preserve up to scale?

The answer is no. Two consecutive transfer steps already obstruct such a
form, independently of the wall parameter.

## Transfer family

The degree-\(j\) tail-wall transfer is

\[
M_j=
\begin{pmatrix}
j+19/4 & -(3/2)(j+5/4) & 1\\
1 & 0 & 0\\
0 & 0 & c
\end{pmatrix},
\qquad c>0.
\]

Assume that a fixed real symmetric nondegenerate matrix \(Q\) and positive
scalars \(\lambda_j\) satisfy

\[
M_j^TQM_j=\lambda_jQ.
\]

Then the relative transfer

\[
A=M_1M_0^{-1}
\]

must be conformal for the same form, with factor
\(\mu=\lambda_1/\lambda_0\).

## Relative spectrum

Direct calculation gives

\[
A=
\begin{pmatrix}
9/5 & -14/5 & -4/(5c)\\
0 & 1 & 0\\
0 & 0 & 1
\end{pmatrix}.
\]

Its spectrum is

\[
\{1,1,9/5\},
\qquad
\det A=9/5.
\]

For a conformal transformation in dimension three,

\[
A^TQA=\mu Q
\]

implies that \(A\) is similar to \(\mu A^{-T}\). Its eigenvalue multiset must
therefore be invariant under

\[
\alpha\longmapsto\frac{\mu}{\alpha}.
\]

Taking determinants also forces

\[
\mu^3=(\det A)^2=(9/5)^2,
\qquad
\mu=(9/5)^{2/3}.
\]

But neither \(\mu\) nor \(\mu/(9/5)\) belongs to the spectrum
\(\{1,1,9/5\}\). The required reciprocal pairing is impossible.

Hence no fixed nondegenerate quadratic form is conformally preserved by even
the first two source transfers. Exact invariance is excluded a fortiori.

## Geometric meaning

The positive determinant theorem remains intact: finite transfers preserve
orientation and never annihilate the complete blade. What fails is the
stronger claim that they act as rotors or conformal Clifford transformations
for one stationary metric.

Three geometries remain possible:

1. a degree-dependent metric transported by the recurrence;
2. a larger carrier on which a fixed form exists and the observed transfer is
   a compression;
3. a relative or groupoid-valued metric comparing adjacent degrees without
   identifying all fibers with one quadratic space.

The first option exists formally by transporting any initial form, but that
is not explanatory. The next source test is whether the Pearson/Mellin data
select a metric recurrence independently of the desired Clifford conclusion.

## Falsifier value

Any proposed stationary geometric-algebra formulation of this carrier must
fail on the relative spectrum above. Adding a metric chosen separately at
each degree avoids the contradiction only by changing the claim; it must then
derive the metric transport from the source.

## Verification

The checker
`research/grothendieck/checkers/gamma_wall_no_fixed_clifford_metric.py`
verifies the relative matrix, characteristic polynomial, determinant, and the
failure of conformal reciprocal pairing exactly.
