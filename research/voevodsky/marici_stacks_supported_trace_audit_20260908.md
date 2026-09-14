# Stacks Project audit for the missing supported trace

Date: 2026-09-08

## Sources checked

The Stacks Project search was queried for dualizing residues, local duality and trace maps. The directly relevant entries are:

- Tag `08XG`, Chapter 47, *Dualizing Complexes*;
- Tag `0A7A`, Section 47.15, *Dualizing complexes*;
- Tag `0A7M`, Section 47.16, *Dualizing complexes over local rings*;
- Tag `0A81`, Section 47.18, *The local duality theorem*;
- Tag `0A82`, Lemma 47.18.1, the local-duality statement for a normalized dualizing complex and closed point;
- Tag `0DWE`, Chapter 48, *Duality for Schemes*;
- Tag `0AU5`, Section 48.20, *Glueing dualizing complexes*;
- Tag `0BSY`, Section 49.4, *Traces for flat quasi-finite ring maps*.

## What these results provide here

For the Noetherian node and conductor, Stacks supplies the correct framework for:

1. representing support by `R Gamma_m` rather than by an informal pole;
2. retaining the nonsplit dualizing complex of the singular node;
3. identifying supported duality through a normalized dualizing complex;
4. constructing trace/counit maps when an appropriate duality morphism is present;
5. gluing branch dualizing data without first replacing it by its cohomology modules.

This supports the already computed normalization triangle and sixfold Koszul-Cech residue. In the regular ambient ring, the chosen order `(0,2,4,1,3,5)` and volume line give the normalized functional

\[
[1/(X_0X_2X_4X_1X_3X_5)]\longmapsto1.
\]

Local duality also explains why the natural target before choosing a coefficient/orientation identification is an injective-hull or dualizing object, not automatically the scalar ring.

## What it does not provide

The Stacks trace formalism does not produce, merely from the module complex `D_k`, a functional on

\[
R\Gamma_{\mathfrak m}\operatorname{Sym}_B((QD_k)^\vee).
\]

There are two separate integrations here:

- integration/residue in the six occurrence directions, which is available;
- integration in every formal fiber coordinate introduced by the symmetric algebra, which is not specified.

A dualizing trace for the total formal function algebra requires its relative dualizing/Berezinian line and a pushforward or support condition in the formal fiber directions. For polynomial even fiber coordinates there is no canonical coefficient-extraction trace invariant under arbitrary derivations. For odd finite-rank coordinates there is a Berezin top-coefficient functional only after choosing and orienting the determinant line. The strict complex contains both parity sectors and conductor-supported nonprojective terms, so neither a naive top exterior coefficient nor evaluation at the zero section supplies the requested trace.

Evaluation at the zero section is a valid augmentation, but because the formal homological vector field has no constant term it annihilates every Bruce product. It therefore cannot detect the desired P24 deformation.

## Exact conclusion

The missing datum is more specific than “a residue.” The occurrence residue exists. What is absent is a **relative dualizing orientation and supported pushforward for the formal fibers**, producing a map of the form

\[
R\Gamma_{\mathfrak m+\mathfrak f}
  (\mathcal O_k\otimes\omega_{\mathcal O_k/B})
\longrightarrow
R\Gamma_{\mathfrak m}(\omega_B)
\xrightarrow{\operatorname{Res}_{X_0,\ldots,X_5}}
C\Pi^{\otimes ?},
\]

where `f` is a declared fiber support ideal. One must then prove that the divergence of `Q_k` with respect to this relative orientation vanishes. Stacks can justify the duality and pushforward arrows once this geometry, support and orientation are supplied; it does not choose them.

Thus the next concrete construction is the relative Berezinian/dualizing line of a finite semi-free presentation of `QD_k`, together with a fiber-supported residue. Without finite perfectness or a specified completion, the infinite symmetric algebra does not carry the needed canonical trace.
