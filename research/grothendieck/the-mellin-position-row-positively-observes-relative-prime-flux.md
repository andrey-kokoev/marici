# The Mellin position row positively observes relative prime flux

## Missing observer

The two-cone Toeplitz current at scale `L>0` is represented by the odd
distribution

\[
j_L=\delta_L-\delta_{-L}.
\]

Every even scalar theta probe `Phi` annihilates it:

\[
\langle j_L,\Phi\rangle
=\Phi(L)-\Phi(-L)
=0.
\]

Thus scalar theta evaluation cannot observe the arithmetic relative class,
even when that class is nonzero.

## Source-derived odd channel

Let `Q` be multiplication by the logarithmic scale coordinate:

\[
(Q\Phi)(q)=q\Phi(q).
\]

This operator is already source-derived as the generator conjugate to Mellin
character transport. If `Phi` is even, `Q Phi` is odd, and

\[
\langle j_L,Q\Phi\rangle
=L\Phi(L)-(-L)\Phi(-L)
=2L\Phi(L).
\]

For the positive theta profile and `L>0`, this pairing is strictly positive.
It is the smallest archimedean observer that detects the anti-diagonal prime
flux without erasing its orientation.

At prime-power depth `k`, put

\[
L_{p,k}=k\log p.
\]

Then

\[
\langle j_{L_{p,k}},Q\Phi\rangle
=2k(\log p)\Phi(k\log p).
\]

When combined with the connected cyclic coefficient `1/k`, the exponent
cancels once again:

\[
\frac1k
\langle j_{L_{p,k}},Q\Phi\rangle
=2(\log p)\Phi(k\log p).
\]

This is the smooth archimedean realization of the same boundary-index law
that produced the von Mangoldt coefficient.

## Why a second row is mandatory

Under Fourier transform, position and derivative exchange, up to the fixed
normalization constants and phase:

\[
\mathcal FQ\mathcal F^{-1}\sim D,
\qquad
D=\partial_q.
\]

Therefore `Q` alone is not a Fourier-stable observer. The minimal completed
archimedean port is the phase-space graph pair

\[
(Q,D).
\]

This matches the independently obtained two-sided leakage theorem: `Q`
controls omitted-to-visible transport, while `D` controls
visible-to-omitted transport. Here the same pair acquires a direct semantic
role:

- `Q` turns even theta density into an odd test that detects relative prime
  flux;
- `D` is its Fourier-dual wall-current channel.

Neither row may be replaced by an extra scalar endpoint value.

## Correct constructor order

The atomic current `j_L` is a covector, not an `L2` state. The derivative must
not be applied directly to it. The typed construction is

```text
prime-power packet
    -> relative atomic flux
theta source
    -> smooth Mellin–de Rham graph state
pair flux with the Q/D graph rows by duality
```

For fixed finite packets, the `Q` pairing above is exact. Global completion
still requires continuity of the moving prime-power flux in the common graph
dual. The existing fixed-window bounds do not imply this uniform statement.

## Falsifiers

1. Pairing the odd flux only with the even theta scalar.
2. Applying `D` to the atomic current as though it were a Hilbert vector.
3. Keeping `Q` without its Fourier-dual `D` row.
4. Claiming uniform restricted-product continuity from fixed finite packets.
5. Inferring zero confinement from positivity of the finite `Q` pairing.

## Result

The missing finite archimedean observer exists. Mellin position turns the even
positive theta profile into an odd probe and pairs strictly positively with
every oriented prime-power flux atom. Together with its Fourier-dual de Rham
row, it forms the minimal source-derived phase-space observer. The remaining
obstacle is uniform extension of the complete relative prime flux to the dual
of this graph domain and its coupling to the completed zero-state condition.
