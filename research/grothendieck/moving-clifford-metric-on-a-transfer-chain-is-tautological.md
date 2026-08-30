# A Moving Clifford Metric on a Transfer Chain Is Tautological

## Question

The Gamma-wall carrier has no fixed conformally preserved quadratic form.
Could a degree-dependent metric supply the missing geometric algebra?

It can always supply one, but without additional source structure this says
nothing beyond invertibility.

## Universal construction

Let

\[
X_{j+1}=M_jX_j
\]

be any chain of invertible real transfer matrices. Choose any nondegenerate
symmetric form \(Q_0\) at the initial fiber and define recursively

\[
Q_{j+1}=M_j^{-T}Q_jM_j^{-1}.
\]

Then

\[
M_j^TQ_{j+1}M_j=Q_j
\]

identically. Every transfer becomes an isometry between two different
quadratic spaces.

If

\[
P_j=M_{j-1}\cdots M_1M_0,
\]

then

\[
Q_j=P_j^{-T}Q_0P_j^{-1}.
\]

The construction works for every invertible recurrence. It does not use the
Gamma source, Mellin residues, Pearson coefficients, or the cubic response.

## Nonuniqueness

In dimension three, the initial symmetric form has six free parameters.
Every nondegenerate choice produces a different compatible metric chain.
Signature is preserved under the congruence transport, but the source has not
selected which signature or initial form is physical.

Therefore the assertion that a moving Clifford metric exists is universal
and nonexplanatory. It cannot distinguish the physical Gamma wall from a
hostile invertible transfer family.

## What orientation really supplies

The exact determinant theorem supplies less structure and more authority. It
canonically orients the determinant line. In carrier dimension \(d\), define

\[
\widetilde M_j=(\det M_j)^{-1/d}M_j.
\]

Then \(\det\widetilde M_j=1\). This gives a source-authorized special-linear
transport after choosing the positive real determinant root. It preserves
volume, not a metric.

Thus the honest finite geometry is currently special-linear and filtered:

- an invariant tail coflag;
- a wall extension class;
- a positively transported determinant line;
- no fixed quadratic form.

## Where a metric could gain content

A source-selected metric requires more than a linear chain. At least one of
the following must be derived independently:

1. an initial form fixed by a source symmetry or normalization;
2. a local formula for \(Q_j\) from the moment or residue data;
3. a second transport direction producing loops whose metric holonomy can be
   tested;
4. an enlarged carrier with a fixed bilinear pairing before compression.

The third option is the sharpest falsifier. On a one-dimensional chain there
are no loops, so every connection is flat by lack of comparison. With two
independent source transports, compatibility requires both paths around each
square to induce the same form. A nontrivial discrepancy would be genuine
curvature rather than a coordinate choice.

## Consequence for the RH programme

Geometric algebra has not disappeared, but its useful role has shifted. The
next object is not an arbitrarily transported Clifford metric on the
degree chain. It is a source-derived bilinear pairing tested against the
two-dimensional Pearson/Mellin transport and its completion. Only its loop
holonomy or failure thereof can carry information absent from the original
linear recurrence.

## Verification

The checker
`research/grothendieck/checkers/moving_metric_chain_tautology.py` verifies the
metric pullback identity for two symbolic Gamma-wall steps, the closed formula
for the transported form, signature-preserving determinant congruence, and
special-linear normalization.
