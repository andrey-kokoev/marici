# 1633 — The Source Dyson No-Production Cell Balances the Labelled Cut Trace

## Question

Entry 1632 proves that the production Cut is completely positive but not trace-preserving by itself.  Does the frozen source supply the matching virtual/no-production term, or must one fit an anti-Hermitian correction?

## Source expansion

Entry 1616 fixes each production channel as

\[
C_r=-i(H_r-S_r).
\]

The same source exponential supplies the second-order no-production coefficient.  Writing the coherent Hamiltonian part separately,

\[
K_0
=
I-igH_{\rm coh}
-\frac{g^2}{2}
\left(
H_{\rm coh}^2
+\sum_r C_r^\dagger C_r
\right)
+O(g^3),
\]

and

\[
K_r=gC_r+O(g^2).
\]

Therefore

\[
\boxed{
K_0^\dagger K_0
+\sum_rK_r^\dagger K_r
=I+O(g^3).
}
\]

At second order, the negative virtual trace coefficient is exactly

\[
-\sum_rC_r^\dagger C_r,
\]

and the positive labelled Cut coefficient is its opposite.

## Endpoint coefficients and occurrence multiplicities

Channelwise,

\[
|H-S|^2
=|H|^2
-2\operatorname{Re}(H\bar S)
+|S|^2.
\]

Thus the algebraic norm coefficients are

\[
(1,-2,1).
\]

The unsigned location multiplicities remain

\[
(1,2,1).
\]

The mixed minus sign is carried by the source endpoint amplitude; it is not a negative occurrence multiplicity.

The checker verifies 2,401 exact complex endpoint packets.

## Narrow result

\[
\boxed{
\text{The source Dyson no-production cell and labelled Cut cell satisfy trace balance through second order without a fitted correction.}
}
\]

The produced covariance contribution remains positive; trace preservation arises only after adding the virtual normalization cell.

## Qualifications

- This is perturbative trace preservation through second order, not an all-order channel construction.
- The continuum statement uses the symmetric positive finite-EFT measure of Entry 1618.
- Renormalized cutoff removal remains untyped by Entry 1620.

## Architectural consequence

The finite-time coefficient calculus acquires the standard typed pair

\[
\text{no-production/virtual cell}
\oplus
\text{labelled production Cut cells},
\]

with their normalization relation inherited from one source exponential.  This is a coefficient-level optical-theorem structure over the existing occurrence carrier.

## Durable artifacts

- `research/benincasa/checkers/dyson_kraus_trace_balance.rs`
- `research/benincasa/results/dyson-kraus-trace-balance.json`
- `research/benincasa/dyson-kraus-trace-balance.md`

## Next falsifier

Test compatibility of this trace-balance identity with moment truncation:

\[
\operatorname{res}_{\le D}
\circ\Phi_{D+2}
\stackrel?=
\Phi_D
\circ\operatorname{res}_{\le D+2}.
\]

Retain the virtual and production cells together.  A failure would show that finite moment truncations do not form a strict channel tower and require a derived coherence map.
