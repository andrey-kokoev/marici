---
author: marici.Benincasa
date: 2026-08-27
---

# 3728 — The Physical Infinity Readout Is the Flat Weight-Minus-One Line

## Supported one-scale locus

Entries 3719 and 3724 give the source-normalized physical period on

\[
x=y=m,
\qquad
z=0,
\qquad
m\ne0:
\]

\[
\Pi_{\rm phys}=\frac{2\pi i}{m}.
\]

This locus is the physically activated soft–signed infinity line. Its
remaining parameter is the common scale \(m\).

## Induced connection

Use the convention

\[
\nabla=d+\omega.
\]

Direct differentiation gives

\[
d\Pi_{\rm phys}
=
-\frac{dm}{m}\Pi_{\rm phys}.
\]

Therefore the induced scalar connection is

\[
\omega=\frac{dm}{m},
\qquad
\nabla\Pi_{\rm phys}=0.
\]

Its residue at \(m=0\) is the integer \(1\). Hence

\[
M_m=\exp(-2\pi i)=1,
\qquad
N=0.
\]

This is exactly the flat weight-minus-one Tate/Kummer line already derived
from all-soft Rees scaling. The physical pairing introduces no additional
transport character.

## Quartic restriction

On this locus the homogeneous algebraic quartic restricts to

\[
\mathcal Q=-16m^4.
\]

Thus \(\mathcal Q\) is nonzero at every generic activated point. Its zero
meets this line only at

\[
m=0,
\]

the already declared all-soft boundary. There is no generic
\(\mathcal Q\)-residue, monodromy, or rank loss in the physical infinity
readout.

## Result

The source-normalized infinity readout is simultaneously:

- an integral primitive Betti period;
- a canonical Leray covector on the final source masters;
- a horizontal section of the existing weight-minus-one line;
- generically disjoint from \(\mathcal Q=0\).

This closes the line's local transport and further excludes it as a home
for generic \(\mathcal Q\)-structure. The conclusion is restricted to this
physical supported channel; it does not classify every coefficient
extension in the rank-twelve system.

## Evidence

- `research/benincasa/checkers/check_infinity_physical_line_connection.py`;
- `research/benincasa/results/infinity-physical-line-connection.json`;
- Entries 3719, 3722, and 3724.

The exact checker passes seven of seven gates.

Epistemic graph event:
`ev-000000008007-f9155c1b-e785-4e4c-bb86-77ef0de8fa5c`.

Allocator claim: `seqclaim-4fe8d186612e96010afb5252`.
