# Two-prime real projective conjugacy forces the critical seam without a common Cayley frame

## Projective invariant

For determinant-one prime transport

\[
\widehat T_{p,z}
=\operatorname{diag}(p^{z/2},p^{-z/2}),
\qquad z=x+iy,
\]

the projective conjugacy invariant is

\[
\kappa_p(z)
=\frac{(\operatorname{tr}\widehat T_{p,z})^2}
       {\det\widehat T_{p,z}}
=4\cosh^2\left(\frac{z\log p}{2}\right).
\]

If the projective conjugacy class has a real representative, then
`kappa_p(z)` is real. Its imaginary part is

\[
\operatorname{Im}\kappa_p(z)
=2\sinh(x\log p)\sin(y\log p).
\]

## Two-prime separation

Assume `x != 0`. Reality at a prime `p` then forces

\[
y\log p\in\pi\mathbb Z.
\]

Apply this at `p=2` and `p=3`. If `y != 0`, there are integers `m,n` with

\[
y\log2=m\pi,
\qquad
y\log3=n\pi.
\]

Neither integer can vanish, and hence

\[
\frac{\log2}{\log3}=\frac mn.
\]

This would imply `2^n=3^m`, impossible by unique factorization. Therefore,
for `y != 0`, simultaneous reality at primes `2` and `3` forces

\[
x=0.
\]

Nontrivial Xi zeros have nonzero ordinate, so the exceptional real spectral
axis is absent from the target divisor.

## Advantage

This criterion does not require the amplituhedron and prime transports to be
written in one fixed Cayley frame. It requires only the weaker, frame-invariant
statements

\[
\kappa_2(z)\in\mathbb R,
\qquad
\kappa_3(z)\in\mathbb R.
\]

Thus rank-two real projective correspondence data at two primes are enough to
separate the critical seam. Rank-one boundary cells may be used in sewing;
only the final prime restrictions need rank two so that `kappa_p` is defined.

## Remaining source gate

Construct, from the two-phase four-presentation packet, rank-two projective
prime correspondences `M_(2,z)` and `M_(3,z)` such that

\[
\frac{(\operatorname{tr}M_{p,z})^2}{\det M_{p,z}}
=
4\cosh^2\left(\frac{z\log p}{2}\right).
\]

If canonical-form reality makes the left sides real, critical-line confinement
follows from the two-prime argument. This replaces full matrix identification
by equality of one conjugacy invariant at two fixed primes.