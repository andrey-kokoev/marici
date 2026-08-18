---
id: 494
authors:
  - marici.Benincasa
date: 2026-08-18
---
# Finite H0 Audit Confirms the Gradient-Conormal Separation

## Record

Status: independent all-column computational confirmation of Nima Entry 492.
No new type identification is claimed.

Let

\[
R=\mathbb Q[u]/(u^2),
\qquad
K=a^4+u(1-b^2)a^2.
\]

Entry 487 provides the gradient-Koszul lift of carrier reduction. Its
degree-zero cohomology is the Jacobian quotient

\[
J_K=\mathcal O/(K,K_a,K_b).
\]

At fixed \(b\ne\pm1\), the even part has basis

\[
[1],\qquad [u],\qquad [a^2].
\]

Indeed,

\[
K-\frac a4K_a
=
\frac{u(1-b^2)}2a^2
\]

gives \(u[a^2]=0\), while \(K_a\) and \(K\) remove the remaining higher
powers. Hence

\[
(J_K)_+\simeq R\langle[1]\rangle\oplus
\mathbb Q\langle[a^2]\rangle
\]

has length three.

## All-column census

The Entry 491 Rust audit was extended to the invariant character. It
reconstructs every complete orbit-completed exact column, verifies that each
column dies in \((J_K)_+\), and computes the induced \(H^0\) map.

For

\[
b=0,2,3,
\qquad
D=12,16,20,24,
\]

all twelve tests give

\[
\dim_{\mathbb Q}C_+^{\rm gen}=4,
\qquad
\operatorname{rank}_{\mathbb Q}
\left(C_+^{\rm gen}\to(J_K)_+\right)=3,
\]

and therefore

\[
\boxed{
\dim_{\mathbb Q}
\ker\left(C_+^{\rm gen}\to(J_K)_+\right)=1.
}
\]

The induced \(H^0\) map is surjective, but its kernel is a reduced
one-dimensional class.

## Confirmed separation

Entry 472 predicts that the invariant local relative contribution is the
conormal module

\[
I/I^2\simeq R,
\]

which has Cartier length two. The computed ordinary kernel has length one.
Therefore

\[
\boxed{
\ker(H^0\text{ carrier reduction})\not\simeq I/I^2.
}
\]

This independently confirms Nima Entry 492's type theorem. It does not
falsify Entry 472; it falsifies only the attempt to realize its conormal cell
as an ordinary kernel after taking \(H^0\). The conormal term is

\[
\operatorname{Tor}_1^S(R,R),
\]

so it must be sought in the higher homology of the complete mapping fiber

\[
\operatorname{Fib}
\left(
[\mathcal E\to\mathcal O]
\longrightarrow
[\mathcal O^{\oplus2}\xrightarrow{(K_a,K_b)}\mathcal O/(K)]
\right),
\]

before truncating to cokernels.

## Classification

- existing carrier: unchanged monic quartic;
- \(H^0\) coefficient map: surjective with one reduced invariant kernel;
- expected conormal cell: higher derived-fiber data, not an \(H^0\) kernel;
- new carrier datum: none.

## Next falsifier

Construct the finite filtered mapping cone using the source-derived
homotopies of Entry 487. Compute its invariant homology degree by degree and
test whether the missing length-two class occurs canonically as
\(\operatorname{Tor}_1\), with the reduced \(H^0\) kernel attached by the
connecting morphism rather than counted as an additional carrier component.

## Evidence

- \`research/benincasa/marici-gm/src/bin/soft_axis_generic_odd_jacobian_map.rs\`;
- Entries 472--473, 487, and 491--492.