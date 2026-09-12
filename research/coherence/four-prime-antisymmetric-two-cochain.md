# A source-antisymmetrized window two-cochain has a nonzero four-cup

## Construction

The ordered half-line square residuals are

\[
K_{q,p}=R_qS_p-S_pR_q.
\]

Cubical orientation canonically supplies their alternating part:

\[
\mathcal F_{ij}=K_{j,i}-K_{i,j},
\qquad
\mathcal F_{ji}=-\mathcal F_{ij}.
\]

Unlike the earlier exterior-degree-zero operators \(c_i i_j\otimes K_{j,i}\), the assignment

\[
(i,j)\longmapsto\mathcal F_{ij}
\]

is explicitly a two-cochain on oriented prime faces, with values in half-line boundary operators.

## Closure

Let prime-edge transport act on coefficients by commutator with \(R_i\). For every triple,

\[
[ R_i,\mathcal F_{jk}]
+[ R_j,\mathcal F_{ki}]
+[ R_k,\mathcal F_{ij}]
=0.
\]

The checker verifies this on all four triples and every seam basis state. Thus \(\mathcal F\) is a covariantly closed operator-valued two-cochain.

## Four-cup

Because two-forms have even degree, use the symmetrized operator product while retaining Pfaffian orientation:

\[
\mathcal Q_4
=
\{\mathcal F_{01},\mathcal F_{23}\}
-
\{\mathcal F_{02},\mathcal F_{13}\}
+
\{\mathcal F_{03},\mathcal F_{12}\}.
\]

In the exact finite incidence model,

\[
\mathcal Q_4\ne0.
\]

Its left-boundary compression has rank four. Its full ordinary trace is zero, so once again the scalar diagonal readout discards the supported four-cell relation.

## Status

This closes the typing gap exposed by the prior null audit:

\[
\boxed{
\mathcal F\in C^2_{\rm cube}(\mathcal B),
\qquad
D_R\mathcal F=0,
\qquad
\mathcal F\smile\mathcal F\ne0.
}
\]

The construction is canonical relative to three declared choices already present in the source model:

1. ordered prime axes;
2. half-line shift and adjoint;
3. cubical alternation.

The remaining issue is completion, not finite incidence: replace integer shift proxies by the actual lengths \(\log p\), formulate the same operators on the common half-line graph domain, and test continuity of \(\mathcal Q_4\) in the projective prime rigging.

## Verification

Run:

```text
python research/coherence/check_four_prime_antisymmetric_two_cochain.py
```

Artifacts:

- `check_four_prime_antisymmetric_two_cochain.py`
- `four-prime-antisymmetric-two-cochain.v1.json`
