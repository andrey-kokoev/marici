# Scalar continuation of primitive current imports the zeta divisor

## Question

The connected third-order determinant tail converges around the critical
seam, while the primitive and square currents remain relative boundary data.
Can those first two currents be continued separately as scalar holomorphic
functions and then reassembled?

## Prime-zeta inversion

Let

\[
P(s)=\sum_pp^{-s}
\]

in \(\Re s>1\).  The Euler logarithm gives

\[
\log\zeta(s)
=
\sum_{k\ge1}\frac{P(ks)}{k}.
\]

Möbius inversion yields

\[
P(s)
=
\sum_{m\ge1}
\frac{\mu(m)}{m}
\log\zeta(ms).
\]

Thus scalar continuation of the primitive current is expressed through
logarithms of the completed section at scaled arguments.

## Divisor dependence

Every zero or pole of \(\zeta(ms)\) becomes a logarithmic singularity or
branch point of a scalar branch of \(P(s)\).  Therefore a continuation of
\(P\) into the critical strip cannot be specified globally without knowing
and cutting around the divisor of \(\zeta\).

The square current is

\[
P_2(s)=\frac12P(2s),
\]

so it inherits the same problem at scaled locations.  Treating these currents
as separately continued scalar functions imports exactly the divisor that the
operator programme is supposed to derive.

This is not merely a poor choice of logarithm.  The monodromy around a zero is
the scalar shadow of nontrivial determinant-line winding.  Erasing it by a
branch choice discards the boundary capability.

## Why the connected tail is different

The third-order tail

\[
P_{\ge3}(s)
=
\sum_p\sum_{k\ge3}\frac{p^{-ks}}{k}
\]

converges absolutely for \(\Re s>1/3\).  It is an ordinary holomorphic scalar
near the critical seam and needs no divisor information.

Hence the three current levels differ categorically:

- the connected tail may be scalarized before completion;
- the primitive and square currents cannot be scalarized there without
  importing determinant monodromy;
- they must remain typed boundary objects until the global section is formed.

## Correct order of operations

The only noncircular order is:

1. retain primitive and square currents as labelled boundary operators or
   distributions;
2. combine them with the connected determinant tail;
3. sew the reciprocal valuation sectors and the rank-two archimedean boundary;
4. form the completed determinant line;
5. only then take its scalar section.

The forbidden order is to analytically continue \(P(s)\) through
\(\log\zeta(ms)\), insert it into a regularized Euler product, and claim the
resulting section was source-derived.

## Consequence for canonical-section rigidity

Finite bordered systems have canonical divisors up to units.  To pass this
rigidity through completion, the comparison maps must be constructed on the
boundary-bearing operator packet, not on scalar prime-zeta branches.

If one scalarizes first, different branch cuts appear as apparently different
completion units even though they carry divisor monodromy.  Local uniform
unit convergence cannot be established because the proposed units are not
globally single-valued on domains surrounding zeros.

## Source-level alternative

The completed theta representation sums labelled integer states before prime
separation.  Its modular sewing is entire and does not require prime-zeta
branches.  This suggests the arithmetic boundary currents should enter as
operators acting on the integer-labelled Fock module, while theta/Poisson
completion supplies the global determinant section.

The bordered prime blocks remain valid local charts, but their primitive and
square scalar logarithms are not global coordinates.  Their correct global
objects are relative transition currents.

## Falsifier

Any proposed global determinant construction fails the noncircularity gate if
its definition of the primitive or square port uses:

- \(\log\zeta\);
- a branch cut chosen from known or conjectured zero locations;
- cancellation verified only after scalar aggregation;
- a continuation unit whose monodromy is not tracked in the determinant line.

The successful construction must exist on simply described source domains
before a scalar divisor is known.

## Result

Separate scalar continuation of the primitive and prime-square currents is
circular: Möbius inversion imports the zeta divisor and its monodromy.  These
currents must remain boundary-bearing operator data until reciprocal and
archimedean sewing have produced the completed determinant section.
