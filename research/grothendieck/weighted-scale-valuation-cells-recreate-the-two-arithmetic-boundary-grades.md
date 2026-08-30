# Weighted scale-valuation cells recreate the two arithmetic boundary grades

## Question

The scale/valuation Beck–Chevalley cell tends to zero on every fixed compact
set as \(p\to\infty\). Does its prime-weighted sum therefore remain in the
Gaussian bulk?

No. The cells move outward with prime scale, and prime density accumulates
along that moving support.

## The adjacent square cell

Write

\[
\alpha_p(q)
=W_{2\log p}(q)-W_{\log p}(q).
\]

For large positive \(q\), this is approximately negative one when

\[
\frac q2<\log p<q
\]

and approximately zero outside that moving band. The Gaussian edges only
smooth its two endpoints.

Thus the primitive-weighted aggregate has the prime-number-theorem model

\[
A_1(q)
=
\sum_p p^{-1/2}\alpha_p(q)
\sim
-\int_{e^{q/2}}^{e^q}\frac{x^{-1/2}}{\log x}\,dx.
\]

Its magnitude has exponential scale

\[
|A_1(q)|\asymp\frac{e^{q/2}}q.
\]

The primitive comparison therefore leaves not only every Gaussian step but
every decaying tail space.

For the square weight,

\[
A_2(q)
=
\sum_p p^{-1}\alpha_p(q)
\sim
-\int_{e^{q/2}}^{e^q}\frac{dx}{x\log x}
=-\log2.
\]

The square comparison approaches a nonzero constant boundary plateau.

## Why compact-local convergence misled us

For each fixed \(q\), one cell \(\alpha_p(q)\) tends rapidly to zero as
\(p\to\infty\). But the number of primes whose moving bands cross a large
\(q\) grows exponentially. Pointwise decay in the label is not uniform after
the observation coordinate is allowed to follow the label scale.

This is a traveling-support version of escape at infinity. The source packet
does not disappear; it moves to \(q\simeq\log p\), where the arithmetic
multiplicity reconstructs a boundary mode.

## Exact recovery of the two grades

The Beck–Chevalley cell did not eliminate the primitive/square distinction.
It translated that distinction into archimedean growth types:

- primitive weight produces an exponentially growing distributional wall;
- square weight produces a constant, Hilbert-but-non-trace-class wall;
- higher weights decay and belong to the connected tail.

This matches the previously derived three-level Tate filtration. The scale
pullback has therefore recovered, rather than assumed, why primitive and
square channels require separate completion grades.

## Consequence for finite-part sewing

No fixed archimedean line can absorb the primitive traveling wall. Its size
depends on the moving cutoff scale. The required boundary operation must be
cutoff-covariant and live on the joint \((p,q)\) correspondence before either
prime summation or archimedean projection.

The square plateau can land in the fifth constant–delta wall, but only after
the primitive traveling component has been retained separately. Collapsing
both into the same constant fiber loses the exponential grade.

## Remaining gate

The source object must now be enlarged from a pullback over scale to a
properly supported correspondence over both prime scale and observation
position. The natural coordinate is the relative displacement

\[
u=q-\log p.
\]

In that comoving coordinate the cells stop traveling. The next theorem is to
rewrite primitive, square, and archimedean currents on this groupoid and test
whether reciprocal sewing becomes a continuous pushforward there.

## Result

Prime-weighted scale/valuation 2-cells do not remain Gaussian bulk. Primitive
weights create an \(e^{q/2}/q\) traveling wall and square weights create a
constant plateau. The two arithmetic boundary grades reappear exactly under
global pushforward. A comoving scale-observation correspondence is required
before finite-part sewing.
