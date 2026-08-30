# The primitive current is the connection of the cutoff anomaly line

## Why the primitive channel should not be a graph covector

The critical primitive current escapes the Mellin–de Rham graph dual. This
does not prevent it from completing as relative line data. The determinant
packet already supplies the correct value type.

For a finite prime set `S`, put

\[
\tau_{1,S}(s)=\sum_{p\in S}p^{-s}.
\]

For an inclusion `S` into `T`, define the primitive transition unit

\[
g^{(1)}_{S,T}(s)
=
\exp\left[-\left(\tau_{1,T}(s)-\tau_{1,S}(s)\right)\right].
\]

Every finite transition is entire and nowhere zero.

## Exact cutoff coherence

For nested cutoffs `S` inside `T` inside `U`, additivity of finite prime sums
gives

\[
g^{(1)}_{S,U}
=g^{(1)}_{T,U}g^{(1)}_{S,T}.
\]

Thus the finite trivializations form a multiplicative line system over the
cutoff poset. No global scalar value of the divergent primitive sum is needed.

The primitive von Mangoldt current is its connection one-form:

\[
\frac{d}{ds}\log g^{(1)}_{S,T}(s)
=
\sum_{p\in T\setminus S}
(\log p)p^{-s}.
\]

This identifies the current before analytic continuation and without treating
it as a state vector or a continuous functional on the polynomial graph norm.

## Square transition and determinant-three packet

The square cumulant has the parallel transition

\[
g^{(2)}_{S,T}(s)
=
\exp\left[
-\frac12
\sum_{p\in T\setminus S}p^{-2s}
\right],
\]

with

\[
\frac{d}{ds}\log g^{(2)}_{S,T}(s)
=
\sum_{p\in T\setminus S}
(\log p)p^{-2s}.
\]

The order-three determinant carries the convergent connected tail. Hence the
three analytic grades have three different but compatible realizations:

```text
primitive: connection on an exponential anomaly line
square:     Hilbert/graph-grade line transition
tail:       ordinary determinant-three section
```

Their product reconstructs the finite determinant packet. They are not three
summands of one Hilbert operator.

## Comoving interpretation

On the sheet-aware comoving correspondence, each summand of the connection is
supported on the fixed zero section `(p,epsilon,0)`. The exponential growth
seen after pushforward is therefore the connection coefficient in a scalar
cutoff chart. It is not growth of a vector norm in the source line system.

Fourier exchanges the two sheet lines. Their finite transition ratio is the
local Tate sewing factor. On the critical seam that ratio is unitary, while
off the seam it is a nonunitary comparison. The line system retains this fact
without requiring either primitive scalar series to converge.

## Divisor consequence

Every finite cutoff transition is nowhere zero. Changing cutoff
trivialization therefore cannot create or remove a zero of a determinant
section. The primitive and square anomaly lines transport divisor data; they
do not generate divisor points by themselves.

This statement has a strict scope. A completed scalar section still requires
descent of the pro-line and its archimedean sewing. A nonconvergent sequence of
transition units cannot simply be replaced by a chosen scalar
renormalization. The hostile multiplier problem survives at the level of
canonical section rigidity.

## Falsifiers

1. Requiring the primitive connection coefficient to converge as a scalar.
2. Treating `g_(S,T)` as allowed to vanish.
3. Violating the triangle law under three cutoff refinements.
4. Adding primitive, square, and tail as independent Hilbert operators.
5. Claiming that nowhere-zero finite transitions prove completed section
   nonvanishing.

## Result

The critical primitive current has a canonical completion type despite its
failure as a Mellin–de Rham graph covector. It is the logarithmic connection
of a cutoff anomaly line whose finite transitions are coherent and nowhere
zero. The square current is the next line grade, and the connected tail is the
ordinary determinant-three section. The next gate is canonical reciprocal and
archimedean descent of this pro-line, not stronger polynomial graph control.
