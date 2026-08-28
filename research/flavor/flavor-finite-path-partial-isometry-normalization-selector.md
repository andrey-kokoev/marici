# Finite-Path Partial-Isometry Normalization Selector

## Question

Can a source algebra eliminate WP851's holomorphic coefficient fiber rather
than tuning the coefficients of independently normalized spurions?

## Finite charged path

Let (H=\mathbb C^4) have ordered orthonormal vertices
(e_0,e_1,e_2,e_3), number operator

\[
N=\operatorname{diag}(0,1,2,3),
\]

and forward creation operator

\[
C=e_1e_0^*+e_2e_1^*+e_3e_2^*.
\]

It satisfies

\[
[N,C]=C,
\qquad
C^*C=I-P_3,
\qquad
CC^*=I-P_0,
\qquad
C^4=0.
\]

The source descendants are (C^je_0=e_j). Their relative norms and
multiplication coefficients are one before any fitted scalar potential is
written.

## Exact uniqueness theorem

Every degree-one operator obeying ([N,T]=T) is a weighted shift

\[
T=w_0e_1e_0^*+w_1e_2e_1^*+w_2e_3e_2^*.
\]

The partial-isometry source relation

\[
T^*T=I-P_3
\]

forces (|w_0|=|w_1|=|w_2|=1). A diagonal unitary commuting with (N) and
fixing (e_0) removes all three phases. Therefore the complete admitted
operator fiber is one unitary orbit, not merely a locally rigid point.

This also collapses WP851's apparent extra quadratic channel. On the cyclic
source line,

\[
C^*C^3e_0=C^2e_0.
\]

Thus the path constructor makes the charge-two descendants relationally
identical instead of allowing an independent 
(\overline S_1S_3) coefficient.

## What this selects

If the flavor spurions are source-defined as the descendants

\[
S_j=C^je_0,
\]

then the primitive ray is fixed by the path incidence and the Fock metric.
No coefficient ratio (d/c), (f/e), or extra (g) remains. This is a
genuine normalization selector on the admitted finite-path representation
family.

It is not yet a selector on `physical16`. The required interface

\[
P_{\mathrm{path}}:
(H,N,C,e_0)\longrightarrow
\text{canonically normalized flavor operators}
\]

has not been derived from Standard Model flavor dynamics. Declaring
(S_j=C^je_0) without that interface would simply restrict the answer into
the source domain.

## Portal gates

The path partial isometry supplies a candidate source principle for the
previously free positive pairing and multiplication normalization. It does
not by itself establish:

- the orientation that couples this path asymmetrically to the two portal
  species;
- the physical normalization carrying unit path weight to the portal
  magnitude;
- the microscopic beta function or its global basin;
- survival of the path relation through symmetry breaking and thresholds;
- a calibrated map from path observables to `physical16` and detector units.

In particular, unitary uniqueness internal to the path is not evidence that
the physical flavor source realizes this path.

## Classification

Progressive algebraic selector, conditional on a finite-path Toeplitz source
constructor. It eliminates WP851's coefficient fiber by a full-orbit theorem,
not by fitting a scalar. The remaining decisive gate is the physical
interface (P_{\mathrm{path}}) and its joint transport through RG, thresholds,
and readout.

## Verification

Run:

```text
uv run --with sympy python research/flavor/checkers/wp852_finite_path_partial_isometry_normalization_selector.py
```
