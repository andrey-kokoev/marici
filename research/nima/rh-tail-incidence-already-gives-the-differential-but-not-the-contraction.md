# Tail incidence already gives the differential but not the contraction

## Canonical graded promotion of a source arrow

Let the augmented tail operator be a source-authorized arrow

\[
D_s:E_s\longrightarrow F_s
\]

with its boundary domain included in the type. On the graded carrier

\[
\mathcal C_s=E_s^{\mathrm{even}}\oplus F_s^{\mathrm{odd}},
\]

define

\[
d_s=
\begin{pmatrix}
0&0\\
D_s&0
\end{pmatrix}.
\]

Then

\[
d_s^2=0
\]

formally and canonically. No new source operator is needed for nilpotence; it
comes from the ordered domain-to-codomain incidence.

This corrects the earlier formulation that asked the ungraded tail operator to
square to zero. It need not and generally does not.

## The genuinely missing reverse arrow

An odd reverse operator

\[
Q_s:F_s\longrightarrow E_s
\]

gives

\[
Q_s^{\mathrm{odd}}
=
\begin{pmatrix}
0&Q_s\\
0&0
\end{pmatrix}.
\]

Their supercommutator is block diagonal:

\[
d_sQ_s+Q_sd_s
=
\begin{pmatrix}
Q_sD_s&0\\
0&D_sQ_s
\end{pmatrix}.
\]

Thus the normal Cartan law requires two compatible identities:

\[
Q_sD_s=aN_E+B_E,
\qquad
D_sQ_s=aN_F+B_F,
\]

where `B_E,B_F` are the declared chain-level boundary incidences. The reverse
operator and both ordered composites are the actual missing constructors.

## Exact triangular finite model

Consider the source-shaped matrix

\[
D_{a,f}=
\begin{pmatrix}
a&f\\
0&1
\end{pmatrix}.
\]

Its polynomial complementary operator is

\[
Q_{a,f}=
\begin{pmatrix}
1&-f\\
0&a
\end{pmatrix}.
\]

Direct multiplication gives

\[
Q_{a,f}D_{a,f}
=D_{a,f}Q_{a,f}
=aI.
\]

The forcing entry `f` may be arbitrary; it cancels because the ordered
triangular source structure fixes the complementary arrow. For nonzero `a`,
`Q/a` is the inverse contraction. At `a=0`, the normal contraction degenerates.

This is the finite algebraic pattern sought from bilateral theta/Tate sewing.

## Mixed-diagonal falsifier

Replace the normal diagonal entry by

\[
a+r(t).
\]

The same complementary construction yields

\[
QD=DQ=(a+r(t))I.
\]

Any nonzero tangential residual in the normal diagonal tilts the degeneration
locus away from the seam. Off-diagonal forcing is harmless in this model;
normal-diagonal leakage is decisive.

## Relation to the actual tail operator

The augmented source operator has triangular form

\[
\mathcal D_s=
\begin{pmatrix}
\partial_q+s&f(q)\\
0&\partial_q
\end{pmatrix}.
\]

This already provides the ordered forward incidence and hence the two-term
differential. But the finite adjugate formula does not transfer automatically
to unbounded differential operators with boundary domains. The candidate
reverse arrow must encode:

- Green propagation;
- both endpoint conditions;
- the reciprocal tail;
- seam incidence;
- primitive and square currents;
- archimedean completion.

Constructing it by the inverse boundary problem would be equivalent to
assuming zero-freeness. It must arise polynomially or functorially from the
doubled source operations, as the finite `Q_{a,f}` does.

## DPC

Require:

1. exact domain and codomain of each tail incidence;
2. the canonical two-term grading;
3. an independently source-derived reverse arrow;
4. both ordered composites on their common domains;
5. the normal number operator and boundary blocks;
6. cancellation of off-diagonal forcing before scalar expectation;
7. absence of tangential leakage in the normal diagonal;
8. completion-stable closedness and contraction bounds.

Reject:

- squaring the ungraded tail operator and calling the result a differential;
- defining the reverse arrow as the inverse completed boundary problem;
- using a finite adjugate without an infinite-domain analogue;
- checking only one of `QD` and `DQ`;
- scalar cancellation that hides an operator block residual;
- a normal diagonal `a+r(t)` with nonzero `r`.

## Verdict

The source-derived tail operator has already solved the parity and nilpotence
part of the graded promotion once treated as an ordered incidence. The
remaining RH-bearing constructor is the source-derived reverse arrow whose two
composites reduce to signed normal displacement plus typed boundary incidence.

