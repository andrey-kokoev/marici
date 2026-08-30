# 1690 — The Positive-Moment Comparison Is an Ordered Map, Not a Linear Relative Cone

## Comparison typing

Entry 1689 requires an independently declared target. Entries 1678--1680 supply
one: the finite Hankel/joint-moment positivity cones.

These targets are convex semialgebraic cones inside moment spaces. They are not
linear subcomplexes, so an ordinary kernel/cokernel or mapping-cone calculation
does not classify positivity.

The source-derived comparison is instead ordered:

1. a finite Dyson truncation acts by the one-Kraus map

   \[
   \rho\longmapsto U_{\le K}\rho U_{\le K}^{\dagger};
   \]

2. moment evaluation is a positive Gram/Hankel functional;
3. Cut reduction is partial trace and remains completely positive.

Entries 1679 and 1680 prove the finite moment congruences

\[
H_Z=T^T(H_X\otimes H_Y)T
\]

and

\[
H_Z=T^TM_{XY}T.
\]

Entry 1686 proves the one-Kraus CP factorization for every finite Dyson grade.
Therefore the dynamically reachable moment packet lands in the independently
declared positive cone by an order-preserving map.

## Normalization is separate

Complete positivity does not imply trace preservation for (U_{\le K}). The
trace/virtual comparison is already the distinct optical-theorem cell of
Entries 1633--1634. It must not be retyped as positivity cokernel data.

## Narrow result

\[
\boxed{
\text{the Dyson-to-positive-moment comparison is an ordered positive map, not a linear relative cone.}
}

No additional linear “positivity class” is defined by this comparison. Any
residual question concerns:

- normalization/trace balance;
- representability of truncated moments by full states;
- support-sensitive restrictions;
- or completion of the filtered ordered spaces.

This result does not prove that every positive truncated moment packet extends
to a physical density operator.

## Evidence

- Entries 1678--1680: independently declared finite positivity cones and
  congruences;
- Entry 1686: finite Dyson CP factorization;
- Entries 1633--1634: separate trace/virtual balance.

## Next falsifier

Test representability rather than linear cokernel. Identify the first positive
truncated noncommutative moment packet in the source filtration that fails to
extend to a positive density operator, or prove extension for a predeclared
finite class. Keep this distinct from Hankel positivity and Cut complete
positivity.
