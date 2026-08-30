# Entry 1604 — The Gaussian Cutoff Is a Carrier Domain, Not a Dyson-Invariant Profile Support

## Claim

The source condition that the initial Bogoliubov profile vanishes above the
EFT cutoff is not preserved as pointwise support under one-loop Dyson
evolution.  It is correctly typed as a restriction of the physical momentum
carrier.

## Finite support calculation

At first order in the state variation, the middle self-energy contains one
excited internal occurrence \(q\) and one vacuum occurrence
\(k=|\mathbf p-\mathbf q|\).  With

\[
0\le q\le\Lambda,
\qquad
0\le k\le\Lambda,
\]

the triangle incidence relation gives the external support

\[
0\le p\le2\Lambda.
\]

Consequently every \(p\) in the admitted EFT observation domain
\([0,\Lambda]\) has explicit internal witnesses and may receive a
state-dependent correction.  This remains true where the original
tree-coordinate \(\beta_p\) vanishes.

## Typed conclusion

\[
\boxed{
\text{Dyson preserves the CTP/Keldysh coefficient object over the cutoff
carrier, not pointwise }\operatorname{supp}\beta.
}
\]

No output above the EFT domain is asserted.  The formal support up to
\(2\Lambda\) only proves that convolution does not preserve the tree-level
profile filtration.

## Architectural update

The general Gaussian sector therefore has three distinct layers:

1. the momentum/incidence carrier restricted to the EFT domain;
2. the rank-three CTP/Keldysh coefficient object;
3. tree-level Gaussian coordinates and their Hadamard/cutoff filtration.

Only the first two are candidates for functorial interacting preservation.

## Next falsifier

Project the corrected rank-three CTP object back to effective Bogoliubov and
statistical coordinates at fixed external momentum.  Test whether that
projection is canonical or depends on a choice of time slice/primitive.

## Artifacts

- `research/benincasa/checkers/gaussian_dyson_support_spread.rs`
- `research/benincasa/results/gaussian-dyson-support-spread.json`
- `research/benincasa/gaussian-dyson-support-spread.md`

Allocator claim: `seqclaim-b3523aa8f103da85684d21bc`.
