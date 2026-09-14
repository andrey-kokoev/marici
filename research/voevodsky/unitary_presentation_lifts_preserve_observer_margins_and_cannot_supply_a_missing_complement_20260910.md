# Unitary presentation lifts preserve observer margins and cannot supply a missing complement

## Question

Can a line-valued or metaplectic presentation lift repair the loss of a lower margin in a compact analytic observer?

## Claim boundary

No when the lift acts by unitary source and target equivalences, tensoring with a unitary line, or finitely many scalar-phase aliases of the same source map. These constructions preserve singular values up to an explicit finite multiplicity factor and preserve compactness. They can retain symmetry-extension data but cannot become a complementary observer of previously invisible carrier directions. Arbitrarily rotated source copies are excluded: they can detect new directions and therefore have the role of additional observers.

## Problem

Let

\[
A:X\to Y
\]

be a bounded analytic observer. A presentation lift may attach a phase line or replace \(A\) by conjugate copies associated with presentation charts. It is tempting to treat the enlarged presentation as new observational information.

## Bold conjecture

A unitary metaplectic or line-valued lift of a compact analytic observer can restore stable reconstruction without an independent observer.

## Named rivals

1. Unitary equivalence preserves the lower modulus exactly.
2. Tensoring by a one-dimensional unitary line changes presentation but not singular values.
3. A finite family of unitary aliases can repair the lower margin.
4. An infinite family of genuinely distinct probes might supply a frame, but that is a new observer rather than bookkeeping.

## Lower modulus

Define

\[
m(A)=\inf_{\|x\|=1}\|Ax\|.
\]

Stable reconstruction by \(A\) is equivalent to

\[
m(A)>0.
\]

## Theorem 1: unitary transport invariance

Let \(U:X'\to X\) and \(V:Y\to Y'\) be unitary. Set

\[
A'=VAU.
\]

Then

\[
m(A')=m(A),
\]

and \(A'\) is compact exactly when \(A\) is compact.

### Proof

The unit spheres correspond under \(U\), and \(V\) preserves norms:

\[
\|A'x'\|=\|AUx'\|.
\]

Compactness is invariant under composition with bounded operators and recovered by composing with the unitary inverses.

## Theorem 2: tensoring by a unitary line

Let \(L\) be a one-dimensional Hilbert space and define

\[
A_L=A\otimes I_L:X\otimes L\to Y\otimes L.
\]

Then

\[
m(A_L)=m(A),
\]

and compactness is preserved.

After choosing a unit vector in \(L\), the tensor products are unitarily identified with \(X\) and \(Y\). Changing that vector multiplies coordinates by a phase and does not alter the statement.

Thus a noncanonically trivialized phase line may matter for coherence while remaining invisible to the observer norm.

## Theorem 3: finite unitary aliases

Let

\[
A_j=V_jAU_j,
\qquad 1\le j\le N,
\]

where \(U_j\) and \(V_j\) are unitary, and suppose the source identifications are presentation aliases of the same source direction. Define

\[
\mathcal A x=(A_1x,\ldots,A_Nx).
\]

If \(U_j=U_1R_j\) with \(R_j\) preserving the norm and satisfying \(AR_j\) unitarily equivalent to \(A\), then each component has the same lower modulus as \(A\). In particular, when the aliases differ only by scalar phases,

\[
\|\mathcal A x\|^2=N\|Ax\|^2,
\qquad
m(\mathcal A)=\sqrt N\,m(A).
\]

Therefore

\[
m(A)=0
\quad\Longrightarrow\quad
m(\mathcal A)=0.
\]

If \(A\) is compact and \(N<\infty\), then \(\mathcal A\) is compact and cannot be bounded below on an infinite-dimensional source.

## Kernel consequence

For scalar-phase aliases,

\[
\ker\mathcal A=
\ker A.
\]

The aliases add presentation multiplicity but no new detected source direction. A genuine complement \(D\) must instead satisfy a lower bound on sequences for which \(Ax_n\to0\).

## Restriction consequence

Restricting a group representation to a subgroup changes the declared symmetry family but not the underlying operator \(A\), source norm, or target norm. Therefore restriction alone preserves \(m(A)\). The enriched comparison by the unitary fold \(C_u\) also preserves it.

Hence the chain

\[
\operatorname{Rep}(C_4)
\xrightarrow{\operatorname{Res}}
\operatorname{Rep}(C_2)
\xrightarrow{C_u}
\operatorname{Rep}(C_{2,\rm rad})
\]

cannot improve analytic coercivity.

## Green/Real worked example

The canonical fold is unitary:

\[
C_u:L^2(\mathbb R)
\to
L^2(\mathbb R_+)\oplus L^2(\mathbb R_+).
\]

For an observer \(A\) transported to the radial carrier,

\[
A_{\rm rad}=C_uAC_u^{-1},
\]

we have

\[
m(A_{\rm rad})=m(A).
\]

The fold establishes

\[
C_uF^2=W_uC_u
\]

and transports the Real/Green cells, but it cannot turn compact Euler-to-theta loading into a bounded-below observer.

Likewise, a metaplectic phase line may retain quarter-turn coherence while leaving the lower modulus unchanged.

## Strongest falsification attempt

Take a compact diagonal observer

\[
Ae_n=a_ne_n,
\qquad
a_n\to0.
\]

Attach any finite family of phase aliases

\[
A_je_n=e^{i\theta_{j,n}}a_ne_n.
\]

Then

\[
\|\mathcal Ae_n\|^2
=N|a_n|^2
\longrightarrow0.
\]

No finite phase decoration restores a lower margin.

Rival 4 is not refuted: an infinite family of nonredundant probes can form a frame. But if the maps detect new source directions or carry nontrivial weights, they constitute a new observer constructor and must be typed as such. They are not a mere presentation lift.

## Constructor-role rule

A `presentation_lift` may change:

- symmetry-extension data;
- chart or polarization labels;
- line-valued coherence;
- projective cocycles.

A `complementary_observer` must change:

- the joint kernel, or
- the lower modulus on analytically invisible directions.

If a proposed lift is unitary-equivalent to the original observer and does neither, it cannot be promoted to the complementary-observer role.

## Disposition

The bold conjecture is rejected. Unitary presentation lifts preserve observer margins and compactness; finite phase aliases cannot supply missing stable information. The symmetry and observer layers therefore meet through a strict boundary: extension data may preserve presentation distinctions, while stable reconstruction requires genuinely new source-sensitive maps.
