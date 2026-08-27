# Exponential dichotomy does not control stable-bundle intersection

## Candidate architecture

The reciprocal half-planes naturally suggest two outward evolution laws. Each
has a stable bundle, and the completed scalar is modeled by the determinant of
their sewing map. A zero occurs when the two stable bundles fail to be
transverse.

This is the standard geometric shape of an Evans function. It correctly types
the scalar zero as a relationship failure rather than loss of either state.

However, exponential dichotomy in each sector does not control the
intersection divisor.

## Exact reciprocal-symmetric hostile

Let

\[
D=
\begin{pmatrix}
-1&0\\
0&1
\end{pmatrix}
\]

and fix the first stable line

\[
E_+=\operatorname{span}(e_1).
\]

Choose an off-seam parameter `a` and the reciprocal-symmetric polynomial

\[
p(z)=(z-a)(z-(1-a)).
\]

Define

\[
R(z)=
\begin{pmatrix}
1&0\\
p(z)&1
\end{pmatrix},
\qquad
A_-(z)=R(z)DR(z)^{-1}.
\]

Then

\[
A_-(z)=
\begin{pmatrix}
-1&0\\
-2p(z)&1
\end{pmatrix}.
\]

For every `z`, the eigenvalues remain exactly `-1` and `1`. The second sector
therefore has a perfect algebraic stable/unstable splitting, with stable line

\[
E_-(z)=\operatorname{span}(1,p(z))^T.
\]

The Evans determinant of the two stable lines is

\[
\det
\begin{pmatrix}
1&1\\
0&p(z)
\end{pmatrix}
=p(z).
\]

It vanishes at `a` and `1-a`, although neither sector loses its dichotomy and
the conjugating frame has determinant one everywhere.

## Meaning of the hostile

The divisor can be moved almost arbitrarily by changing the holomorphic
conjugating frame `R(z)` while preserving:

- the stable and unstable eigenvalues;
- the dimensions of both subbundles;
- invertibility of the full frame;
- reciprocal symmetry of the intersection divisor;
- local exponential rates.

Therefore spectral gaps, stable dimensions, and reciprocal pairing do not
orient the relative position of the two stable bundles.

## Categorical form

Let

\[
E_+(z)\oplus E_-(z)\longrightarrow H(z)
\]

be the seam sewing map. Its determinant section measures transversality. The
two sector objects and their internal dichotomies can remain completely valid
while this map loses invertibility.

Consequently, an unfillable higher cell at a zero is not forced by the two
sector dichotomies. It appears only if the source category restricts the
relative conjugating frame. The missing fifth-tower datum is a law on relative
position, not a law on either stable bundle separately.

## Surviving source laws

A viable theorem must forbid the hostile `R(z)` through independently derived
structure such as:

- a fixed source flag preserved by both sector transports;
- total positivity of the relative transfer matrix;
- a symplectic or Lagrangian monotonicity law with oriented crossing form;
- a passive scattering law constraining the graph transform;
- a source curvature equation for the relative frame;
- a boundary incidence map fixing the off-diagonal block `p(z)`;
- a completion-stable lower bound on the principal angle between the bundles.

Each candidate must be tested under reciprocal-symmetric conjugations before
scalar evaluation.

## DPC

For the theta/Tate dichotomy proposal, require:

1. source derivation of both stable bundles;
2. source derivation of the seam sewing map;
3. explicit typing of allowable frame conjugations;
4. a law constraining the relative off-diagonal graph coordinate;
5. proof that this law excludes reciprocal-symmetric intersection insertion;
6. completion-stable transversality.

Reject:

- stable eigenvalue gaps alone;
- fixed stable dimensions alone;
- full-frame determinant nonvanishing;
- reciprocal symmetry of the Evans determinant;
- a relative frame chosen using the desired zero-free result;
- finite transversality whose smallest principal angle collapses at completion.

## Verdict

Exponential dichotomy supplies the correct two-sector carrier but not the RH
orientation. The exact unresolved object is the source-derived relative-frame
law that forbids stable-bundle intersection off the seam.

