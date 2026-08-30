# The Mellin observer has an exact off-seam dual-energy norm

## Energy space

On the nonvacuum coefficient module, the source interval energy is

\[
\mathcal E(c)
=
2\sum_{n\ge2}
(\log n)|c_n|^{2}.
\]

For

\[
s=\sigma+it,
\]

the Mellin observer is

\[
\ell_s(c)
=
\sum_{n\ge2}
c_n n^{-s},
\]

with the vacuum coordinate handled separately by the constant wall.

## Exact dual norm

Cauchy–Schwarz in the energy metric gives

\[
|\ell_s(c)|^{2}
\le
\left(
\sum_{n\ge2}
\frac{n^{-2\sigma}}{2\log n}
\right)
\mathcal E(c).
\]

This constant is sharp. The squared dual-energy norm of the nonvacuum observer is therefore

\[
\|\ell_s\|_{\mathcal E^{*}}^{2}
=
\sum_{n\ge2}
\frac{n^{-2\sigma}}{2\log n}.
\]

It is independent of \(t\), although the observer itself retains every Mellin phase.

## Seam threshold

The series converges exactly for

\[
\sigma>\frac12.
\]

At the seam,

\[
\sum_{n\ge2}
\frac1{2n\log n}
\]

diverges.

Thus the source observer is a bounded functional on the interval-energy Hilbert space throughout the open right sector, uniformly on compact sets

\[
\sigma\ge\frac12+\varepsilon,
\]

but it does not extend as a bounded Hilbert functional to the seam.

The reciprocal statement holds in the opposite sector after the typed sheet transformation.

## Consequence for the mixed kernel

For every off-seam \(s\), the Riesz representative of the nonvacuum observer is

\[
r_s(n)
=
\frac{n^{-\overline s}}{2\log n}
\]

in the energy coordinates. This supplies a canonical rank-one mixed block at the Hilbert level off the seam.

But the seam limit of \(r_s\) leaves the energy space. Therefore:

- the mixed source–observer kernel is Hilbert-bounded off seam;
- its seam value must be a rigged boundary distribution;
- no completion theorem may demand uniform Hilbert control through \(\sigma=1/2\);
- wall and archimedean ports must carry the boundary value, not falsely repair the bulk dual norm.

## What this does not prove

Boundedness of \(\ell_s\) does not give the missing Green identity

\[
2\Re(s-\tfrac12)\mathcal E
=
\text{completed mixed boundary flux}.
\]

Nor does the Riesz representative identify the completed \(\xi\)-section. It only proves that the off-seam mixed incidence exists canonically in the source energy geometry.

The scalar zero condition remains cancellation in \(\ell_s(c)\), not loss of state energy.

## New completion gate

The completed observer should be constructed as a rigged family

\[
\ell_s:
\mathcal E_{\mathrm{test}}
\longrightarrow
\mathbb C
\]

whose off-seam Hilbert representatives are \(r_s\) and whose seam limit lands in the declared boundary dual.

The source Green identity must intertwine this Abelian boundary limit with the external constant-delta and archimedean ports.

## Minimal hostile

A proposed completion inserts an extra logarithmic weight so that

\[
\sum \frac1{n(\log n)^{1+\epsilon}}
\]

converges on the seam. It obtains Hilbert boundedness, but changes the source interval energy and is therefore unauthorized.

The genuine divergence is structural: the seam observer is distributional even though every compact off-seam observer is bounded.
