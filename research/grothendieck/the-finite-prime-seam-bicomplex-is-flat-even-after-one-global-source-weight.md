# The finite prime-seam bicomplex is flat even after one global source weight

## Bare boundary cocycle

Let `S_a` be the right-shift isometry on the half-line and let

\[
P_a=1-S_aS_a^*
\]

be projection onto `[0,a)`. The semigroup law `S_aS_b=S_{a+b}` gives

\[
P_{a+b}=P_a+S_aP_bS_a^*.
\]

This is the exact boundary-defect composition law.

For two primes with lengths `a=log p` and `b=log q`, the two attachment
orders give

\[
P_a+S_aP_bS_a^*=P_{a+b}
\]

and

\[
P_b+S_bP_aS_b^*=P_{a+b}.
\]

Their interval decompositions differ, but both become the same projection on
the common divisor-chamber refinement. The two-prime square has trivial
holonomy.

Associativity of the shift semigroup proves the same statement for every
finite prime packet. Every parenthesized composition gives `P` for the total
logarithmic length. The three-prime cube and hexagon are therefore flat before
any coefficient is added.

## Add one global theta-source weight

Let `M_f` denote multiplication by one common source function. Its failure to
commute with the backward translation `R_a` is

\[
[M_f,R_a]
=M_{f-f(\cdot+a)}R_a.
\]

This is nonzero for the theta source, so source weighting does create a local
prime-scale defect. But it is the finite difference of one global potential.
Writing

\[
\delta_af=f-f(\cdot+a),
\]

the commuting translations imply

\[
\delta_a\delta_bf=\delta_b\delta_af.
\]

Hence every finite mixed source defect is an iterated coboundary. The source
weight does not create finite curvature or factorization-order holonomy.

## Consequence

The Koszul-Toeplitz construction of ledger 3828 is exact and source-native,
but its finite prime geometry is flat. It supplies:

- the correct cross-label differential;
- the correct moving-window boundary defect;
- strict compatibility with all finite prime orders;
- no zero-confining inner-factor record.

This agrees with Nima's independent result that the source-Gram tower is a
global Stein coboundary.

## Where a nontrivial class can still arise

Only mechanisms absent from one finite global potential remain:

1. failure of the global source weight to extend through restricted-product
   completion;
2. inequivalent counterterms for determinant and Gram completions;
3. an archimedean boundary contribution not represented by finite shifts;
4. a genuinely noncommutative or prime-dependent coefficient system;
5. reciprocal sewing that acts on domains rather than on the common scalar
   source alone.

The first three are completion-at-infinity phenomena. Accumulating larger
finite prime cubes cannot reveal them because flatness is already exact at
arbitrary finite order.

## Falsifier

Any claimed finite mixed curvature derived solely from commuting prime shifts
and one global multiplication source must vanish after common refinement. A
nonzero reported residual indicates inconsistent domains, omitted boundary
windows, or a coefficient that was not actually one global source potential.

## Scope

This closes the finite-holonomy version of the prime-seam bicomplex. It does
not analyze restricted-product completion, archimedean sewing, noncommutative
coefficients, the inner-factor phase record, or RH.
