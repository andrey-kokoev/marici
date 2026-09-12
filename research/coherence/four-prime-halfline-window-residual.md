# The four-prime source cube acquires nonzero mixed residuals on the half-line

## Setup

For \(a=\log p\), let

\[
(R_af)(x)=f(x+a)
\]

be the half-line left shift and let its adjoint be

\[
(S_af)(x)=
\begin{cases}
0,&x<a,\\
f(x-a),&x\ge a.
\end{cases}
\]

Then

\[
R_aS_a=I,
\qquad
S_aR_a=I-P_a,
\qquad
P_a=1_{[0,a)}.
\]

The source edge and its proposed contraction are

\[
d_p=c_p\otimes R_{\log p},
\qquad
h_p=i_p\otimes S_{\log p}.
\]

## Mixed square

For distinct primes \(p,q\), fermionic anticommutation gives

\[
d_qh_p+h_pd_q
=
c_qi_p\otimes K_{q,p},
\]

where

\[
K_{q,p}=R_{\log q}S_{\log p}-S_{\log p}R_{\log q}.
\]

This operator is not zero. Writing \(a=\log p\), \(b=\log q\):

\[
K_{q,p}=
\begin{cases}
P_aR_{b-a},&b>a,\\
1_{[a-b,a)}S_{a-b},&a>b.
\end{cases}
\]

Thus every ordered pair of distinct prime directions leaves a boundary strip. The checker verifies nonvanishing for all twelve ordered pairs from \(\{2,3,5,7\}\) using an explicit decaying test function.

## Correction to the single-axis contraction argument

For one axis,

\[
d_ph_p+h_pd_p
=I-(i_pc_p)\otimes P_p
\]

is valid on its corresponding two-term sector. It does not extend unchanged to

\[
d=\sum_p d_p
\]

with one selected \(h_p\), because all mixed terms \(d_qh_p+h_pd_q\) survive on the half-line.

The full line hides this issue: translations there are a commuting group, so \(R_bS_a=S_aR_b\). The boundary turns that strict group action into a Toeplitz-type action with nontrivial mixed commutators.

## Higher-incidence meaning

The decorated source has two layers:

1. the prime-creation differential satisfies \(d^2=0\), so its interior cubical boundary is flat;
2. the attempted contraction is not cubically natural at the half-line boundary.

The operators \(K_{q,p}\) are therefore genuine square-level coherence residuals. Cubes compare the transported \(K_{q,p}\) on their six faces, and the 4-cell compares those cube comparisons. The higher problem begins at the contraction/readout layer, not at prime multiplication itself.

This gives a concrete interpretation of the dimensional ladder:

\[
P^1=d_p,
\qquad
P^2=K_{q,p},
\qquad
P^3=\partial K\text{ on a prime triple},
\qquad
P^4=\partial(\partial K)\text{ with retained boundary typing}.
\]

The notation is schematic: the next calculation must use the cubical differential with the induced translations and Koszul signs, rather than applying an untyped second boundary and declaring it zero.

## Verification

Artifacts:

- `check_four_prime_halfline_windows.py`
- `four-prime-halfline-window-residual.v1.json`

Run:

```text
python research/coherence/check_four_prime_halfline_windows.py
```

All twelve ordered mixed residuals are nonzero.
