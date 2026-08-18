---
id: 487
authors:
  - marici.Benincasa
date: 2026-08-18
---
# The Gradient Koszul Homotopy Lifts Carrier Reduction Derivedly

## Record

Status: canonical all-sector nullhomotopy for the obstruction of Entry 485;
the generic relative fiber remains to be computed.

Let

\[
m=fL_1^{e_a}L_2^{e_b}
\]

in any frozen exact sector and either deck lattice. The complete operators
have the form

\[
p=(\text{coefficient})K+\frac32mK_b,
\qquad
q=(\text{coefficient})K-\frac32mK_a.
\]

Therefore, after reduction modulo the full quartic,

\[
\boxed{
p\bmod K=\frac32mK_b,
\qquad
q\bmod K=-\frac32mK_a.
}
\]

This identity is exact in \(u\), not restricted to the dual-number example
of Entry 485.

## Source-derived homotopy

Use the gradient Koszul differential

\[
d_K:\mathcal O^{\oplus2}\longrightarrow\mathcal O/(K),
\qquad
d_K(A,B)=AK_a+BK_b.
\]

Then

\[
H_p=\left(0,\frac32m\right),
\qquad
H_q=\left(-\frac32m,0\right)
\]

satisfy

\[
d_KH_p=p\bmod K,
\qquad
d_KH_q=q\bmod K.
\]

Thus every complete exact generator maps to a boundary. The obstruction in
Entry 485 is cancelled without a basis choice, splitting, or fitted
coefficient.

## Consequence

Carrier reduction lifts naturally only after replacing the bare coefficient
module by the source-defined derived hypersurface target

\[
\left[
\mathcal O^{\oplus2}
\xrightarrow{(K_a,K_b)}
\mathcal O/(K)
\right].
\]

The naive map to \(\mathcal O/(K)\) alone remains invalid. The added degree is
not a new carrier cell: it is relative de Rham/Koszul data forced by the
frozen equation \(K=0\).

Entry 486 finds one flat odd line and one reduced resonance line at generic
interior points before this correction. The present result constructs the
map needed to decide their roles, but does not yet compute its relative
fiber.

## Classification

- carrier: unchanged monic quartic family;
- correction: source-derived gradient Koszul homotopy;
- Entry 485 obstruction: canonically nullhomotopic;
- remaining ambiguity: image of the generic flat odd line;
- new carrier datum: none.

## Next falsifier

At generic \(b\ne\pm1\), evaluate the lifted map on explicit representatives
of

\[
C_-^{\rm gen}\simeq
\mathbb Q[u]/(u^2)\oplus\mathbb Q.
\]

Test whether the flat summand maps with rank one to the odd quartic carrier
while the reduced summand is its kernel. Failure leaves a genuine interior
extension class in the relative fiber.

## Evidence

- \`research/benincasa/marici-gm/src/bin/soft_axis_gradient_koszul_lift.rs\`;
- Entries 447, 452, 466, 485, and 486.
