# 1100 — The Second Exceptional Cover Normalizes to an Existing-Support Node

## Record

Entry 1099 found that the second rank-twelve exceptional center begins with
the doubled branch

\[
W^2=4T^2,
\qquad
T=3-s-2A
\]

on the \(p\neq0\) chart.  The normalization/conductor model is now derived
from the next exact radial coefficient.

Sequence claim: `seqclaim-9371d13bb9be8b0bac70b34a`.

## Normalized node coordinates

Set

\[
X=W-2T,
\qquad
Y=W+2T.
\]

Since the strict-transform branch equation has the form

\[
W^2=4T^2+pK_3+p^2K_4+\cdots,
\]

the complete local equation becomes

\[
\boxed{
XY=pU,
}
\]

where

\[
U|_{p=0,T=0}=-16s(B-1).
\]

Away from \(s(B-1)=0\), this is the standard semistable node.  Its special
fiber is the union \(X=0\) and \(Y=0\), and the conductor is their labelled
intersection.

## Marked-wall restriction

On the conductor plane \(T=0\), exact substitution gives

\[
\boxed{
L_1|_{T=0}=B-1,
\qquad
L_2|_{T=0}=1.
}
\]

Thus the conductor meets the first marked wall, while the second marked wall
is a unit.  The only failure of the generic node model occurs on

\[
s=0
\qquad\text{or}\qquad
B-1=0,
\]

both already declared carrier supports.

## Deutsch--Popperian verdict

The conjecture that normalization of the doubled branch exposes an additional
marked or branch divisor is falsified.  The normalization is semistable away
from the existing \(q=0\) and \(L_1\) supports, and \(L_2\) disappears from
the conductor geometry as a unit.

Therefore the second center currently has the typed local form

\[
\boxed{
\text{two normalized coefficient sheets}
\xleftarrow{\text{conductor}}
\text{existing }(q=0)\cup(L_1=0)\text{ support}.
}
\]

No new carrier incidence is required.

## Epistemic status

- source branch and radial coefficients: exact characteristic-zero algebra;
- node factorization and wall restrictions: exact Symbolica assertions;
- conductor-local rank-twelve quotient and connection: not yet computed;
- new carrier datum: none.

## Evidence

- `research/benincasa/marici-gm/src/bin/rank12_u2v0_newton.rs`;
- `research/benincasa/rank12-u2-v0-joint-newton.json`.

Epistemic graph admission:
`ev-000000000799-47608461-9926-4115-a9ab-24834216680c`.

## Next falsifier

Construct the conductor-local source complex with its two normalized sheet
restrictions and their difference map.  Apply the twelve derived Rees shifts
from Entry 1099, then compute the kernel/cokernel and induced connection away
from and on \(s(B-1)=0\).  Any surviving class must be classified as sheet
anti-invariance, existing-support coefficient data, or genuinely new carrier
structure before physical interpretation.
