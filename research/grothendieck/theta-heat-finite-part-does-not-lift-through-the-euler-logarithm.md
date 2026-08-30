# Theta heat finite part does not lift through the Euler logarithm

## Apparent shortcut

The theta heat construction already gives a canonical relative finite part

\[
\operatorname{FP}_{\varepsilon\downarrow0}
\left[Z_\varepsilon(s)-B_\varepsilon(s)\right]
=\zeta(s).
\]

Could this scalar finite part be pulled backward through the Euler product to
supply the primitive and square finite-part sewing on the compactified prime
scale?

It cannot. The obstruction is the nonlinear logarithm.

## Failure of the logarithmic square

Write schematically in the critical half-strip

\[
Z_\varepsilon(s)
=B_\varepsilon(s)+\zeta(s)+o(1),
\qquad
|B_\varepsilon(s)|\to\infty.
\]

Then

\[
\log Z_\varepsilon
=
\log B_\varepsilon
+
\log\left(1+\frac{\zeta(s)+o(1)}{B_\varepsilon}
\right).
\]

The second term tends to zero. After subtracting the divergent logarithmic
boundary term, the remaining constant is controlled by the chosen boundary
normalization of \(B_\varepsilon\), not by \(\log\zeta(s)\).

Thus

\[
\operatorname{FP}(\log Z_\varepsilon)
\ne
\log\left(
\operatorname{FP}(Z_\varepsilon-B_\varepsilon)
\right)
\]

in general. At a zero of \(\zeta\), the right-hand logarithm is not even
defined, whereas every regulated \(Z_\varepsilon\) may remain nonzero.

## Categorical interpretation

The heat finite part is a scalar pushforward from the full integer/Fock
source. Primitive and prime-square currents are coordinates of the
determinant-line logarithm before scalar completion. The desired diagram

\[
\begin{array}{ccc}
\text{regulated Fock source}&\longrightarrow&\text{relative scalar}\\
\downarrow\log&&\downarrow\log\\
\text{typed prime currents}&\longrightarrow&\text{boundary finite part}
\end{array}
\]

does not commute.

Consequently the known heat regulator proves existence and provenance of the
completed scalar section but supplies no lift to the two scale-boundary
grades. Recovering primitive and square data afterward would require choosing
a logarithm across the divisor and would import the zero set.

## Why one archimedean line is insufficient after projection

On the scale pullback, primitive and square currents have distinct boundary
orders. The scalar heat boundary term combines all integer and prime-power
labels before the logarithmic filtration is exposed. Once compressed, it
cannot determine how its finite part should split between the half-order and
zero-order prime boundaries.

This is not merely a dimension count. Different typed lifts can have the same
scalar finite part while differing by a primitive–square boundary
coboundary. The scalar detector sees only their pushforward.

## Surviving construction

The finite-part sewing must therefore be built on a multiplicative or
determinant-line object before scalar heat extraction. The exact local
identity

\[
E_p-I+N_p
=
\sum_{k\ge2}P_{p^k\mid n}
\]

already supplies the primitive-to-square filtration step. The next admissible
diagram must combine:

1. the compactified prime-scale pullback;
2. the primitive boundary projection;
3. valuation degree;
4. the square-and-higher remainder;
5. the archimedean boundary line;
6. scalar heat finite part only after those incidences commute.

The decisive test is a Beck–Chevalley square between scale-boundary pullback
and valuation/Fock pushforward. If it closes, the scalar heat detector is the
pushforward of a typed relative current. If it does not, scalar regulator
universality cannot be promoted to arithmetic boundary sewing.

## Result

The source-derived scalar heat finite part cannot be pulled backward through
the Euler logarithm. Finite part and logarithm fail to commute, particularly
at the divisor. The missing theorem is a pre-scalar determinant/Fock lift of
the finite-part current, tested by a scale-boundary/valuation
Beck–Chevalley square.
