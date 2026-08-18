---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# The Fitting-Conic Enhancement Is a Canonical Rank-One Limit Quotient

## Question

Entry 390 established a simple rank-one enhancement on

\[
C_{\rm fit}:\qquad X_1X_2-E_T^2=0.
\]

A rank jump alone does not canonically separate the new direction from the
persistent exact-lift gauge plane. Test the hard-to-vary claim

\[
\boxed{\text{the generic rank-two gauge plane has no regular transverse
limit inside the rank-three conic fiber.}}
\]

No two-plane may be selected from the enhanced fiber after specialization.

## Frozen construction

On the \(X_1=1\) patch use

\[
u=E_T,\qquad v=\ell_3,\qquad
C_{\rm fit}:v=2u^2-u+2.
\]

At fixed \(u\), approach the conic in the source coordinate

\[
\tau=v-v_{\rm conic}(u).
\]

For each nonzero \(\tau\), take the source-defined homogeneous exact-lift
kernel and project it to the twelve master coordinates. Its generic
rank-two RREF chart has pivots \((3,4)\). Reconstruct every RREF coordinate
as a rational function of \(\tau\), then evaluate at \(\tau=0\).

This constructs the transverse limit of the generic plane. It does not choose
two rows from the rank-three special fiber.

## Exact result

Over \(\mathbf F_{2305843009213693951}\), test

\[
u=3,5,7,11,19,37
\]

at exact-form degrees \(8\) and \(10\), using 65 transverse samples per
fiber.

In all twelve tests:

\[
\operatorname{rank}G_{\rm lim}=2,
\qquad
\operatorname{rank}G_{C_{\rm fit}}=3,
\]

\[
\operatorname{rank}
\langle G_{\rm lim},G_{C_{\rm fit}}\rangle=3.
\]

Every transverse reconstruction is regular at \(\tau=0\); the largest
selected numerator and denominator degrees are \((1,0)\). Hence

\[
\boxed{
G_{\rm lim}\subset G_{C_{\rm fit}},
\qquad
\dim(G_{C_{\rm fit}}/G_{\rm lim})=1.
}
\]

The limit pivots are \((3,4)\). The additional special-fiber pivot is
column \(8\), namely \(e_6\) in the frozen basis

\[
(\Omega_{111},\Omega_{101},\Omega_{110},e_1,\ldots,e_9).
\]

The normalized extra representative has support mask \(3328\), exactly

\[
\boxed{\langle e_6,e_8,e_9\rangle,}
\]

with zero \(e_7\) coordinate. Its tested representatives agree identically
between exact-form degrees \(8\) and \(10\).

## Verdict

The tested claim is falsified:

\[
\boxed{
\mathcal L_{\rm fit}
:=
G_{C_{\rm fit}}/G_{\rm lim}
\text{ is a canonically typed rank-one quotient in the tested presentation.}
}
\]

This is stronger than a dimension jump: the persistent plane is obtained by
transverse specialization, and the new line is its quotient. The appearance
of the \(e_6\) pivot places the line in the same algebraic final-block sector
as the second-Rees bridge, but does not identify those objects.

## Classification

| Datum | Classification |
|---|---|
| \(C_{\rm fit}\) | internal coefficient Fitting divisor |
| \(G_{\rm lim}\) | persistent exact-lift gauge plane |
| \(\mathcal L_{\rm fit}\) | rank-one special-fiber coefficient quotient |
| support \((e_6,e_8,e_9)\) | algebraic final-block data |
| new carrier datum | none |

## Epistemic boundary

This finite-field result does not construct the induced connection on
\(\mathcal L_{\rm fit}\), prove its flat saturation, reconstruct a global
rational frame in \(u\), locate \(\mathcal Q\), establish an integral
lattice, or identify the physical relative chain.

## Next falsifier

Differentiate the complete homogeneous exact-lift relation along
\(C_{\rm fit}\), retaining its primitive coordinates. Reduce the derivative
modulo the persistent limit plane and exact boundaries. Test whether the
result preserves \(\mathcal L_{\rm fit}\) and therefore defines a rank-one
connection.

If it does, factor the nonintegral singular support of that connection and
test whether \(\mathcal Q\) occurs. If it does not, test whether the failure
is the extension class coupling \(\mathcal L_{\rm fit}\) to the elliptic
quotient. No carrier modification is admissible.

## Evidence

- `research/benincasa/marici-gm/src/bin/marked_tangency_support.rs`;
- `research/benincasa/gauge-fitting-conic-limit-line.json`;
- Entries 388--390.
