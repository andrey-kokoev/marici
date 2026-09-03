# Strict-load threshold from coherence and route balance

## Question

How much total physical route load is compatible with strict return when normalized coherence and route-load balance are known?

## Dimensionless parameters

For route-load bounds \(U,V\), define total load and balance

\[
S=U+V,
\qquad
\kappa=\frac{2\sqrt{UV}}{U+V}.
\]

Here \(0\le\kappa\le1\); equal loads give \(\kappa=1\), while a rank-one load limit gives \(\kappa=0\).

If normalized parity defects give the coherence bound

\[
C\le\gamma\sqrt{UV},
\qquad 0\le\gamma\le1,
\]

the optimal route-Gram eigenvalue bound becomes

\[
\lambda_{\max}
\le
\frac{S}{2}
\left(1+
\sqrt{1-\kappa^2(1-\gamma^2)}
\right).
\]

## Exact threshold

Strict return is certified when

\[
S<
\frac{2}{1+\sqrt{1-\kappa^2(1-\gamma^2)}}.
\]

This separates three physical inputs: total normalization \(S\), load balance \(\kappa\), and parity-controlled coherence \(\gamma\).

## Limiting cases

For equal routes, \(\kappa=1\), the threshold is

\[
S<\frac{2}{1+\gamma}.
\]

Orthogonal equal routes permit any \(S<2\), whereas unit-coherent equal routes require \(S<1\).

For orthogonal routes with \(\kappa=3/5\), the threshold is \(S<10/9\). Thus orthogonality alone cannot recover the equal-route allowance when one route dominates.

At \(\kappa=0\), or at unit coherence \(\gamma=1\), the threshold reduces to

\[
S<1.
\]

This is the trace-only certificate and receives no improvement from parity information.

## Minimal closure data

A physical normalization bound on \(S\) is indispensable. A balance lower bound on \(\kappa\) and a coherence upper bound on \(\gamma\) can relax the required trace bound, but neither replaces it. The required source-to-physical chain is therefore:

1. route normalization gives \(S\);
2. relative route loads give \(\kappa\);
3. parity defects give \(\gamma\);
4. the displayed inequality certifies strict return.

The local arithmetic frame currently supplies none of the first two physical quantities.

## Verification

`research/aspect/checkers/check_load_coherence_balance_threshold.py` verifies equal orthogonal, equal half-coherent, imbalanced orthogonal, unit-coherent, and rank-limit thresholds using exact rational radicals.

## Disposition

The optimal dimensionless threshold is derived. It identifies total physical route load as the irreducible missing datum and quantifies exactly how balance and parity coherence can improve a supplied normalization bound.
