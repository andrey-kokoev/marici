# The P4 endpoint readout is alternating under all frame permutations

## Test

Permute the four prime axes \((2,3,5,7)\) in all 24 ways. For each ordered frame, reconstruct from scratch:

- its logarithmic half-line shifts;
- the ordered residuals \(K_{q,p}\);
- the antisymmetric two-cochain \(\mathcal F_{ij}\);
- the Pfaffian-signed four-cup \(\mathcal Q_4\);
- endpoint evaluation at zero.

No output ratio or sign is supplied to the calculation.

## Result

Every permutation produces exactly one evaluation coordinate. The underlying positive coordinate is always

\[
\log\frac{3\cdot7}{2\cdot5}=\log\frac{21}{10}.
\]

The coefficient is exactly the permutation orientation:

\[
\boxed{
\rho_0(\mathcal Q_4^{\sigma})
=
\operatorname{sgn}(\sigma)\,
\operatorname{ev}_{\log(21/10)}.
}
\]

There are twelve even permutations with coefficient \(+1\) and twelve odd permutations with coefficient \(-1\).

Thus the earlier formula was not an accident of presenting the primes in ascending order. The half-line support conditions recover their magnitude order, while cubical orientation retains the orientation of the supplied frame.

## Geometric interpretation

The readout is an alternating four-frame covector. Relabelling axes does not produce arbitrary new ratios: it changes only orientation. Forgetting orientation leaves the invariant positive coordinate

\[
\frac{21}{10}.
\]

This behaves more like an oriented volume element than an ordinary projective cross-ratio. A classical cross-ratio generally moves among six values under permutations. Here the boundary order selects one chamber and the four-cup alternates over frame orientation.

For four increasing primitive scales

\[
x_0<x_1<x_2<x_3,
\]

the observed pattern predicts the chamber coordinate

\[
(x_1-x_0)+(x_3-x_2)
\]

in logarithmic variables, equivalently

\[
\frac{p_{(1)}p_{(3)}}{p_{(0)}p_{(2)}}
\]

in multiplicative variables, with the sign supplied by the orientation of the original frame. The general four-positive-scale theorem remains to be proved; the present exhaustive result establishes it for this prime frame.

## Consequence

The four-dimensional object has two independent components:

1. **metric chamber data**, supplied by the boundary ordering of logarithmic lengths;
2. **orientation data**, supplied by the alternating cubical four-cup.

Their combination is invariant under even relabelling and sign-reversing under odd relabelling. This is the expected transformation law of a determinant-line element.

## Verification

Run:

```text
python research/coherence/check_p4_permutation_covariance.py
```

Artifacts:

- `check_p4_permutation_covariance.py`
- `p4-permutation-covariance.v1.json`
