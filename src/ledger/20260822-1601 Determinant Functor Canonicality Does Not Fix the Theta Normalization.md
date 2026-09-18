---
id: 1601
date: 2026-08-22
title: Determinant Functor Canonicality Does Not Fix the Theta Normalization
draft: true
publication_note: Duplicate entry number; withheld pending ledger-number reconciliation.
---

# Determinant Functor Canonicality Does Not Fix the Theta Normalization

A rebuilt 4068-page reference search isolates exactly what determinant-functor
technology contributes to the six-point physical line.

Braverman--Kappeler, *Refined Analytic Torsion as an Element of the
Determinant Line*, pp. 7--8, gives the sign-refined canonical isomorphism
\[
  \phi_C:\operatorname{Det}(C^\bullet)\xrightarrow{\sim}
  \operatorname{Det}(H^\bullet(C)).
\]
For the based physical complex of Entry 436, whose ranks are
\((1,4,5,1)\), whose only homology is the primitive integral line
\(H_1=\mathbb Z z\), and whose road-oriented generator is
\(z=(1,0,1,0,0)\), this canonically fixes the determinant-of-cohomology
generator, including its odd-degree dualization convention.

Bismut--Gillet--Soulé further identify canonical Knudsen--Mumford sections for
acyclic complexes and exact triangles (Bott--Chern p. 3; Quillen pp. 34--38).
This confirms that the contractible conductor/road summands contribute
canonical unit sections and that cancellation to the surviving physical line
is functorial. Proper-base-change references in *Condensed Mathematics*
pp. 73--74 and DAG I pp. 312--315 place this determinant cancellation inside
the correspondence/six-functor formalism.

However none of these results identifies that canonical determinant generator
with an independently specified theta section. This is not a missing theorem
of determinant functors: in `RHReciprocalChartDeterminantCarrier.agda`,
`commonLine` is an arbitrary type, while in `DistinguishedThetaSection` the
map `section : Parameter -> commonLine` is explicitly extra data. Therefore no
construction from the physical complex alone can produce an equality with
that arbitrary section.

The exact frontier is consequently
\[
 \mathbb Z z
 \longrightarrow \operatorname{Det}H(C_{\rm phys})
 \quad\text{canonical and sourced},
\]
followed by
\[
 \operatorname{Det}H(C_{\rm phys})\longrightarrow L_\Theta
 \quad\text{requiring one normalization comparison}.
\]
The second arrow must come from the definition or analytic normalization of
the project-specific theta object. Calling the Knudsen--Mumford generator
"theta" would merely rename the missing comparison.

The page-15 refined-chirality construction is not applicable directly: it
requires paired ranks \(\dim C^j=\dim C^{3-j}\), whereas the middle physical
ranks are 4 and 5.
