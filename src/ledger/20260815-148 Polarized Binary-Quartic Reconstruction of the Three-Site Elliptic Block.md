---
authors:
  - marici.Benincasa
---
# Polarized Binary-Quartic Reconstruction of the Three-Site Elliptic Block

## Record

Date: 2026-08-15

Status: conditional theorem on the published homogeneous slice; the exact symbolic derivation is recorded, but an independent executable certificate has not yet been admitted.

This entry semantically corrects the normal-order conclusion of entry 145. It preserves entry 145's identification of the homogeneous rank-two elliptic coefficient system, but withdraws the claim that ellipticity first appears at second normal order.

## Claim

Let

\[
X_1=a\lambda,
\qquad
X_2=\lambda,
\qquad
X_3=1,
\]

and define

\[
A=(a-1)^2\lambda^2-1,
\qquad
B=(a+1)^2\lambda^2-1,
\qquad
h=(a^2+1)\lambda^2-1.
\]

The highest homogeneous tangential part of the source-native deleted-edge Cayley--Menger geometry is the binary quartic

\[
F(t,\lambda)
=a^2\lambda^2t^4-ht^2+\lambda^2.
\]

Its double cover

\[
E_{a,\lambda}:\quad w^2=F(t,\lambda)
\]

has Legendre modulus

\[
m=\frac BA
\]

This is the reciprocal of entry 145's convention \(m_{145}=A/B\).
The change \(m=m_{145}^{-1}\) is a standard Legendre branch-point
permutation, so the two presentations define equivalent variations; the
normalization and local-monodromy formulas below use the present \(B/A\)
coordinate.

and the natural normalization of its holomorphic differential supplies the Kummer factor \(B^{-1/2}\). Its algebraic Gauss--Manin system is therefore

\[
\boxed{
V_{\mathrm{ell}}
\simeq
\mathcal K_{B^{-1/2}}\otimes m^*\mathbb H_{\mathrm{Leg}}.
}
\]

On the homogeneous slice, direct Griffiths reduction reproduces the complete published second-order operator \(L_2\), not merely its modulus. After a rational gauge, the resulting first-order connection is traceless and preserves a constant alternating form. Its Wronskian is proportional to

\[
\frac1{\lambda AB}.
\]

The pure elliptic degeneration is controlled by

\[
AB(A-B)=0,
\]

whereas the source algebraic-letter quartic \(\mathcal Q\) is absent from the pure elliptic connection. Thus

\[
\boxed{
AB(A-B)=0\text{ is elliptic degeneration,}
\qquad
\mathcal Q=0\text{ is extension or marked-section support.}
}
\]

## Physical monodromy at \(B=0\)

The Legendre factor contributes semisimple monodromy \(-1\) at the physical
\(B=0\) degeneration in this normalization. The Kummer factor
\(B^{-1/2}\) contributes a second \(-1\). These signs cancel in the
tensor product, leaving total unipotent monodromy

\[
\boxed{
T=\exp N,
\qquad
\operatorname{rank}N=1,
\qquad
N^2=0.
}
\]

Thus the rank-one nilpotent Picard--Lefschetz residue is the logarithm of the
total twisted monodromy; no residual semisimple sign remains.

## Semantic correction to entry 145

For the elliptic curve family itself,

\[
\partial_{E_T}C_{E_T}\big|_{E_T=0}\neq0.
\]

It has a nonzero first-order Kodaira--Spencer class. The rank-one nilpotent nearby-cycle monodromy is its degeneration-theoretic realization.

What vanishes at first normal order is instead the separate algebraic-letter quartic:

\[
\operatorname{gr}^{(1)}_{E_T}\mathcal Q=0,
\qquad
\operatorname{gr}^{(2)}_{E_T}\mathcal Q=-8X_1X_2.
\]

Therefore the statement in entry 145 that the first genuinely elliptic deformation occurs only at second normal order is false. A first jet can detect the elliptic Kodaira--Spencer deformation; it does not detect the first variation of \(\mathcal Q\).

This correction does not establish that first jets suffice for the complete integrated loop coefficient system.

## Evidence

The parallel Benincasa derivation records:

- the exact deleted-edge Cayley--Menger restriction and its homogeneous binary quartic;
- the branch-point cross-ratio \(m=B/A\);
- the \(B^{-1/2}\) normalization;
- exact Griffiths-reduction identities for a two-form de Rham basis;
- equality with the published \(L_2\);
- the Wronskian and preserved symplectic line;
- rank-one nilpotent Picard--Lefschetz residues at generic \(A=0\) and \(B=0\);
- the separation of the elliptic discriminant from \(\mathcal Q=0\).

Evidence source:

`temp/202608151032 Benincasa work to be put in ledger entries.txt`

SHA-256:

`1caac12b8565f8318ecafe76dce3507898788ac93cbd0750eb158787e98d7967`

The derivation is exact but currently embedded in a research transcript. Promotion from conditional to proved requires a compact executable or independently checkable symbolic certificate reproducing the identities above.

## Boundary

This entry proves no canonical embedding into the source four-dimensional master block.

It does not identify:

- the complementary rank-one factor \(L_1\);
- the complete multivariate \(4\times4\) connection;
- the full relative/Borel--Moore coefficient system;
- the spatial loop pushforward compatibility with the graphical Cut coaction.

It also does not identify the degree-two Jacobi block with the elliptic sector. The final transcript corrects that intermediate assignment: in the binary-quartic Brieskorn model the pure elliptic Milnor-character grade is the two-dimensional anti-invariant block, while the complementary two-dimensional block carries extension data.

## Consequence

The three-site result now supports the pipeline

\[
\boxed{
\text{carrier geometry}
\longrightarrow
\text{filtered coefficient object}
\longrightarrow
\text{flat physical subquotient}.
}
\]

No cosmology-specific carrier generator is required by the pure elliptic block. The remaining uncertainty is a coefficient-level embedding and extension problem.

## Outcome contract

```json
{
  "claim": "On the published homogeneous slice, the source-native q-cut Cayley-Menger binary quartic reconstructs the complete polarized elliptic Gauss-Manin module L2. The elliptic Kodaira-Spencer deformation is first order; only the separate algebraic-letter quartic has vanishing first normal grade.",
  "status": "conditional",
  "assumptions": [
    "Published homogeneous three-site source formulas and L2 normalization.",
    "The exact symbolic derivation in the cited transcript is correct.",
    "No claim beyond the homogeneous slice is made."
  ],
  "evidence_refs": [
    "temp/202608151032 Benincasa work to be put in ledger entries.txt sha256:1caac12b8565f8318ecafe76dce3507898788ac93cbd0750eb158787e98d7967",
    "ledger entry 145"
  ],
  "factorization_test": {
    "binary_quartic_modulus": "passed",
    "published_L2_reconstruction": "passed in recorded symbolic derivation",
    "polarization_and_Wronskian": "passed in recorded symbolic derivation",
    "first_order_Kodaira_Spencer": "passed",
    "entry_145_second_order_ellipticity_claim": "falsified",
    "four_block_embedding": "open"
  },
  "counterevidence": [
    "The derivation has not yet been packaged as an independently executable certificate.",
    "The source 4x4 connection and complementary rank-one factor are unpublished in the inspected materials."
  ],
  "next_experiment": "Package the binary-quartic Griffiths reduction as an exact certificate, then test the invariant rank-one quotient L1 of the last-three-master system."
}
```
