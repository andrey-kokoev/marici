# 2126 — The Triple Deletion Port Produces a Source-Derived Incidence Sextic

> **Superseded by Entry 2129.** The sextic is the mathematically valid
> restriction of the Cayley--Menger determinant to three equations, but those
> equations come from three different additive sectors. The frozen source does
> not define their simultaneous fiber product. Calling the sextic
> source-derived coefficient incidence was a typing error.

## Hard-to-vary claim

Imposing all three translated deletion normals produces a new external sextic, but it is canonically the restriction of the existing Cayley--Menger divisor. It is not the homogeneous source quartic \(\mathcal Q\) and does not require a new Carrier stratum.

## Frozen incidence

The three equations

\[
E_T+2y_{12}=E_T+2y_{23}=E_T+2y_{31}=0
\]

fix

\[
A=B=C=\frac{E_T^2}{4}.
\]

No loop coordinate remains. Substituting this section into the frozen Cayley--Menger determinant gives

\[
K\big|_{A=B=C=E_T^2/4}
=-rac12\widetilde{\mathcal Q}_3,
\]

where

\[
\boxed{
\widetilde{\mathcal Q}_3
=
E_T^2\Lambda(p_1,p_2,p_3)
+4p_1p_2p_3,
\qquad p_i=P_i^2.
}
\]

## Type and comparison

`\widetilde{\mathcal Q}_3` is homogeneous of physical degree six. The source algebraic-letter \(\mathcal Q\) is a degree-four polynomial in homogeneous site energies. Their degrees and source variables differ, so they are not the same typed object.

After imposing `P_i=X_i` and `E_T=X_1+X_2+X_3`, exact factorization does not reduce the sextic to the published quartic times a source-fixed linear or quadratic carrier factor.

## Interpretation

This is the first progressive result of the enlarged deletion-port microprogramme:

\[
\boxed{
\text{existing Cayley--Menger carrier}
\xrightarrow{\text{triple translated-port section}}
\text{new source-derived external sextic}.
}
\]

The polynomial is new as a coefficient/readout incidence equation, not as a Carrier divisor. It predicts an independently testable analytic-continuation locus without repairing the old \(\mathcal Q\) hypothesis.

## Physical qualification

The section uses

\[
y_{12}=y_{23}=y_{31}=-E_T/2,
\]

so it does not meet the literal positive loop chamber for `E_T>0`. Physical activation would require an analytically continued relative cycle and must be tested independently.

## Verification

The exact determinant construction and specialization are in

`research/benincasa/marici-gm/src/bin/three_site_deletion_landau.rs`.

## Next falsifier

Test whether `\widetilde{\mathcal Q}_3=0` carries any coefficient-rank loss or monodromy in the triple-deleted contact-sector period. Then test whether the source Cayley--Menger relative cycle can reach the triple section under the admitted analytic continuation.

Three outcomes remain distinct:

1. no coefficient variation: the sextic is an apparent incidence equation;
2. coefficient variation but no physical cycle: sector-specific coefficient support without physical activation;
3. nontrivial relative-cycle pairing: a genuine correlator singularity on the unchanged Carrier.
