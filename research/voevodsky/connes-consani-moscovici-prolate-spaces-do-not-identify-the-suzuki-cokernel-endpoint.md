# Connes--Consani--Moscovici prolate spaces do not identify the Suzuki cokernel endpoint

## Newly inspected source

Alain Connes, Caterina Consani, and Henri Moscovici, *Zeta zeros and prolate wave operators*, Annals of Functional Analysis 15 (2024), article 87, DOI `10.1007/s43034-024-00388-z`.

The publisher endpoint initially returned an access-control page, but a broader CORE search identified the preprint as arXiv:2310.18423. The primary PDF was then downloaded and audited at `temp/connes-consani-moscovici-prolate.pdf`.

## What the paper constructs

The publisher abstract states that the paper:

- introduces a semilocal analogue of the prolate wave operator;
- uses the positive part of its spectrum for low-lying zeta-zero realization;
- uses the Sonin space associated with the negative spectrum for ultraviolet behavior;
- writes the archimedean prolate operator as the square of the scaling operator plus the grading of orthogonal polynomials;
- extends this formulation semilocally;
- proves stability of semilocal Sonin spaces as the finite set of places increases;
- relates those spaces to Hilbert spaces of entire functions;
- proposes a future metaplectic candidate rather than claiming completion of it.

This is genuine positive/self-adjoint spectral architecture, but the paper does not claim an unconditional positive factorization of the complete Weil form. Its introduction says explicitly that the operator-theoretic programme is to compare an automatically positive trace functional with the Weil functional, and that the proposed semilocal implementation is a strategy rather than a completed comparison theorem.

## Suzuki's primary-text comparison

Suzuki explicitly warns that the Connes--Consani--Moscovici de Branges spaces, denoted `B_S` in his discussion, and his own `H(E)` have “completely different properties.” He states that they are not isomorphic because their generators and spectral properties differ.

Therefore one cannot identify the semilocal Sonin/prolate space with

\[
\ker T_{\bar\Theta},
\qquad
\ker T_{\bar\Theta}^*,
\]

or with the minimal endpoint

\[
E=\ker L^*
\]

merely because both constructions involve entire-function Hilbert spaces and zeta spectra.

## Typing comparison

The two architectures currently have different roles:

| Suzuki Toeplitz complex | Semilocal prolate architecture |
|---|---|
| boundary symbol `Theta=E#/E` | finite-place semilocal scaling carrier |
| leakage `L` between Hardy sectors | self-adjoint prolate wave operator |
| kernel/cokernel harmonic boundary | positive/negative prolate spectral sectors |
| required exact Weil--`L2` isometry | spectral approximation/realization of zeta zeros |
| forbidden-divisor interpolation gate | stability of Sonin spaces under adding places |

No sourced arrow identifies the right column's negative prolate sector with the left column's Toeplitz cokernel. The paper's Theorem 4.6 instead proves a Hilbertian isomorphism

\[
\mathcal S(\mathbb R,e^\lambda)\cong\mathcal S(X_S,\lambda)
\]

between archimedean and semilocal Sonin spaces. Proposition 4.8 identifies these spaces with one common entire-function space `B`, but emphasizes that `B` inherits different inner products depending on the finite set of places. This is stability of the Sonin carrier, not equality with Suzuki's `H(E)` or its Toeplitz harmonic boundary.

## Radical quotient has the wrong homological role

The primary text identifies the radical of the compact-support Weil quadratic form with the range of an arithmetic map

\[
\mathcal E(f)(u)=u^{1/2}\sum_{n\ge1}f(nu)
\]

(on its stated even Schwartz domain). The low-lying construction conditions the scaling operator by quotienting or orthogonalizing against this range.

This cannot be identified formally with the Suzuki endpoint `ker L*`:

- `ran E` is declared null for the restricted Weil form;
- `ker L*` is the negatively graded cokernel retained by the Toeplitz complex;
- quotienting a radical removes zero-energy directions;
- completing a cokernel must account for a signed nonzero boundary contribution.

An isomorphism of the underlying Hilbert spaces would therefore still be insufficient. One would need a Green identity proving that the relevant prolate/Sonin sector carries the same graded arithmetic form.

## Why spectral-sign analogy is insufficient

The phrase “negative part of the spectrum” refers to a spectral projection of a self-adjoint prolate operator. It is still a positive Hilbert subspace with negative eigenvalues of that operator. By contrast,

\[
\ker L^*
\]

is a homological cokernel sector whose sign arises from grading in the Weil/Pontryagin boundary form.

These are not automatically the same kind of negativity. An identification must supply:

1. a unitary map between the two Hilbert sectors;
2. equality of their translation/scaling representations;
3. equality of endpoint multiplicities;
4. a Green identity matching the complete prime--gamma--endpoint pairing;
5. compatibility as the semilocal set of places grows.

Without these data, mapping “negative spectrum” to “negative harmonic degree” is an untyped analogy.

## Relation to the semilocal quotient audit

Prior repository work found that positive semilocal `L2` quotients either lose the analytic `Xi` cokernel or do not reproduce deterministic cross-prime Weil polarization. The prolate paper's stability under increasing finite place sets addresses an important directed-system issue, but the available abstract does not assert the missing global comparison identity.

In particular, stability of Sonin spaces is not the same as a compatible family of maps

\[
E_S\longrightarrow\ker L_S^*
\]

whose direct limit is isometric and whose endpoint norm equals the completed Weil correction.

## Exact theorem to search in the full text

A full primary-text audit should look for an identity of the form

\[
W_S(f*g^*)
=
\|P_{+,S}A_Sf\|^2-\|P_{-,S}A_Sf\|^2
\]

and a transition theorem preserving both terms as `S` grows. If present, its negative feature should be compared explicitly with the generalized-inner Blaschke model `K_B` and the Toeplitz cokernel `ker L*`.

Absent such an identity, the prolate construction is a spectral model, not the endpoint differential required by the Suzuki complex.

## Disposition

The primary-text audit provides a semilocal self-adjoint positive/negative spectral decomposition and stable Sonin spaces, but no theorem identifies its negative sector with Suzuki's cokernel endpoint or its pairing with the complete Weil form. Section 3.6 instead describes a quotient by the range of the arithmetic map `E`; Proposition 3.6 says that multiplication by the spectral variable on an entire-function quotient has the zeta zeros as spectrum. This is a spectral quotient statement, not positivity of the Weil quadratic form.

Moreover, Suzuki's own primary text explicitly rejects an isomorphism between the two de Branges-space constructions. The prolate route therefore remains a separate architecture until an exact intertwiner and Green identity are exhibited.
